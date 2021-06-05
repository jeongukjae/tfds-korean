"""klue_tc dataset."""

import tensorflow_datasets as tfds

from . import klue_tc


class KlueTcTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for klue_tc dataset."""

    DATASET_CLASS = klue_tc.KlueTc
    SPLITS = {"train": 2, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "train.json", "dev": "dev.json"}


if __name__ == "__main__":
    tfds.testing.test_main()
