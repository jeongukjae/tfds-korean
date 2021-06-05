"""klue_dp dataset."""
import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
KLUE benchmark - Dependency Parsing(DP) task.

For more details, see [KLUE Benchmark - DP Task - Overview description](https://klue-benchmark.com/tasks/71/overview/description)
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
See also [Copyright notice](https://klue-benchmark.com/tasks/71/overview/copyright).
"""


class KlueDp(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for klue_dp dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:

        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "word_form": tfds.features.Sequence(tfds.features.Text()),
                    "lemma": tfds.features.Sequence(tfds.features.Text()),
                    "pos": tfds.features.Sequence(tfds.features.Text()),
                    "head": tfds.features.Sequence(tfds.features.Tensor(shape=[], dtype=tf.int64)),
                    "dependency_relation": tfds.features.Sequence(tfds.features.Text()),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/KLUE-benchmark/KLUE",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download_and_extract(
            {
                "train": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-dp-v1/klue-dp-v1_train.tsv",
                "dev": "https://raw.githubusercontent.com/KLUE-benchmark/KLUE/ab22cd5cfdd6b527a9a4e2d177f9dacb85ddde2c/klue_benchmark/klue-dp-v1/klue-dp-v1_dev.tsv",
            }
        )

        return {
            "train": self._generate_examples(splits["train"]),
            "dev": self._generate_examples(splits["dev"]),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            example_name = None
            word_form, lemma, pos, head, dependency_relation = [], [], [], [], []

            for line in f:
                line = line.rstrip()

                if line == "":
                    assert word_form and lemma and pos and head and dependency_relation and example_name
                    yield example_name, {
                        "word_form": word_form,
                        "lemma": lemma,
                        "pos": pos,
                        "head": head,
                        "dependency_relation": dependency_relation,
                    }

                    example_name = None
                    word_form, lemma, pos, head, dependency_relation = [], [], [], [], []
                    continue

                if line.startswith("##"):
                    if not line.startswith("## klue-dp"):  # example name
                        continue

                    example_name = line[2:].split("\t")[0].strip()
                    continue

                # INDEX, WORD_FORM, LEMMA, POS, HEAD, DEPREL
                splits = line.split("\t")

                word_form.append(splits[1])
                lemma.append(splits[2])
                pos.append(splits[3])
                head.append(int(splits[4]))
                dependency_relation.append(splits[5])

            if example_name is not None:
                yield example_name, {
                    "word_form": word_form,
                    "lemma": lemma,
                    "pos": pos,
                    "head": head,
                    "dependency_relation": dependency_relation,
                }
