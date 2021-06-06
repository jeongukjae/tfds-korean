"""korean_wikipedia_corpus dataset."""

import tensorflow_datasets as tfds

from . import korean_wikipedia_corpus


class KoreanWikipediaCorpusTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for korean_wikipedia_corpus dataset."""

    DATASET_CLASS = korean_wikipedia_corpus.KoreanWikipediaCorpus
    SPLITS = {"train": 3}

    # If you are calling `download/download_and_extract` with a dict, like:
    #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
    # then the tests needs to provide the fake output paths relative to the
    # fake data directory
    # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
    tfds.testing.test_main()
