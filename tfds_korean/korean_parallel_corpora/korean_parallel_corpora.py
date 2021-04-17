"""korean_parallel_corpora dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
Korean Parallel corpora (of https://sites.google.com/site/koreanparalleldata/)

Jungyeul Park, Jeen-Pyo Hong and Jeong-Won Cha (2016) Korean Language Resources for Everyone. In Proceedings of the 30th Pacific Asia Conference on Language, Information and Computation (PACLIC 30). October 28 - 30, 2016. Seoul, Korea. https://www.aclweb.org/anthology/Y16-2002/
"""

# TODO(korean_parallel_corpora): BibTeX citation
_CITATION = """
@inproceedings{park-etal-2017-building,
    title = "Building a Better Bitext for Structurally Different Languages through Self-training",
    author = {Park, Jungyeul  and
      Dugast, Lo{\\"\\i}c  and
      Hong, Jeen-Pyo  and
      Shin, Chang-Uk  and
      Cha, Jeong-Won},
    booktitle = "Proceedings of the First Workshop on Curation and Applications of Parallel and Comparable Corpora",
    month = nov,
    year = "2017",
    address = "Taipei, Taiwan",
    publisher = "Asian Federation of Natural Language Processing",
    url = "https://www.aclweb.org/anthology/W17-5601",
    pages = "1--10",
    abstract = "We propose a novel method to bootstrap the construction of parallel corpora for new pairs of structurally different languages. We do so by combining the use of a pivot language and self-training. A pivot language enables the use of existing translation models to bootstrap the alignment and a self-training procedure enables to achieve better alignment, both at the document and sentence level. We also propose several evaluation methods for the resulting alignment.",
}
"""

VERSION = tfds.core.Version("1.0.0")

# TODO JHE-pos-tagged
NEWS_NAME = "news-v1"
JHE_NAME = "jhe-v1"
FRENCH_JIM_NAME = "french-jim-v1"
NORTH_KOREAN_NEWS_NAME = "northkorean-news-v1"
BIBLE_NAME = "bible"


class KoreanParallelCorporaConfig(tfds.core.BuilderConfig):
    def __init__(self, **kwargs):
        super(KoreanParallelCorporaConfig, self).__init__(version=VERSION, **kwargs)


class KoreanParallelCorpora(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for korean_parallel_corpora dataset."""

    VERSION = VERSION
    BUILDER_CONFIGS = [
        # TODO(korean_parallel_corpora): Add description for each config
        KoreanParallelCorporaConfig(name=NEWS_NAME),
        KoreanParallelCorporaConfig(name=JHE_NAME),
        KoreanParallelCorporaConfig(name=FRENCH_JIM_NAME),
        KoreanParallelCorporaConfig(name=NORTH_KOREAN_NEWS_NAME),
        KoreanParallelCorporaConfig(name=BIBLE_NAME),
    ]

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""

        if self.builder_config.name == FRENCH_JIM_NAME:
            feature_dict = {
                "ko": tfds.features.Text(),
                "fr": tfds.features.Text(),
            }
        elif self.builder_config.name == NORTH_KOREAN_NEWS_NAME:
            feature_dict = {
                "nk": tfds.features.Text(),
                "en": tfds.features.Text(),
            }
        else:
            feature_dict = {
                "ko": tfds.features.Text(),
                "en": tfds.features.Text(),
            }

        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(feature_dict),
            supervised_keys=None,
            homepage="https://github.com/jungyeul/korean-parallel-corpora",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        if self.builder_config.name == NEWS_NAME:
            splits = dl_manager.download_and_extract(
                {
                    "train": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-news-v1/korean-english-park.train.tar.gz",
                    "dev": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-news-v1/korean-english-park.dev.tar.gz",
                    "test": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-news-v1/korean-english-park.test.tar.gz",
                }
            )

            return {
                "train": self._generate_examples(
                    splits["train"] / "korean-english-park.train.ko",
                    splits["train"] / "korean-english-park.train.en",
                    src_name="ko",
                    tgt_name="en",
                ),
                "dev": self._generate_examples(
                    splits["dev"] / "korean-english-park.dev.ko",
                    splits["dev"] / "korean-english-park.dev.en",
                    src_name="ko",
                    tgt_name="en",
                ),
                "test": self._generate_examples(
                    splits["test"] / "korean-english-park.test.ko",
                    splits["test"] / "korean-english-park.test.en",
                    src_name="ko",
                    tgt_name="en",
                ),
            }

        if self.builder_config.name == JHE_NAME:
            splits = dl_manager.download(
                {
                    "dev.ko": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-jhe/jhe-koen-dev.ko",
                    "dev.en": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-jhe/jhe-koen-dev.en",
                    "eval.ko": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-jhe/jhe-koen-eval.en",
                    "eval.en": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-english-jhe/jhe-koen-eval.en",
                }
            )

            return {
                "dev": self._generate_examples(splits["dev.ko"], splits["dev.en"], src_name="ko", tgt_name="en"),
                "eval": self._generate_examples(splits["eval.ko"], splits["eval.en"], src_name="ko", tgt_name="en"),
            }

        if self.builder_config.name == FRENCH_JIM_NAME:
            splits = dl_manager.download_and_extract(
                {
                    "train": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-french-jim-v1/korean-french-park-v1.train.tar.gz",
                    "test": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/korean-french-jim-v1/korean-french-park-v1.test.tar.gz",
                }
            )

            return {
                "train": self._generate_examples(
                    splits["train"] / "korean-french-park-v1.train.ko",
                    splits["train"] / "korean-french-park-v1.train.fr",
                    src_name="ko",
                    tgt_name="fr",
                ),
                "test": self._generate_examples(
                    splits["test"] / "korean-french-park-v1.test.ko",
                    splits["test"] / "korean-french-park-v1.test.fr",
                    src_name="ko",
                    tgt_name="fr",
                ),
            }

        if self.builder_config.name == NORTH_KOREAN_NEWS_NAME:
            splits = dl_manager.download(
                {
                    "dev.nk": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/northkorean-english-news-v1/northkorean-english.dev.nk",
                    "dev.en": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/northkorean-english-news-v1/northkorean-english.dev.en",
                    "test.nk": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/northkorean-english-news-v1/northkorean-english.test.nk",
                    "test.en": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/northkorean-english-news-v1/northkorean-english.test.en",
                }
            )

            return {
                "dev": self._generate_examples(splits["dev.nk"], splits["dev.en"], src_name="nk", tgt_name="en"),
                "test": self._generate_examples(splits["test.nk"], splits["test.en"], src_name="nk", tgt_name="en"),
            }

        if self.builder_config.name == BIBLE_NAME:
            splits = dl_manager.download(
                {
                    "train.ko": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/bible/bible-all.kr.txt",
                    "train.en": "https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/07883d4cae4e309dfde8c48c5f37ebea0b59574e/bible/bible-all.en.txt",
                }
            )

            return {"train": self._generate_examples(splits["train.ko"], splits["train.en"], src_name="ko", tgt_name="en")}

    def _generate_examples(self, src_path, tgt_path, src_name, tgt_name):
        with src_path.open() as src_file, tgt_path.open() as tgt_file:
            for index, (src_line, tgt_line) in enumerate(zip(src_file, tgt_file)):
                yield f"{self.builder_config.name}-line-{index}", {
                    src_name: src_line.strip(),
                    tgt_name: tgt_line.strip(),
                }
