"""korean_chatbot_qa_data dataset."""
import csv

import tensorflow_datasets as tfds

_DESCRIPTION = """
Chatbot_data_for_Korean v1.0

인공데이터입니다.일부 이별과 관련된 질문에서 다음카페 "[사랑보다 아름다운 실연](http://cafe116.daum.net/_c21_/home?grpid=1bld)"에서 자주 나오는 이야기들을 참고하여 제작하였습니다.
가령 "이별한 지 열흘(또는 100일) 되었어요"라는 질문에 챗봇이 위로한다는 취지로 답변을 작성하였습니다.

챗봇 트레이닝용 문답 페어 11,876개
일상다반서 0, 이별(부정) 1, 사랑(긍정) 2로 레이블링

자세한 정보는 <https://github.com/songys/Chatbot_data>를 참고하세요.
라이선스는 <https://github.com/songys/Chatbot_data/blob/master/LICENSE>에서 확인하실 수 있습니다.
"""

_CITATION = """
@misc{koreanchatbotqa18
    title={Chatbot data for Korean},
    author={Youngsook Song},
    howpublished={https://github.com/songys/Chatbot_data},
    year={2018}
}
"""

_LICENSE = """MIT License"""


class KoreanChatbotQaData(tfds.core.GeneratorBasedBuilder):
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
                    "Q": tfds.features.Text(),
                    "A": tfds.features.Text(),
                    "label": tfds.features.ClassLabel(names=["0", "1", "2"]),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/songys/Chatbot_data",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        train_filepath = dl_manager.download(
            "https://raw.githubusercontent.com/songys/Chatbot_data/a22e508811b5040eead0be5a89c27ef3780d4e82/ChatbotData%20.csv"
        )

        return {
            "train": self._generate_examples(train_filepath),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for index, row in enumerate(csv.DictReader(f)):
                yield f"row-{index}", {"Q": row["Q"], "A": row["A"], "label": row["label"].strip()}
