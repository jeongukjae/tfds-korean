"""kmounlp_ner dataset."""

import tensorflow_datasets as tfds

from . import kmounlp_ner


class KmounlpNerTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = kmounlp_ner.KmounlpNer
    SPLITS = {"train": 1}

    DL_EXTRACT_RESULT = ["test1.txt"]


if __name__ == "__main__":
    tfds.testing.test_main()
