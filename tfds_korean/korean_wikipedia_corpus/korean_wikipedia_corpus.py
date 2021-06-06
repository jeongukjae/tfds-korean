"""korean_wikipedia_corpus dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
한국어 위키백과 말뭉치.

[kss](https://github.com/hyunwoongko/kss)를 사용하여 문장 단위로 분절되어 있는 위키백과 말뭉치입니다.
"""

_CITATION = """
@misc{korean_wikipedia_corpus21
    title={Korean Wikipedia Corpus},
    author={Ukjae Jeong},
    howpublished={https://github.com/jeongukjae/korean-wikipedia-corpus},
    year={2021}
}
"""

_LICESNSE = """
This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).
"""


class KoreanWikipediaCorpus(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for korean_wikipedia_corpus dataset."""

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
                    "content": tfds.features.Sequence(tfds.features.Text()),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/jeongukjae/korean-wikipedia-corpus",
            citation=_CITATION,
            redistribution_info={"license": _LICESNSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        path = dl_manager.download_and_extract(
            "https://github.com/jeongukjae/korean-wikipedia-corpus/releases/download/20210606/corpus.zip"
        )

        return {"train": self._generate_examples(path / "text-preprocessed")}

    def _generate_examples(self, path):
        """Yields examples."""
        for docs_file in path.glob("*/wiki_*"):
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
