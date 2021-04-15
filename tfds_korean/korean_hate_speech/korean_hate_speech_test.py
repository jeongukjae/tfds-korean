"""korean_hate_speech dataset."""
import tensorflow_datasets as tfds

from . import korean_hate_speech


class KoreanHateSpeechLabeledTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for labeled korean_hate_speech dataset."""

    DATASET_CLASS = korean_hate_speech.KoreanHateSpeech
    BUILDER_CONFIG_NAMES_TO_TEST = ["labeled"]
    SPLITS = {
        "train": 3,
        "dev": 1,
        "test": 1,
    }

    DL_EXTRACT_RESULT = {
        "train": "train.tsv",
        "train_title": "train.news_title.txt",
        "dev": "dev.tsv",
        "dev_title": "dev.news_title.txt",
        "test": "test.no_label.tsv",
        "test_title": "test.news_title.txt",
    }


class KoreanHateSpeechUnlabeledTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for unlabeled korean_hate_speech dataset."""

    DATASET_CLASS = korean_hate_speech.KoreanHateSpeech
    BUILDER_CONFIG_NAMES_TO_TEST = ["unlabeled"]
    SPLITS = {
        "train": 3,
    }

    DL_EXTRACT_RESULT = {
        "0": "unlabeled_comments.news_title_1.txt",
        "1": "unlabeled_comments.news_title_2.txt",
        "2": "unlabeled_comments.news_title_3.txt",
        "3": "unlabeled_comments.news_title_4.txt",
        "4": "unlabeled_comments.news_title_5.txt",
        "0_title": "unlabeled_comments_1.txt",
        "1_title": "unlabeled_comments_2.txt",
        "2_title": "unlabeled_comments_3.txt",
        "3_title": "unlabeled_comments_4.txt",
        "4_title": "unlabeled_comments_5.txt",
    }


if __name__ == "__main__":
    tfds.testing.test_main()
