"""klue_re dataset."""
import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Relation Extraction(RE) task.

For more details, see [KLUE Benchmark - RE Task - Overview description](https://klue-benchmark.com/tasks/70/overview/description)
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
See also [Copyright notice](https://klue-benchmark.com/tasks/70/overview/copyright).
"""


class KlueRe(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for klue_re dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "guid": tfds.features.Text(),
                    "sentence": tfds.features.Text(),
                    "subject_entity": tfds.features.FeaturesDict(
                        {
                            "word": tfds.features.Text(),
                            "start_idx": tfds.features.Tensor(shape=[], dtype=tf.int64),
                            "end_idx": tfds.features.Tensor(shape=[], dtype=tf.int64),
                            "type": tfds.features.Text(),
                        }
                    ),
                    "object_entity": tfds.features.FeaturesDict(
                        {
                            "word": tfds.features.Text(),
                            "start_idx": tfds.features.Tensor(shape=[], dtype=tf.int64),
                            "end_idx": tfds.features.Tensor(shape=[], dtype=tf.int64),
                            "type": tfds.features.Text(),
                        }
                    ),
                    "label": tfds.features.Text(),
                    "source": tfds.features.Text(),
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
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-re-v1/klue-re-v1_train.json",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-re-v1/klue-re-v1_dev.json",
                "relation_list": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-re-v1/relation_list.json",
            }
        )

        with files["relation_list"].open() as f:
            relations = json.load(f)["relations"]

        return {
            "train": self._generate_examples(files["train"], relations=relations),
            "dev": self._generate_examples(files["dev"], relations=relations),
        }

    def _generate_examples(self, path, relations):
        with path.open() as f:
            for obj in json.load(f):
                assert obj["label"] in relations
                yield obj["guid"], obj
