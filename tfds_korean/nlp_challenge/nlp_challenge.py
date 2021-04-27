"""nlp_challenge dataset."""
import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
네이버, 창원대가 함께하는 NLP Challenge 기술 대회의 NER/SRL 데이터.

자세한 정보는 <https://air.changwon.ac.kr/?page_id=14>와 <https://air.changwon.ac.kr/?page_id=10>를 참고하세요.
"""

_CITATION = """
@misc{Naver2018,
  author = {Naver},
  title = {NLP Challenge},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\\url{https://github.com/naver/nlp-challenge}},
  commit = {a51654472e0da75cd37c6e73ffe583db78e68323}
}
"""

_LICENSE = """
> 제공되는 코퍼스는 Data.ly에서 제작한 것으로, 연구 및 리더보드를 위한 학습으로 사용 가능하며 상업적인 목적으로 사용될 수 없음을 알려드립니다. 추가문의가 필요한 경우 메일을 남겨주세요.
"""

VERSION = tfds.core.Version("1.0.0")


class NlpChallengeConfig(tfds.core.BuilderConfig):
    def __init__(self, **kwargs):
        super(NlpChallengeConfig, self).__init__(version=VERSION, **kwargs)


class NlpChallenge(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }
    BUILDER_CONFIGS = [
        NlpChallengeConfig(
            name="ner",
            description="NLP Challenge NER dataset",
        ),
        NlpChallengeConfig(
            name="srl",
            description="NLP Challenge SRL dataset",
        ),
    ]

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "tokens": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "tags": tfds.features.Tensor(shape=[None], dtype=tf.string),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/naver/nlp-challenge",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        url = f"https://raw.githubusercontent.com/naver/nlp-challenge/a51654472e0da75cd37c6e73ffe583db78e68323/missions/{self.builder_config.name}/data/train/train_data"
        train_file = dl_manager.download(url)

        return {
            "train": self._generate_examples(train_file),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            tokens = []
            tags = []
            for index, line in enumerate(f):
                line = line.strip()

                if line == "" and len(tokens) > 0:
                    yield f"train-{index}", {
                        "tokens": tokens,
                        "tags": tags,
                    }
                    tokens = []
                    tags = []
                    continue

                _, token, tag = line.split("\t")
                tokens.append(token)
                tags.append(tag)

            if len(tokens) > 0:
                yield f"train-{index}", {
                    "tokens": tokens,
                    "tags": tags,
                }
