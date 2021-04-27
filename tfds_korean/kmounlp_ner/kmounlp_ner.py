"""kmounlp_ner dataset."""

import os

import tensorflow as tf
import tensorflow_datasets as tfds

_DESCRIPTION = """
한국어 개체명 정의 및 표지 표준화 기술보고서와 이를 기반으로 제작된 개체명 형태소 말뭉치.

자세한 정보는 <https://github.com/kmounlp/NER/blob/master/NER%20Guideline%20(ver%201.0).pdf>를 참고하세요.
라이선스는 <https://github.com/kmounlp/NER/blob/master/LICENSE>에서 확인하실 수 있습니다.
"""

_CITATION = """
@misc{kmounlpner19
    title={Kmounlp NER},
    author={Min-Ah Cheon and Jae-Hoon Kim},
    howpublished={https://github.com/kmounlp/NER},
    year={2019}
}
"""

_LICENSE = """
```
NER License

DO NOT use this dataset for commercial use.
MIT License for non-commercial use.

---------------------------------------------------------------------------------

MIT License

Copyright (c) 2019 한국해양대학교 자연언어처리연구실

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
"""


class KmounlpNer(tfds.core.GeneratorBasedBuilder):
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
                    "text": tfds.features.Text(),
                    "recognized": tfds.features.Text(),
                    "tokens": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "lemma": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "pos": tfds.features.Tensor(shape=[None], dtype=tf.string),
                    "named_entity": tfds.features.Tensor(shape=[None], dtype=tf.string),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/kmounlp/NER",
            citation=_CITATION,
            redistribution_info={"license": _LICENSE},
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        # ls | sort > filelist.txt
        # 위 명령어로 filelist.txt 생성 후 넣어줌
        with tf.io.gfile.GFile(os.path.join(os.path.dirname(__file__), "filelist.txt")) as f:
            files = f.readlines()
        train_files = dl_manager.download(
            [
                f"https://raw.githubusercontent.com/kmounlp/NER/1e557de738b8e6215c7cacac116e735518c0f680/말뭉치%20-%20형태소_개체명/{filename.strip()}"
                for filename in files
            ]
        )

        return {"train": self._generate_examples(train_files)}

    def _generate_examples(self, train_files):
        for train_file in train_files:
            with train_file.open() as f:
                for example in f.read().split("\n\n"):
                    example = example.strip()
                    if example == "":
                        continue

                    example = example.split("\n")
                    id_ = example[0][2:].strip()  # remove prefix "## "
                    id_ = f"{os.path.basename(train_file)}-{id_}"
                    text = example[1][2:].strip()  # remove prefix "## "
                    recognized = example[2][2:].strip()  # remove prefix "## "

                    details = [line.split("\t") for line in example[3:]]
                    tokens = [i[0] for i in details]
                    lemma = [i[1] for i in details]
                    pos = [i[2] for i in details]
                    named_entity = [i[3] for i in details]

                    yield id_, {
                        "text": text,
                        "recognized": recognized,
                        "tokens": tokens,
                        "lemma": lemma,
                        "pos": pos,
                        "named_entity": named_entity,
                    }
