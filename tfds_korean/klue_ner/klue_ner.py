"""klue_ner dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Named Entity Recognition(NER) task.

For more details, see [KLUE Benchmark - NER Task - Overview description](https://klue-benchmark.com/tasks/69/overview/description)
"""

_CITATION = """
@misc{park2021klue,
    title={KLUE: Korean Language Understanding Evaluation},
    author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
    year={2021},
    eprint={2105.09680},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

_LICENSE = """
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/69/overview/copyright).
"""


class KlueNer(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "tokens": tfds.features.Sequence(tfds.features.Text()),
                    "labels": tfds.features.Sequence(tfds.features.Text()),
                }
            ),
            supervised_keys=("tokens", "labels"),
            homepage="https://github.com/KLUE-benchmark/KLUE",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        files = dl_manager.download_and_extract(
            {
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-ner-v1/klue-ner-v1_train.tsv",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-ner-v1/klue-ner-v1_dev.tsv",
            }
        )

        return {
            "train": self._generate_examples(files["train"]),
            "dev": self._generate_examples(files["dev"]),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            example_name = None
            tokens = []
            labels = []
            for line in f:
                line = line.rstrip()

                if line == "":
                    assert tokens and labels and example_name
                    yield example_name, {"tokens": tokens, "labels": labels}

                    tokens = []
                    labels = []
                    example_name = None
                    continue

                if line.startswith("##"):
                    if "\t" not in line:
                        continue

                    example_name = line[2:].split("\t")[0].strip()
                    continue

                token, label = line.split("\t")
                tokens.append(token)
                labels.append(label)

            if example_name is not None:
                yield example_name, {"tokens": tokens, "labels": labels}
