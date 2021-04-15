"""korean_chatbot_qa_data dataset."""

import tensorflow_datasets as tfds

from . import korean_chatbot_qa_data


class KoreanChatbotQaDataTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = korean_chatbot_qa_data.KoreanChatbotQaData
    SPLITS = {
        "train": 1,
    }

    DL_EXTRACT_RESULT = "Chatbot .csv"


if __name__ == "__main__":
    tfds.testing.test_main()
