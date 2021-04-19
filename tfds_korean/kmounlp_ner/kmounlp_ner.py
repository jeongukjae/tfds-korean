"""kmounlp_ner dataset."""

import os

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
한국어 개체명 정의 및 표지 표준화 기술보고서와 이를 기반으로 제작된 개체명 형태소 말뭉치
"""

# TODO(kmounlp_ner): BibTeX citation
_CITATION = """
"""


class KmounlpNer(tfds.core.GeneratorBasedBuilder):
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
                    "text": tfds.features.Text(),
                    "recognized": tfds.features.Text(),
                    "tokens": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "lemma": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "pos": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "named_entity": tfds.features.Tensor(shape=[None], dtype=tf.string),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/kmounlp/NER",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        # ls | sort > filelist.txt
        # 위 명령어로 filelist.txt 생성 후 넣어줌
        with tf.io.gfile.GFile(os.path.join(os.path.dirname(__file__), "filelist.txt")) as f:
            files = f.readlines()
        train_files = dl_manager.download(
            [f"https://raw.githubusercontent.com/kmounlp/NER/master/말뭉치%20-%20형태소_개체명/{filename.strip()}" for filename in files]
        )

        return {"train": self._generate_examples(train_files)}

    def _generate_examples(self, train_files):
        for train_file in train_files:
            with train_file.open() as f:
                for example in f.read().split("\n\n"):
                    example = example.strip()
                    if example == "":
                        continue

                    example = example.split("\n")
                    id_ = example[0][2:].strip()  # remove prefix "## "
                    id_ = f"{os.path.basename(train_file)}-{id_}"
                    text = example[1][2:].strip()  # remove prefix "## "
                    recognized = example[2][2:].strip()  # remove prefix "## "

                    details = [line.split("\t") for line in example[3:]]
                    tokens = [i[0] for i in details]
                    lemma = [i[1] for i in details]
                    pos = [i[2] for i in details]
                    named_entity = [i[3] for i in details]

                    yield id_, {
                        "text": text,
                        "recognized": recognized,
                        "tokens": tokens,
                        "lemma": lemma,
                        "pos": pos,
                        "named_entity": named_entity,
                    }
