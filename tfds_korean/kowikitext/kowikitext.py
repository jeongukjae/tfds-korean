"""kowikitext dataset."""

from typing import List

import tensorflow_datasets as tfds

_DESCRIPTION = """
Wikitext format Korean corpus

한국어 위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
"""

_CITATION = """
@misc{kowikitext20
    title={Ko-wikitext},
    author={Hyunjoong Kim},
    howpublished={https://github.com/lovit/kowikitext},
    year={2020}
}
"""

_LICENSE = """
[CC-BY-SA 3.0](https://www.creativecommons.org/licenses/by-sa/3.0/) which [kowiki](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EC%A0%80%EC%9E%91%EA%B6%8C) dump dataset is licensed
"""


class Kowikitext(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for kowikitext dataset."""

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
                    "title": tfds.features.Text(),
                    "content": tfds.features.Text(),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/lovit/kowikitext",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download_and_extract(
            {
                "train": "https://github.com/lovit/kowikitext/releases/download/20200920.v3/kowikitext_20200920.train.zip",
                "dev": "https://github.com/lovit/kowikitext/releases/download/20200920.v3/kowikitext_20200920.dev.zip",
                "test": "https://github.com/lovit/kowikitext/releases/download/20200920.v3/kowikitext_20200920.test.zip",
            }
        )

        return {
            "train": self._generate_examples(splits["train"] / "kowikitext_20200920.train", "train"),
            "dev": self._generate_examples(splits["dev"] / "kowikitext_20200920.dev", "dev"),
            "test": self._generate_examples(splits["test"] / "kowikitext_20200920.test", "test"),
        }

    def _generate_examples(self, path, split_name):
        def _get_feature(text: List[str]):
            title = text[0].strip()
            content = "\n".join(text[1:]).strip()
            return {
                "title": title,
                "content": content,
            }

        with path.open() as f:
            text = []
            index = 0
            for line in f:
                stripped = line.strip()

                if stripped.startswith("= ") and stripped.endswith(" ="):
                    # Split docs on a heading line
                    # See https://github.com/jeongukjae/tfds-korean/issues/12
                    if len(text) != 0:
                        yield f"namu-{split_name}-{index}", _get_feature(text)
                        index += 1

                    text = [stripped]
                    continue

                text.append(stripped)

            if len(text) > 0:
                yield f"namu-{split_name}-{index}", _get_feature(text)
