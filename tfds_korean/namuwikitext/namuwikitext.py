"""namuwikitext dataset."""
from typing import List

import tensorflow_datasets as tfds

_DESCRIPTION = """
Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.
"""

# TODO(namuwikitext): BibTeX citation
_CITATION = """
"""


class Namuwikitext(tfds.core.GeneratorBasedBuilder):
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
            homepage="https://github.com/lovit/namuwikitext",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        splits = dl_manager.download_and_extract(
            {
                "train": "https://github.com/lovit/namuwikitext/releases/download/v0.3/namuwikitext_20200302.train.zip",
                "dev": "https://github.com/lovit/namuwikitext/releases/download/v0.3/namuwikitext_20200302.dev.zip",
                "test": "https://github.com/lovit/namuwikitext/releases/download/v0.3/namuwikitext_20200302.test.zip",
            }
        )

        return {
            "train": self._generate_examples(splits["train"] / "namuwikitext_20200302.train", "train"),
            "dev": self._generate_examples(splits["dev"] / "namuwikitext_20200302.dev", "dev"),
            "test": self._generate_examples(splits["test"] / "namuwikitext_20200302.test", "test"),
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
                    # See https://github.com/jeongukjae/tfds-korean/issues/12#issuecomment-826358469
                    if len(text) != 0:
                        yield f"namu-{split_name}-{index}", _get_feature(text)
                        index += 1

                    text = [stripped]
                    continue

                text.append(stripped)

            if len(text) > 0:
                yield f"namu-{split_name}-{index}", _get_feature(text)
