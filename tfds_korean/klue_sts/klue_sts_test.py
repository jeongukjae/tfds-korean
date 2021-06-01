"""klue_sts dataset."""

import tensorflow_datasets as tfds

from . import klue_sts


class KlueStsTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for klue_sts dataset."""

    DATASET_CLASS = klue_sts.KlueSts
    SPLITS = {"train": 3, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "train.json", "dev": "dev.json"}


if __name__ == "__main__":
    tfds.testing.test_main()
