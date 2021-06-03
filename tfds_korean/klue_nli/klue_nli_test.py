"""klue_nli dataset."""

import tensorflow_datasets as tfds

from . import klue_nli


class KlueNliTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = klue_nli.KlueNli
    SPLITS = {"train": 3, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "train.json", "dev": "dev.json"}


if __name__ == "__main__":
    tfds.testing.test_main()
