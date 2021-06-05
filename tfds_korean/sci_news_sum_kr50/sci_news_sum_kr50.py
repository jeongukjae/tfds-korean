"""sci_news_sum_kr50 dataset."""
import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
네이버 뉴스 중 IT/과학 분야에서 50개를 선정해서 요약에 해당하는 문장을 태깅해둔 데이터셋입니다.
파일 한개당 뉴스 하나를 뜻하며, 원본 출처가 기록되어 있습니다. 비상업적인 실험에만 사용해주세요.

summaries가 sentences 중 요약에 해당하는 문장의 index입니다. 이걸 정답셋으로 사용하시면 됩니다.

자세한 정보는 <https://github.com/theeluwin/sci-news-sum-kr-50>를 참고하세요.
라이선스는 <https://github.com/theeluwin/sci-news-sum-kr-50/blob/master/LICENSE>에서 확인하실 수 있습니다.
"""

_CITATION = """
@misc{scinewssumkr16
    title={sci-news-sum-kr-50},
    author={Jamie J. Seol},
    howpublished={https://github.com/theeluwin/sci-news-sum-kr-50},
    year={2016}
}
"""

_LICENSE = """
MIT License
"""


class SciNewsSumKr50(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "title": tfds.features.Text(),
                    "summaries": tfds.features.Tensor(shape=[None], dtype=tf.int32),
                    "sentences": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "source": tfds.features.Text(),
                    "slug": tfds.features.Text(),
                    "length": tfds.features.Tensor(shape=[], dtype=tf.int32),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/theeluwin/sci-news-sum-kr-50",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        files = dl_manager.download(
            [
                f"https://raw.githubusercontent.com/theeluwin/sci-news-sum-kr-50/aca0583651503c1cdfa8ef0bc2ef0976250a33ca/data/{index:02d}.json"
                for index in range(1, 51)
            ]
        )

        return {
            "dev": self._generate_examples(files),
        }

    def _generate_examples(self, files):
        index = 0
        for file_handler in files:
            with file_handler.open() as f:
                yield f"news-sum-{index}", json.load(f)
                index += 1
