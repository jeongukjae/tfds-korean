"""korean_hate_speech dataset."""

import csv
import itertools
from typing import Dict, Iterator, Tuple

import tensorflow_datasets as tfds

_DESCRIPTION = """
The human-annotated Korean corpus for toxic speech detection and the large unlabeled corpus.
The data is comments from the Korean entertainment news aggregation platform.
"""

_CITATION = """
@inproceedings{moon-etal-2020-beep,
    title = "{BEEP}! {K}orean Corpus of Online News Comments for Toxic Speech Detection",
    author = "Moon, Jihyung  and
      Cho, Won Ik  and
      Lee, Junbum",
    booktitle = "Proceedings of the Eighth International Workshop on Natural Language Processing for Social Media",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.socialnlp-1.4",
    pages = "25--31",
    abstract = "Toxic comments in online platforms are an unavoidable social issue under the cloak of anonymity. Hate speech detection has been actively done for languages such as English, German, or Italian, where manually labeled corpus has been released. In this work, we first present 9.4K manually labeled entertainment news comments for identifying Korean toxic speech, collected from a widely used online news platform in Korea. The comments are annotated regarding social bias and hate speech since both aspects are correlated. The inter-annotator agreement Krippendorff{'}s alpha score is 0.492 and 0.496, respectively. We provide benchmarks using CharCNN, BiLSTM, and BERT, where BERT achieves the highest score on all tasks. The models generally display better performance on bias identification, since the hate speech detection is a more subjective issue. Additionally, when BERT is trained with bias label for hate speech detection, the prediction score increases, implying that bias and hate are intertwined. We make our dataset publicly available and open competitions with the corpus and benchmarks.",
}
"""

VERSION = tfds.core.Version("1.0.0")


class KoreanHateSpeechConfig(tfds.core.BuilderConfig):
    def __init__(self, *, labeled=True, **kwargs):
        super(KoreanHateSpeechConfig, self).__init__(version=VERSION, **kwargs)
        self.labeled = labeled


class KoreanHateSpeech(tfds.core.GeneratorBasedBuilder):
    VERSION = VERSION
    BUILDER_CONFIGS = [
        KoreanHateSpeechConfig(
            name="labeled",
            labeled=True,
            description="Korean hate speech dataset (labeled)",
        ),
        KoreanHateSpeechConfig(
            name="unlabeled",
            labeled=False,
            description="Korean hate speech dataset (unlabeled)",
        ),
    ]

    def _info(self) -> tfds.core.DatasetInfo:
        feature_dict = {
            "news_title": tfds.features.Text(),
            "comments": tfds.features.Text(),
        }
        if self.builder_config.labeled:
            feature_dict.update(
                {
                    "contain_gender_bias": tfds.features.ClassLabel(names=["False", "True"]),
                    "bias": tfds.features.ClassLabel(names=["none", "gender", "others"]),
                    "hate": tfds.features.ClassLabel(names=["none", "hate", "offensive"]),
                }
            )

        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(feature_dict),
            supervised_keys=None,
            homepage="https://github.com/kocohub/korean-hate-speech",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        if not self.builder_config.labeled:
            num_shard = 5
            files_to_download = {}
            for i in range(num_shard):
                files_to_download.update(
                    {
                        f"{i}": f"https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/unlabeled/unlabeled_comments_{i + 1}.txt",
                        f"{i}_title": f"https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/news_title/unlabeled_comments.news_title_{i + 1}.txt",
                    }
                )

            downloaded_files = dl_manager.download(files_to_download)
            return {
                "train": itertools.chain(
                    *[self._generate_examples(downloaded_files[f"{i}"], downloaded_files[f"{i}_title"], str(i)) for i in range(num_shard)]
                )
            }

        downloaded_files = dl_manager.download(
            {
                "train": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/labeled/train.tsv",
                "train_title": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/news_title/train.news_title.txt",
                "dev": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/labeled/dev.tsv",
                "dev_title": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/news_title/dev.news_title.txt",
                "dev": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/labeled/dev.tsv",
                "dev_title": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/news_title/dev.news_title.txt",
                "test": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/test.no_label.tsv",
                "test_title": "https://raw.githubusercontent.com/kocohub/korean-hate-speech/f8d05dce2b22007bb149e5139c0060c68ad8f94b/news_title/test.news_title.txt",
            }
        )

        return {
            "train": self._generate_examples(downloaded_files["train"], downloaded_files["train_title"], "train", with_label=True),
            "dev": self._generate_examples(downloaded_files["dev"], downloaded_files["dev_title"], "dev", with_label=True),
            "test": self._generate_examples(downloaded_files["test"], downloaded_files["test_title"], "test"),
        }

    def _generate_examples(self, comment_file_path, title_file_path, split_name, with_label=False) -> Iterator[Tuple[str, Dict]]:
        if not self.builder_config.labeled:
            # unlabeled
            with comment_file_path.open() as comment_file, title_file_path.open() as title_file:
                for index, (comment_row, title_row) in enumerate(zip(comment_file, csv.reader(title_file))):
                    yield f"{split_name}-{index}", {
                        "news_title": title_row[0],
                        "comments": comment_row.strip(),
                    }

        else:
            # labeled
            with comment_file_path.open() as comment_file, title_file_path.open() as title_file:
                for index, (comment_row, title_row) in enumerate(zip(csv.DictReader(comment_file, delimiter="\t"), csv.reader(title_file))):
                    if with_label:
                        yield f"{split_name}-{index}", {
                            "news_title": title_row[0],
                            "comments": comment_row["comments"],
                            "contain_gender_bias": comment_row["contain_gender_bias"],
                            "bias": comment_row["bias"],
                            "hate": comment_row["hate"],
                        }
                    else:
                        yield f"{split_name}-{index}", {
                            "news_title": title_row[0],
                            "comments": comment_row["comments"],
                            "contain_gender_bias": False,
                            "bias": "none",
                            "hate": "none",
                        }
