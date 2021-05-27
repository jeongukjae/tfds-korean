"""sae4k dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
**sae4K: Structured Argument Extraction for Korean**

Label Description

* Questions - [Question-Argument] pairs w/ question type label
    * Yes/no (label 0)
    * Alternative (label 1)
    * Wh- (label 2)
* Commands - [Command-Argument] pairs w/ negativeness label
    * Prohibition (label 3)
    * Requirement (label 4)
    * Strong requirement (label 5)

For more details, see <https://github.com/warnikchow/sae4k>.
"""

_CITATION = """
@article{cho2019machines,
    title={Machines Getting with the Program: Understanding Intent Arguments of Non-Canonical Directives},
    author={Cho, Won Ik and Moon, Young Ki and Moon, Sangwhan and Kim, Seok Min and Kim, Nam Soo},
    journal={arXiv preprint arXiv:1912.00342},
    year={2019}
}
"""

_LICENSE = """
[This work is licensed under a CC-BY-SA-4.0 License.](https://github.com/warnikchow/sae4k/blob/master/LICENSE)
"""

VERSION = tfds.core.Version("1.0.0")


class Sae4kConfig(tfds.core.BuilderConfig):
    def __init__(self, *, augmented=True, **kwargs):
        super(Sae4kConfig, self).__init__(version=VERSION, **kwargs)
        self.augmented = augmented


class Sae4k(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    BUILDER_CONFIGS = [
        Sae4kConfig(
            name="original",
            augmented=False,
            description="Original Corpus",
        ),
        Sae4kConfig(
            name="augmented",
            augmented=True,
            description="Augmented Corpus",
        ),
    ]

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "question": tfds.features.Text(),
                    "command": tfds.features.Text(),
                    "label": tfds.features.ClassLabel(num_classes=6),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/warnikchow/sae4k",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        filename_map = {
            False: "sae4k_v1.txt",
            True: "sae4k_v2.txt",  # augmented
        }
        path = dl_manager.download_and_extract(
            f"https://raw.githubusercontent.com/warnikchow/sae4k/a3a7a4510ea010d210956ad50e38a61c7c838b0f/data/{filename_map[self.builder_config.augmented]}"
        )

        return {
            "train": self._generate_examples(path),
        }

    def _generate_examples(self, path):
        with path.open() as f:
            for index, line in enumerate(f):
                splits = line.split("\t")
                assert len(splits) == 3

                if self.builder_config.augmented:
                    yield f"augmented-sae4k-{index}", {
                        "question": splits[1],
                        "command": splits[2],
                        "label": int(splits[0]),
                    }
                else:
                    yield f"original-sae4k-{index}", {
                        "question": splits[0],
                        "command": splits[1],
                        "label": int(splits[2]),
                    }
