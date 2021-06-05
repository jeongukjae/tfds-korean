"""klue_dst dataset."""

import tensorflow_datasets as tfds

from . import klue_dst


class KlueDstTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for klue_dst dataset."""

    DATASET_CLASS = klue_dst.KlueDst
    SPLITS = {"train": 1, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "train.json", "dev": "dev.json"}


if __name__ == "__main__":
    tfds.testing.test_main()
