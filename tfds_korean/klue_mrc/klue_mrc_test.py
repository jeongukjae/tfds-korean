"""klue_ner dataset."""

import tensorflow_datasets as tfds

from . import klue_mrc


class KlueMrcTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = klue_mrc.KlueMrc
    SPLITS = {"train": 3, "dev": 1}

    DL_EXTRACT_RESULT = {"train": "train.json", "dev": "dev.json"}


if __name__ == "__main__":
    tfds.testing.test_main()
