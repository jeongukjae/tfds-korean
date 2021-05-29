"""korquad dataset."""

import tensorflow_datasets as tfds

from . import korquad


class Korquad1Test(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = korquad.Korquad
    BUILDER_CONFIG_NAMES_TO_TEST = ["1.0"]
    SPLITS = {"train": 3, "dev": 1}
    DL_EXTRACT_RESULT = {"train": "1.0_train.json", "dev": "1.0_dev.json"}


class Korquad2Test(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = korquad.Korquad
    BUILDER_CONFIG_NAMES_TO_TEST = ["2.1"]
    SPLITS = {"train": 3, "dev": 1}
    DL_EXTRACT_RESULT = {"train": ["2.0_train"], "dev": ["2.0_dev"]}


if __name__ == "__main__":
    tfds.testing.test_main()
