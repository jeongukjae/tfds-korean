"""para_kqc dataset."""

import tensorflow_datasets as tfds

from . import para_kqc


class ParaKqcTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for para_kqc dataset."""

    DATASET_CLASS = para_kqc.ParaKqc
    SPLITS = {"train": 2}

    DL_EXTRACT_RESULT = "paraKQC_v1.txt"


if __name__ == "__main__":
    tfds.testing.test_main()
