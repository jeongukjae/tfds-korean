import tensorflow_datasets as tfds

from . import nlp_challenge


class NlpChallengeTest(tfds.testing.DatasetBuilderTestCase):
    # NER, SRL 데이터셋 형식이 같아서 동일한 테스트 코드로 테스트한다.
    DATASET_CLASS = nlp_challenge.NlpChallenge
    SPLITS = {"train": 3}

    DL_EXTRACT_RESULT = "train_data"


if __name__ == "__main__":
    tfds.testing.test_main()
