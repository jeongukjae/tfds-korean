"""question_pair dataset."""

import tensorflow_datasets as tfds

from . import question_pair


class QuestionPairTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for question_pair dataset."""

    DATASET_CLASS = question_pair.QuestionPair
    SPLITS = {
        "train": 3,  # Number of fake train example
        "test": 1,  # Number of fake test example
        "validation": 1,  # Number of fake test example
    }

    DL_EXTRACT_RESULT = {"train": "train.txt", "test": "test.txt", "validation": "validation.txt"}


if __name__ == "__main__":
    tfds.testing.test_main()
