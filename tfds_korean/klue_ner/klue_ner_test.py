"""klue_ner dataset."""

import tensorflow_datasets as tfds

from . import klue_ner


class KlueNerTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = klue_ner.KlueNer
    SPLITS = {"train": 3, "dev": 1}

    DL_EXTRACT_RESULT = {"train": "train.txt", "dev": "dev.txt"}


if __name__ == "__main__":
    tfds.testing.test_main()
