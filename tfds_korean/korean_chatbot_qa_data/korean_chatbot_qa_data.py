"""korean_chatbot_qa_data dataset."""
import csv

import tensorflow_datasets as tfds

_DESCRIPTION = """
Chatbot_data_for_Korean v1.0
"""

# TODO(korean_chatbot_qa_data): BibTeX citation
_CITATION = """
"""


class KoreanChatbotQaData(tfds.core.GeneratorBasedBuilder):
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
                    "Q": tfds.features.Text(),
                    "A": tfds.features.Text(),
                    "label": tfds.features.ClassLabel(names=["0", "1", "2"]),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/songys/Chatbot_data",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        train_filepath = dl_manager.download(
            "https://raw.githubusercontent.com/songys/Chatbot_data/a22e508811b5040eead0be5a89c27ef3780d4e82/ChatbotData%20.csv"
        )

        return {
            "train": self._generate_examples(train_filepath),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for index, row in enumerate(csv.DictReader(f)):
                yield f"row-{index}", {"Q": row["Q"], "A": row["A"], "label": row["label"].strip()}
