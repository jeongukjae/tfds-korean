"""question_pair dataset."""

import csv

import tensorflow_datasets as tfds

_DESCRIPTION = """
짝 지어진 두 개의 질문이 같은 질문인지 다른 질문인지 핸드 레이블을 달아둔 데이터.
사랑, 이별, 또는 일상과 같은 주제로 도메인 특정적이지 않음.
"""

# TODO(question_pair): BibTeX citation
_CITATION = """
"""


class QuestionPair(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for question_pair dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "question1": tfds.features.Text(),
                    "question2": tfds.features.Text(),
                    "is_duplicate": tfds.features.ClassLabel(names=["0", "1"]),
                }
            ),
            supervised_keys=None,  # TODO ((question1, question2), is_duplicate)
            homepage="https://github.com/songys/Question_pair",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download(
            {
                "train": "https://raw.githubusercontent.com/songys/Question_pair/e84b6f0e784c10c6a22cbbc7b1e415b901baa877/train.txt",
                "test": "https://raw.githubusercontent.com/songys/Question_pair/e84b6f0e784c10c6a22cbbc7b1e415b901baa877/test.txt",
                "validation": "https://raw.githubusercontent.com/songys/Question_pair/e84b6f0e784c10c6a22cbbc7b1e415b901baa877/validation.txt",
            }
        )

        return {
            "train": self._generate_examples(splits["train"], split_name="train"),
            "test": self._generate_examples(splits["test"], split_name="test"),
            "validation": self._generate_examples(splits["validation"], split_name="validation"),
        }

    def _generate_examples(self, split_file, split_name):
        with split_file.open() as f:
            for index, row in enumerate(csv.DictReader(f, delimiter="\t")):
                yield f"{split_name}-{index}", {
                    "question1": row["question1"],
                    "question2": row["question2"],
                    "is_duplicate": row["is_duplicate"],
                }
