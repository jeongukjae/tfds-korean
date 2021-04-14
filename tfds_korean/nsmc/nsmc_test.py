"""nsmc dataset."""

import tensorflow_datasets as tfds

from . import nsmc


class NsmcTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for nsmc dataset."""

    DATASET_CLASS = nsmc.Nsmc
    SPLITS = {
        "train": 5,
        "test": 3,
    }

    DL_EXTRACT_RESULT = {"train": "ratings_train.txt", "test": "ratings_test.txt"}


if __name__ == "__main__":
    tfds.testing.test_main()
