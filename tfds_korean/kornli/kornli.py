"""kornli dataset."""
import tensorflow_datasets as tfds

_DESCRIPTION = """
The dataset for the paper [_KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding_](https://arxiv.org/abs/2004.03289).
"""

_CITATION = """
@article{ham2020kornli,
    title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
    author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
    journal={arXiv preprint arXiv:2004.03289},
    year={2020}
}
"""


class Kornli(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for kornli dataset."""

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
                    "sentence1": tfds.features.Text(),
                    "sentence2": tfds.features.Text(),
                    "gold_label": tfds.features.ClassLabel(names=["neutral", "contradiction", "entailment"]),
                }
            ),
            supervised_keys=None,  # TODO ((sentence1, sentence2), gold_label)
            homepage="https://github.com/kakaobrain/KorNLUDatasets",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download(
            {
                "mnli_train": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorNLI/multinli.train.ko.tsv",
                "snli_train": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorNLI/snli_1.0_train.ko.tsv",
                "xnli_dev": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorNLI/xnli.dev.ko.tsv",
                "xnli_test": "https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/0df0fe7d496eb61b092e022e238c2230b29f1cbc/KorNLI/xnli.test.ko.tsv",
            }
        )

        return {
            "mnli_train": self._generate_examples(splits["mnli_train"], prefix="mnli_train"),
            "snli_train": self._generate_examples(splits["snli_train"], prefix="snli_train"),
            "xnli_dev": self._generate_examples(splits["xnli_dev"], prefix="xnli_dev"),
            "xnli_test": self._generate_examples(splits["xnli_test"], prefix="xnli_test"),
        }

    def _generate_examples(self, split_file, prefix):
        with split_file.open() as f:
            next(f)
            for index, line in enumerate(f):
                line = line.strip().split("\t")
                # 0: sentence1, 1: sentence2, 2: gold_label
                yield f"{prefix}-{index}", {
                    "sentence1": line[0],
                    "sentence2": line[1],
                    "gold_label": line[2],
                }
