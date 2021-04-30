"""sci_news_sum_kr50 dataset."""

import tensorflow_datasets as tfds

from . import sci_news_sum_kr50


class SciNewsSumKr50Test(tfds.testing.DatasetBuilderTestCase):
    DATASET_CLASS = sci_news_sum_kr50.SciNewsSumKr50
    SPLITS = {"dev": 1}
    DL_EXTRACT_RESULT = ["1.json"]


if __name__ == "__main__":
    tfds.testing.test_main()
