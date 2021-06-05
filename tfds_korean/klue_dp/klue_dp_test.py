"""klue_dp dataset."""

import tensorflow_datasets as tfds

from . import klue_dp


class KlueDpTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for klue_dp dataset."""

    DATASET_CLASS = klue_dp.KlueDp
    SPLITS = {"train": 3, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "train.tsv", "dev": "dev.tsv"}


if __name__ == "__main__":
    tfds.testing.test_main()
