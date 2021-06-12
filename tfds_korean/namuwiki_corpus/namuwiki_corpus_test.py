"""namuwiki_corpus dataset."""

import tensorflow_datasets as tfds

from . import namuwiki_corpus


class NamuwikiCorpusTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for namuwiki_corpus dataset."""

    DATASET_CLASS = namuwiki_corpus.NamuwikiCorpus
    SPLITS = {"train": 3}


if __name__ == "__main__":
    tfds.testing.test_main()
