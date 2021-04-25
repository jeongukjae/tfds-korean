"""namuwikitext dataset."""

import tensorflow_datasets as tfds

from . import namuwikitext


class NamuwikitextTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = namuwikitext.Namuwikitext
    SPLITS = {
        "train": 5,
        "dev": 2,
        "test": 2,
    }

    DL_EXTRACT_RESULT = {
        "train": "train",
        "dev": "dev",
        "test": "test",
    }


if __name__ == "__main__":
    tfds.testing.test_main()
