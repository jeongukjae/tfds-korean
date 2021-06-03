"""klue_nli dataset."""
import json

import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Natural Language Inference(NLI) task.

For more details, see [KLUE Benchmark - NLI Task - Overview description](https://klue-benchmark.com/tasks/68/overview/description)

* label order: `["entailment", "contradiction", "neutral"]`
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
See also [Copyright notice](https://klue-benchmark.com/tasks/68/overview/copyright).
"""


class KlueNli(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for klue_nli dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "guid": tfds.features.Text(),
                    "premise": tfds.features.Text(),
                    "hypothesis": tfds.features.Text(),
                    "gold_label": tfds.features.ClassLabel(names=["entailment", "contradiction", "neutral"]),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/KLUE-benchmark/KLUE",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download(
            {
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-nli-v1/klue-nli-v1_train.json",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-nli-v1/klue-nli-v1_dev.json",
            }
        )

        return {
            "train": self._generate_examples(splits["train"]),
            "dev": self._generate_examples(splits["dev"]),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for example in json.load(f):
                yield example["guid"], {
                    "guid": example["guid"],
                    "premise": example["premise"],
                    "hypothesis": example["hypothesis"],
                    "gold_label": example["gold_label"],
                }
