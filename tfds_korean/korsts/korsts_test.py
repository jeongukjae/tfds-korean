"""korsts dataset."""

import tensorflow_datasets as tfds

from . import korsts


class KorstsTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for korsts dataset."""

    DATASET_CLASS = korsts.Korsts
    SPLITS = {
        "train": 3,
        "dev": 1,
        "test": 1,
    }

    DL_EXTRACT_RESULT = {
        "train": "sts-train.tsv",
        "dev": "sts-dev.tsv",
        "test": "sts-test.tsv",
    }


if __name__ == "__main__":
    tfds.testing.test_main()
