"""kornli dataset."""

import tensorflow_datasets as tfds

from . import kornli


class KornliTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = kornli.Kornli
    SPLITS = {
        "mnli_train": 3,  # Number of fake train example
        "snli_train": 3,  # Number of fake test example
        "xnli_dev": 1,  # Number of fake test example
        "xnli_test": 1,  # Number of fake test example
    }

    DL_EXTRACT_RESULT = {
        "mnli_train": "multinli.train.ko.tsv",
        "snli_train": "snli_1.0_train.ko.tsv",
        "xnli_dev": "xnli.dev.ko.tsv",
        "xnli_test": "xnli.test.ko.tsv",
    }


if __name__ == "__main__":
    tfds.testing.test_main()
