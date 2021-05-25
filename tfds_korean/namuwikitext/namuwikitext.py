"""namuwikitext dataset."""
from typing import List

import tensorflow_datasets as tfds

_DESCRIPTION = """
Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.

[lovit/namuwikitext#10](https://github.com/lovit/namuwikitext/issues/10)과 같은 이슈로 홈페이지에 적힌 수대로 train, dev, test가 나오지는 않습니다.
또한 `content` 피쳐가 비어있는 값이 나올 가능성이 있으니 주의하여 사용하시길 바랍니다.
"""

_CITATION = """
@misc{namuwikitext20
    title={Namuwikitext},
    author={Hyunjoong Kim},
    howpublished={https://github.com/lovit/namuwikitext},
    year={2020}
}
"""

_LICENSE = """
["CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/") which [Namuwiki dump dataset](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84) is licensed
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
            redistribution_info={"license": _LICENSE},
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
