"""kowikitext dataset."""

import tensorflow_datasets as tfds

from . import kowikitext


class KowikitextTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = kowikitext.Kowikitext
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
