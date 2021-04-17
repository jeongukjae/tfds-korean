"""korean_parallel_corpora dataset."""

import tensorflow_datasets as tfds

from . import korean_parallel_corpora
from .korean_parallel_corpora import BIBLE_NAME, FRENCH_JIM_NAME, JHE_NAME, NEWS_NAME, NORTH_KOREAN_NEWS_NAME


class KoreanParallelCorporaNewsTest(tfds.testing.DatasetBuilderTestCase):
    BUILDER_CONFIG_NAMES_TO_TEST = [NEWS_NAME]
    DATASET_CLASS = korean_parallel_corpora.KoreanParallelCorpora
    SPLITS = {"train": 3, "dev": 1, "test": 1}

    DL_EXTRACT_RESULT = {
        "train": "korean-english-park.train",
        "dev": "korean-english-park.dev",
        "test": "korean-english-park.test",
    }


class KoreanParallelCorporaNKNewsTest(tfds.testing.DatasetBuilderTestCase):
    BUILDER_CONFIG_NAMES_TO_TEST = [NORTH_KOREAN_NEWS_NAME]
    DATASET_CLASS = korean_parallel_corpora.KoreanParallelCorpora
    SPLITS = {"dev": 1, "test": 1}

    DL_EXTRACT_RESULT = {
        "dev.nk": "northkorean-english.dev.nk",
        "dev.en": "northkorean-english.dev.en",
        "test.nk": "northkorean-english.test.nk",
        "test.en": "northkorean-english.test.en",
    }


class KoreanParallelCorporaFrJimTest(tfds.testing.DatasetBuilderTestCase):
    BUILDER_CONFIG_NAMES_TO_TEST = [FRENCH_JIM_NAME]
    DATASET_CLASS = korean_parallel_corpora.KoreanParallelCorpora
    SPLITS = {"train": 1, "test": 1}

    DL_EXTRACT_RESULT = {
        "train": "korean-french-park-v1.train",
        "test": "korean-french-park-v1.test",
    }


class KoreanParallelCorporaJheTest(tfds.testing.DatasetBuilderTestCase):
    BUILDER_CONFIG_NAMES_TO_TEST = [JHE_NAME]
    DATASET_CLASS = korean_parallel_corpora.KoreanParallelCorpora
    SPLITS = {"dev": 3, "eval": 1}

    DL_EXTRACT_RESULT = {
        "dev.en": "jhe-koen-dev.en",
        "dev.ko": "jhe-koen-dev.ko",
        "eval.en": "jhe-koen-eval.en",
        "eval.ko": "jhe-koen-eval.ko",
    }


class KoreanParallelCorporaBibleTest(tfds.testing.DatasetBuilderTestCase):
    BUILDER_CONFIG_NAMES_TO_TEST = [BIBLE_NAME]
    DATASET_CLASS = korean_parallel_corpora.KoreanParallelCorpora
    SPLITS = {"train": 3}

    DL_EXTRACT_RESULT = {"train.ko": "bible-all.kr.txt", "train.en": "bible-all.en.txt"}


if __name__ == "__main__":
    tfds.testing.test_main()
