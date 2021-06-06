"""korean_wikipedia_corpus dataset."""

import tensorflow_datasets as tfds

from . import korean_wikipedia_corpus


class KoreanWikipediaCorpusTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for korean_wikipedia_corpus dataset."""

    DATASET_CLASS = korean_wikipedia_corpus.KoreanWikipediaCorpus
    SPLITS = {"train": 3}


if __name__ == "__main__":
    tfds.testing.test_main()
