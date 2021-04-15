import argparse
import importlib
import os
from typing import Iterable

import tensorflow_datasets.public_api as tfds
from absl import logging
from jinja2 import Template

from . import __version__

parser = argparse.ArgumentParser()
parser.add_argument("--index_template", default="./templates/index.md")
parser.add_argument("--dataset_template", default="./templates/dataset.md")
parser.add_argument("--multi_config_dataset_template", default="./templates/multi_config_dataset.md")
parser.add_argument("--catalog_output", default="./docs")
parser.add_argument("--catalog_dataset_output", default="./docs/docs")


def main():
    logging.set_verbosity(logging.INFO)
    args = parser.parse_args()

    #
    # read templates and prepare output path
    logging.info("Read templates")
    with open(args.index_template, encoding="utf8") as f:
        index_template = Template(f.read())
    with open(args.dataset_template, encoding="utf8") as f:
        dataset_template = Template(f.read())
    with open(args.multi_config_dataset_template, encoding="utf8") as f:
        multi_config_dataset_template = Template(f.read())

    logging.info("Prepare output directory(--catalog_output)")
    if not os.path.exists(args.catalog_output):
        os.mkdir(args.catalog_output)
    elif not os.path.isdir(args.catalog_output):
        raise ValueError(f"{args.catalog_output} already exists, but is not a directory.")
    dataset_doc_path = os.path.join(args.catalog_output, "datasets")
    os.makedirs(dataset_doc_path, exist_ok=True)

    #
    # fetch all datasets
    cwd = os.path.dirname(__file__)
    excludes = ["__pycache__"]
    dataset_pkgs = sorted([path for path in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, path)) and path not in excludes])
    logging.info(f"Loaded dataset: {dataset_pkgs}")

    #
    # render docs for all datasets
    logging.info("Render index page")
    with open(os.path.join(args.catalog_output, "index.md"), "w", encoding="utf8") as f:
        print(index_template.render(version=__version__, dataset_names=dataset_pkgs), file=f)

    logging.info("Render dataset catalogs")
    for pkg in dataset_pkgs:
        logging.info(f"Render dataset {pkg}")
        globals()[f"__tfds_korean_{pkg}"] = importlib.import_module(f"tfds_korean.{pkg}")

        builder = tfds.builder(pkg)

        if len(builder.BUILDER_CONFIGS) == 0:
            builder.download_and_prepare()
            with open(os.path.join(dataset_doc_path, f"{pkg}.md"), "w", encoding="utf8") as f:
                ds_df = tfds.as_dataframe(builder.as_dataset()[list(builder.info.splits.keys())[0]], builder.info)[:10]
                decoded_ds_df_values = _decode_df_values(ds_df.values)
                logging.info("Saving...")
                print(
                    dataset_template.render(
                        name=str(builder.info.name),
                        version=str(builder.info.version),
                        release_notes=list(builder.release_notes.items()),
                        description=str(builder.info.description),
                        homepage=str(builder.info.homepage),
                        download_size=str(builder.info.download_size),
                        dataset_size=str(builder.info.dataset_size),
                        features=str(builder.info.features),
                        supervised_keys=str(builder.info.supervised_keys),
                        splits=list(builder.info.splits.items()),
                        citation=str(builder.info.citation),
                        examples={"columns": ds_df.columns, "rows": decoded_ds_df_values},
                    ),
                    file=f,
                )
                logging.info("Done")

            continue

        default_infos = dict(
            name=str(builder.info.name),
            description=str(builder.info.description),
            homepage=str(builder.info.homepage),
            version=str(builder.info.version),
            release_notes=list(builder.release_notes.items()),
            citation=str(builder.info.citation),
            default_config=str(builder.BUILDER_CONFIGS[0].name),
        )
        config_infos = []
        for config in builder.BUILDER_CONFIGS:
            builder = tfds.builder(f"{pkg}/{config.name}")
            builder.download_and_prepare()

            ds_df = tfds.as_dataframe(builder.as_dataset()[list(builder.info.splits.keys())[0]], builder.info)[:10]
            decoded_ds_df_values = _decode_df_values(ds_df.values)

            config_infos.append(
                dict(
                    name=config.name,
                    description=config.description,
                    dataset_size=str(builder.info.dataset_size),
                    download_size=str(builder.info.download_size),
                    splits=list(builder.info.splits.items()),
                    features=str(builder.info.features),
                    examples={"columns": ds_df.columns, "rows": decoded_ds_df_values},
                )
            )

        with open(os.path.join(dataset_doc_path, f"{pkg}.md"), "w", encoding="utf8") as f:
            logging.info("Saving...")
            print(multi_config_dataset_template.render(**default_infos, configs=config_infos), file=f)
            logging.info("Done")


def _decode_df_values(df_values):
    return [[_decode_cell(cell) for cell in row] for row in df_values]


def _decode_cell(cell):
    if isinstance(cell, bytes):
        value = cell.decode("utf8").strip().replace("\n", " ")
        if len(value) > 50:
            value = value[:47] + "..."
        return value

    if isinstance(cell, Iterable) and all([isinstance(val, bytes) for val in cell]):
        value = [_decode_cell(val) for val in cell]
        if len(value) > 5:
            value = value[:4] + ["..."]
        return "<br>".join(value)

    if isinstance(cell, float):
        return f"{cell:.4f}"

    return str(cell)


if __name__ == "__main__":
    main()
