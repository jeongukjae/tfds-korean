"""para_kqc dataset."""

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
Parallel dataset of Korean Questions and Commands

paper: https://www.aclweb.org/anthology/2020.lrec-1.842/

* feature description
    * topic. 0: Email, 1: Scheduling, 2: S. Home, 3: Weather
    * act. 0: Alt. Q, 1. Wh- Q, 2: PH, 3: Str. REQ
"""

_CITATION = """
@inproceedings{cho2020discourse,
    title={Discourse Component to Sentence (DC2S): An Efficient Human-Aided Construction of Paraphrase and Sentence Similarity Dataset},
    author={Cho, Won Ik and Kim, Jong In and Moon, Young Ki and Kim, Nam Soo},
    booktitle={Proceedings of The 12th Language Resources and Evaluation Conference},
    pages={6819--6826},
    year={2020}
}
"""


class ParaKqc(tfds.core.GeneratorBasedBuilder):
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
                    "text": tfds.features.Tensor(dtype=tf.string, shape=[10]),
                    "topic": tfds.features.ClassLabel(names=["0", "1", "2", "3"]),
                    "act": tfds.features.ClassLabel(names=["0", "1", "2", "3"]),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/warnikchow/paraKQC",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        train_split = dl_manager.download(
            "https://raw.githubusercontent.com/warnikchow/paraKQC/c16270fe6c2e888af07e7cb043248ad31d8a6f9c/data/paraKQC_v1.txt"
        )

        return {
            "train": self._generate_examples(train_split),
        }

    def _generate_examples(self, split_path):
        with split_path.open() as f:
            lines = f.read().strip().split("\n")
            assert len(lines) % 10 == 0, "Malformed dataset"

            lines = [line.strip().split("\t") for line in lines]
            assert all([len(line) == 3 for line in lines]), "Malformed dataset"

            for i in range(len(lines) // 10):
                example = lines[i * 10 : i * 10 + 10]
                text = [i[2] for i in example]
                topic = example[0][0]
                act = example[0][0]

                yield i, {
                    "text": text,
                    "topic": topic,
                    "act": act,
                }
