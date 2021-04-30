"""petitions_archive dataset."""

import tensorflow_datasets as tfds

from . import petitions_archive


class PetitionsArchiveTest(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = petitions_archive.PetitionsArchive
    SPLITS = {"train": 2}
    DL_EXTRACT_RESULT = ["1.jsonl"]


if __name__ == "__main__":
    tfds.testing.test_main()
