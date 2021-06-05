"""klue_re dataset."""

import tensorflow_datasets as tfds

from . import klue_re


class KlueReTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for klue_re dataset."""

    DATASET_CLASS = klue_re.KlueRe
    SPLITS = {"train": 1, "dev": 1}
    DL_EXTRACT_RESULT = {
        "train": "train.json",
        "dev": "dev.json",
        "relation_list": "relation_list.json",
    }


if __name__ == "__main__":
    tfds.testing.test_main()
