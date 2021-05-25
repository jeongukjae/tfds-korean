"""sae4k dataset."""

import tensorflow_datasets as tfds

from . import sae4k


class Sae4kTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = sae4k.Sae4k
    BUILDER_CONFIG_NAMES_TO_TEST = ["original"]
    SPLITS = {"train": 3}
    DL_EXTRACT_RESULT = "original.txt"


class Sae4kAugmentedTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = sae4k.Sae4k
    BUILDER_CONFIG_NAMES_TO_TEST = ["augmented"]
    SPLITS = {"train": 3}
    DL_EXTRACT_RESULT = "augmented.txt"


if __name__ == "__main__":
    tfds.testing.test_main()
