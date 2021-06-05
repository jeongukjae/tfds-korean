"""petitions_archive dataset."""

import json

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
청와대 국민청원 데이터 아카이브

청와대 국민청원 게시판의 데이터를 월별로 수집한 데이터입니다.
"""

_CITATION = """
@misc{petitions_archive19
    title={Korean Petitions Archive},
    author={Hyunjoong Kim},
    howpublished={https://github.com/lovit/petitions_archive},
    year={2019}
}
"""

_LICENSE = """
[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)
"""

_FILES = [
    "petitions_2017-08",
    "petitions_2017-09",
    "petitions_2017-10",
    "petitions_2017-11",
    "petitions_2017-12",
    "petitions_2018-01",
    "petitions_2018-02",
    "petitions_2018-03",
    "petitions_2018-04",
    "petitions_2018-05",
    "petitions_2018-06",
    "petitions_2018-07",
    "petitions_2018-08",
    "petitions_2018-09",
    "petitions_2018-10",
    "petitions_2018-11",
    "petitions_2018-12",
    "petitions_2019-01",
    "petitions_2019-02",
    "petitions_2019-03",
    "petitions_2019-04",
    "petitions_2019-05",
    "petitions_2019-06",
    "petitions_2019-07",
    "petitions_2019-08",
]

_FEATURE_KEYS = {"category", "begin", "end", "content", "num_agree", "petition_idx", "status", "title"}


class PetitionsArchive(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "petition_idx": tfds.features.Text(),
                    "title": tfds.features.Text(),
                    "category": tfds.features.Text(),
                    "content": tfds.features.Text(),
                    "begin": tfds.features.Text(),
                    "end": tfds.features.Text(),
                    "status": tfds.features.Text(),
                    "num_agree": tfds.features.Tensor(shape=[], dtype=tf.int32),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/lovit/petitions_archive",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        files = dl_manager.download(
            [
                f"https://raw.githubusercontent.com/lovit/petitions_archive/03dc3f3d69e03a0a4885350c6991e328fc0a6b81/{filename}"
                for filename in _FILES
            ]
        )

        return {"train": self._generate_examples(files)}

    def _generate_examples(self, files):
        index = 0

        for petition_file in files:
            with petition_file.open() as f:
                for line in f:
                    yield f"petition-{index}", {key: value for key, value in json.loads(line).items() if key in _FEATURE_KEYS}
                    index += 1
