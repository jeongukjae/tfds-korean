"""nsmc dataset."""

import csv

import tensorflow_datasets as tfds

_DESCRIPTION = """
Naver sentiment movie corpus v1.0

This is a movie review dataset in the Korean language. Reviews were scraped from [Naver Movies](http://movie.naver.com/movie/point/af/list.nhn).
The dataset construction is based on the method noted in [Large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) from Maas et al., 2011.
"""

# TODO(nsmc): BibTeX citation
_CITATION = """
"""


class Nsmc(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "document": tfds.features.Text(),
                    "label": tfds.features.ClassLabel(num_classes=2),
                }
            ),
            supervised_keys=("document", "label"),
            homepage="https://github.com/e9t/nsmc",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download(
            {
                "train": "https://raw.githubusercontent.com/e9t/nsmc/cc0670e872d4ac27bfe36c87456783004b39ef6c/ratings_train.txt",
                "test": "https://raw.githubusercontent.com/e9t/nsmc/cc0670e872d4ac27bfe36c87456783004b39ef6c/ratings_test.txt",
            }
        )

        return {
            "train": self._generate_examples(splits["train"]),
            "test": self._generate_examples(splits["test"]),
        }

    def _generate_examples(self, split_file):
        with split_file.open() as f:
            for row in csv.DictReader(f, delimiter="\t"):
                yield row["id"], {
                    "document": row["document"],
                    "label": row["label"],
                }
