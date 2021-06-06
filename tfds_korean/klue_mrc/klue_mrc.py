"""klue_mrc dataset."""
import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Machine Reading Comprehension (MRC) task.

or more details, see [KLUE Benchmark - MRC Task - Overview description](https://klue-benchmark.com/tasks/72/overview/description)
"""

_CITATION = """
@misc{park2021klue,
    title={KLUE: Korean Language Understanding Evaluation},
    author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
    year={2021},
    eprint={2105.09680},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

_LICENSE = """
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/72/overview/copyright).
"""


class KlueMrc(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "guid": tfds.features.Text(),
                    "title": tfds.features.Text(),
                    "news_category": tfds.features.Text(),
                    "source": tfds.features.Text(),
                    "context": tfds.features.Text(),
                    "question": tfds.features.Text(),
                    "question_type": tfds.features.Tensor(shape=[], dtype=tf.int64),
                    "answers": tfds.features.Sequence(
                        {
                            "text": tfds.features.Text(),
                            "answer_start": tfds.features.Tensor(shape=[], dtype=tf.int64),
                        }
                    ),
                    "is_impossible": tfds.features.Tensor(shape=[], dtype=tf.bool),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/KLUE-benchmark/KLUE",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        files = dl_manager.download_and_extract(
            {
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-mrc-v1/klue-mrc-v1_train.json",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-mrc-v1/klue-mrc-v1_dev.json",
            }
        )

        return {
            "train": self._generate_examples(files["train"]),
            "dev": self._generate_examples(files["dev"]),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for document in json.load(f)["data"]:
                title, source = document["title"], document["source"]
                news_category = document["news_category"] if document["news_category"] is not None else ""
                for paragraph in document["paragraphs"]:
                    context = paragraph["context"]
                    for qa in paragraph["qas"]:
                        guid, question, question_type, is_impossible = qa["guid"], qa["question"], qa["question_type"], qa["is_impossible"]
                        answers = qa["answers" if question_type in [1, 2] else "plausible_answers"]

                        yield guid, {
                            "guid": guid,
                            "title": title,
                            "news_category": news_category,
                            "source": source,
                            "context": context,
                            "question": question,
                            "question_type": question_type,
                            "answers": answers,
                            "is_impossible": is_impossible,
                        }
