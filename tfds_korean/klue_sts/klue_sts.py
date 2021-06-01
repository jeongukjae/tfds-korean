"""klue_sts dataset."""
import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Semantic Textual Similarity(STS) task.

For more details, see [KLUE Benchmark - STS Task - Overview description](https://klue-benchmark.com/tasks/67/overview/description)
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
See also [Copyright notice](https://klue-benchmark.com/tasks/67/overview/copyright).
"""


class KlueSts(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for klue_sts dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "guid": tfds.features.Text(),
                    "sentence1": tfds.features.Text(),
                    "sentence2": tfds.features.Text(),
                    "label": tfds.features.Tensor(shape=[], dtype=tf.float32),
                    "real-label": tfds.features.Tensor(shape=[], dtype=tf.float32),
                    "binary-label": tfds.features.Tensor(shape=[], dtype=tf.int32),
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
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-sts-v1/klue-sts-v1_train.json",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-sts-v1/klue-sts-v1_dev.json",
            }
        )

        return {
            "train": self._generate_examples(files["train"]),
            "dev": self._generate_examples(files["dev"]),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for obj in json.load(f):
                yield obj["guid"], {
                    "guid": obj["guid"],
                    "sentence1": obj["sentence1"],
                    "sentence2": obj["sentence2"],
                    "label": obj["labels"]["label"],
                    "real-label": obj["labels"]["real-label"],
                    "binary-label": obj["labels"]["binary-label"],
                }
