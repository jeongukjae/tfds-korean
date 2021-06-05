"""klue_tc dataset."""
import json

import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Topic Classification(TC a.k.a. YANT, Yonhap News Agency Topic Classification) task.

For more details, see [KLUE Benchmark - TC Task - Overview description](https://klue-benchmark.com/tasks/66/overview/description)
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
See also [Copyright notice](https://klue-benchmark.com/tasks/66/overview/copyright).
"""


class KlueTc(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for klue_tc dataset."""

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
                    "predefined_news_category": tfds.features.Text(),
                    "label": tfds.features.Text(),
                    "url": tfds.features.Text(),
                    "date": tfds.features.Text(),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/KLUE-benchmark/KLUE",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        splits = dl_manager.download_and_extract(
            {
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/ynat-v1/ynat-v1_train.json",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/ynat-v1/ynat-v1_dev.json",
            }
        )

        return {
            "train": self._generate_examples(splits["train"]),
            "dev": self._generate_examples(splits["dev"]),
        }

    def _generate_examples(self, path):
        """Yields examples."""
        with path.open() as f:
            for obj in json.load(f):
                yield obj["guid"], {
                    "guid": obj["guid"],
                    "title": obj["title"],
                    "predefined_news_category": obj["predefined_news_category"],
                    "label": obj["label"],
                    "url": obj["url"],
                    "date": obj["date"],
                }
