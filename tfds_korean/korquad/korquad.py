"""korquad dataset."""
import itertools
import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
The Korean Question Answering Dataset
"""

# TODO(korquad): BibTeX citation KorQuAD 2
_CITATION = """
@@misc{lim2019korquad10,
      title={KorQuAD1.0: Korean QA Dataset for Machine Reading Comprehension},
      author={Seungyoung Lim and Myungji Kim and Jooyoul Lee},
      year={2019},
      eprint={1909.07005},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""

_LICENSE = """
* KorQuAD 2.0의 데이터셋은 [CC BY-ND 2.0 KR 라이센스](https://creativecommons.org/licenses/by-nd/2.0/kr/)를 따릅니다.
* KorQuAD 1.0의 데이터셋은 [CC BY-ND 2.0 KR 라이센스](https://creativecommons.org/licenses/by-nd/2.0/kr/)를 따릅니다.
"""


VERSION = tfds.core.Version("1.0.0")


class KorquadConfig(tfds.core.BuilderConfig):
    def __init__(self, *, v, **kwargs):
        super(KorquadConfig, self).__init__(version=VERSION, **kwargs)
        self.v = v


class Korquad(tfds.core.GeneratorBasedBuilder):
    VERSION = VERSION
    BUILDER_CONFIGS = [
        KorquadConfig(
            name="1.0",
            v=1,
            description="""KorQuAD 1.0

KorQuAD 1.0은 한국어 Machine Reading Comprehension을 위해 만든 데이터셋입니다.
모든 질의에 대한 답변은 해당 Wikipedia article 문단의 일부 하위 영역으로 이루어집니다.
Stanford Question Answering Dataset(SQuAD) v1.0과 동일한 방식으로 구성되었습니다.""",
        ),
        KorquadConfig(
            name="2.1",
            v=2,
            description="""KorQuAD 2.1

KorQuAD 2.1은 KorQuAD 1.0에서 질문답변 20,000+ 쌍을 포함하여 총 100,000+ 쌍으로 구성된 한국어 Machine Reading Comprehension 데이터셋 입니다.
KorQuAD 1.0과는 다르게 1~2 문단이 아닌 Wikipedia article 전체에서 답을 찾아야 합니다. 매우 긴 문서들이 있기 때문에 탐색 시간에 대한 고려가 필요할 것 입니다.
또한 표와 리스트도 포함되어 있기 때문에 HTML tag를 통한 문서의 구조 이해도 필요합니다.
이 데이터셋을 통해서 다양한 형태와 길이의 문서들에서도 기계독해가 가능해질 것 입니다.""",
        ),
    ]

    def _info(self) -> tfds.core.DatasetInfo:
        if self.builder_config.v == 1:
            homepage = "https://korquad.github.io/KorQuad%201.0/"
            features = tfds.features.FeaturesDict(
                {
                    "qa_id": tfds.features.Text(),
                    "title": tfds.features.Text(),
                    "context": tfds.features.Text(),
                    "question": tfds.features.Text(),
                    "answers": tfds.features.Sequence(
                        {
                            "text": tfds.features.Text(),
                            "answer_start": tfds.features.Tensor(shape=[], dtype=tf.int64),
                        }
                    ),
                }
            )

        elif self.builder_config.v == 2:
            homepage = "https://korquad.github.io/"
            features = tfds.features.FeaturesDict(
                {
                    "qa_id": tfds.features.Text(),
                    "title": tfds.features.Text(),
                    "url": tfds.features.Text(),
                    "raw_html": tfds.features.Text(),
                    "context": tfds.features.Text(),
                    "question": tfds.features.Text(),
                    "answer": tfds.features.FeaturesDict(
                        {
                            "text": tfds.features.Text(),
                            "answer_start": tfds.features.Tensor(shape=[], dtype=tf.int64),
                            "html_answer_text": tfds.features.Text(),
                            "html_answer_start": tfds.features.Tensor(shape=[], dtype=tf.int64),
                        }
                    ),
                }
            )

        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=homepage,
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        if self.builder_config.v == 1:
            splits = dl_manager.download(
                {
                    "train": "https://raw.githubusercontent.com/korquad/korquad.github.io/918f5229639203d741045fdcdbb7462c602887da/dataset/KorQuAD_v1.0_train.json",
                    "dev": "https://raw.githubusercontent.com/korquad/korquad.github.io/918f5229639203d741045fdcdbb7462c602887da/dataset/KorQuAD_v1.0_dev.json",
                }
            )

            return {
                "train": self._generate_examples(splits["train"]),
                "dev": self._generate_examples(splits["dev"]),
            }

        splits = dl_manager.download_and_extract(
            {
                "train": [
                    f"https://raw.githubusercontent.com/korquad/korquad.github.io/918f5229639203d741045fdcdbb7462c602887da/dataset/KorQuAD_2.1/train/KorQuAD_2.1_train_{i:02}.zip"
                    for i in range(13)
                ],
                "dev": [
                    f"https://raw.githubusercontent.com/korquad/korquad.github.io/918f5229639203d741045fdcdbb7462c602887da/dataset/KorQuAD_2.1/dev/KorQuAD_2.1_dev_{i:02}.zip"
                    for i in range(2)
                ],
            }
        )
        return {
            "train": itertools.chain.from_iterable([self._generate_examples(i) for i in splits["train"]]),
            "dev": itertools.chain.from_iterable([self._generate_examples(i) for i in splits["dev"]]),
        }

    def _generate_examples(self, path):
        if self.builder_config.v == 1:
            with path.open() as f:
                for document in json.load(f)["data"]:
                    title = document["title"]
                    for paragraph in document["paragraphs"]:
                        context = paragraph["context"]
                        for qa in paragraph["qas"]:
                            question = qa["question"]
                            answers = qa["answers"]
                            qa_id = qa["id"]

                            yield qa_id, {"qa_id": qa_id, "title": title, "context": context, "question": question, "answers": answers}
            return

        for json_file in path.glob("*.json"):
            with json_file.open() as f:
                for document in json.load(f)["data"]:
                    title = document["title"]

                    url = document["url"]
                    context = document["context"]
                    raw_html = document["raw_html"]

                    for qa in document["qas"]:
                        question = qa["question"]
                        qa_id = qa["id"]
                        answer = qa["answer"]

                        yield qa_id, {
                            "qa_id": qa_id,
                            "title": title,
                            "context": context,
                            "question": question,
                            "answer": answer,
                            "url": url,
                            "raw_html": raw_html,
                        }
