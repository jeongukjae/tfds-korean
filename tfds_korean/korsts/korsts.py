"""korsts dataset."""
import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
The dataset for the paper [_KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding_](https://arxiv.org/abs/2004.03289).
"""

_CITATION = """
@article{ham2020kornli,
    title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
    author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
    journal={arXiv preprint arXiv:2004.03289},
    year={2020}
}
"""


class Korsts(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "genre": tfds.features.Text(),
                    "filename": tfds.features.Text(),
                    "year": tfds.features.Text(),
                    "sentence1": tfds.features.Text(),
                    "sentence2": tfds.features.Text(),
                    "score": tfds.features.Tensor(shape=[], dtype=tf.float32),
                }
            ),
            supervised_keys=None,  # TODO ((sentence1, sentence2), score)
            homepage="https://github.com/kakaobrain/KorNLUDatasets",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download(
            {
                "train": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorSTS/sts-train.tsv",
                "dev": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorSTS/sts-dev.tsv",
                "test": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorSTS/sts-test.tsv",
            }
        )

        return {
            "train": self._generate_examples(splits["train"]),
            "dev": self._generate_examples(splits["dev"]),
            "test": self._generate_examples(splits["test"]),
        }

    def _generate_examples(self, split_file):
        columns = ["genre", "filename", "year", "id", "score", "sentence1", "sentence2"]
        columns = {key: index for index, key in enumerate(columns)}
        with split_file.open() as f:
            next(f)
            for line in f:
                row = line.strip().split("\t")
                yield f"{row[columns['filename']]}-{row[columns['year']]}-{row[columns['id']]}", {
                    "genre": row[columns["genre"]],
                    "filename": row[columns["filename"]],
                    "year": row[columns["year"]],
                    "sentence1": row[columns["sentence1"]],
                    "sentence2": row[columns["sentence2"]],
                    "score": float(row[columns["score"]]),
                }
