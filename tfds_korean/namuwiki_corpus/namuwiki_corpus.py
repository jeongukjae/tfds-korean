"""namuwiki_corpus dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
나무위키 말뭉치.

[kss](https://github.com/hyunwoongko/kss)를 사용하여 문장 단위로 분절되어 있는 나무위키 말뭉치입니다.
"""


_CITATION = """
@misc{namuwiki_corpus21
    title={Namuwiki Corpus},
    author={Ukjae Jeong},
    howpublished={https://github.com/jeongukjae/namuwiki-corpus},
    year={2021}
}
"""

_LICESNSE = """
This work is licensed under a [CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/).
"""


class NamuwikiCorpus(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for namuwiki_corpus dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {"1.0.0": "Initial release."}

    def _info(self) -> tfds.core.DatasetInfo:
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "title": tfds.features.Text(),
                    "content": tfds.features.Sequence(tfds.features.Text()),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/jeongukjae/namuwiki-corpus",
            citation=_CITATION,
            redistribution_info={"license": _LICESNSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        path = dl_manager.download_and_extract("https://github.com/jeongukjae/namuwiki-corpus/releases/download/210301-210612/corpus.zip")

        return {"train": self._generate_examples(path / "corpus")}

    def _generate_examples(self, path):
        for docs_file in path.glob("namu_*"):
            with docs_file.open() as f:
                title = ""
                content = []

                for index, line in enumerate(f):
                    line = line.strip()

                    if line == "":
                        if title != "":
                            yield f"{str(f)}-{index}-{title}", {
                                "title": title,
                                "content": content,
                            }
                        title = ""
                        content = []
                        continue

                    if title == "":
                        title = line
                        continue

                    content.append(line)

                if title != "":
                    yield f"{str(f)}-{index}-{title}", {
                        "title": title,
                        "content": content,
                    }
