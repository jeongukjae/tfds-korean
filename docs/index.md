---
layout: default
title: Dataset Catalog
---

# tfds-korean(`0.1.0`) Catalog

A collection of Korean Text Datasets ready to use using [Tensorflow-Datasets](https://github.com/tensorflow/datasets).

[TensorFlow-Datasets](https://github.com/tensorflow/datasets)를 이용한 한국어/한글 데이터셋 모음입니다.

[**Dataset Catalog**](https://jeongukjae.github.io/tfds-korean) \| [**pypi**](https://pypi.org/project/tfds-korean/)

![PyPI - License](https://img.shields.io/pypi/l/tfds-korean)
![PyPI](https://img.shields.io/pypi/v/tfds-korean)
[![Test Python](https://github.com/jeongukjae/tfds-korean/actions/workflows/test-python.yml/badge.svg)](https://github.com/jeongukjae/tfds-korean/actions/workflows/test-python.yml)

## Usage

* Install using pip: `pip install tfds-korean`
* Download and prepare dataset using tensorflow-datasets

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.nsmc

  for example in tfds.load("nsmc"):
      ...
  ```

* For more details, see [tfds docs(https://www.tensorflow.org/datasets)](https://www.tensorflow.org/datasets).

### Examples

* [Loading NSMC dataset](https://github.com/jeongukjae/tfds-korean/blob/main/examples/nsmc_loading_datasets.ipynb)
* [Training a classifier using Korean hate speech dataset](https://github.com/jeongukjae/tfds-korean/blob/main/examples/korean_hate_speech_lstm.ipynb)

## All datasets

* [kmounlp_ner](./datasets/kmounlp_ner.html)
* [korean_chatbot_qa_data](./datasets/korean_chatbot_qa_data.html)
* [korean_hate_speech](./datasets/korean_hate_speech.html)
* [korean_parallel_corpora](./datasets/korean_parallel_corpora.html)
* [kornli](./datasets/kornli.html)
* [korsts](./datasets/korsts.html)
* [kowikitext](./datasets/kowikitext.html)
* [namuwikitext](./datasets/namuwikitext.html)
* [nlp_challenge](./datasets/nlp_challenge.html)
* [nsmc](./datasets/nsmc.html)
* [para_kqc](./datasets/para_kqc.html)
* [question_pair](./datasets/question_pair.html)


## Licenses

The license for this repository and licenses for datasets are applied separately. It is recommended to use each dataset after checking the dataset's website.

본 레포지토리의 라이선스와 데이터셋의 라이선스는 별도로 적용됩니다. 데이터셋을 사용하기 전 각 데이터셋의 라이선스와 웹 사이트를 확인 후 사용하시길 권해드리며, 본 라이브러리는 데이터셋을 호스팅하거나 배포하지 않는 점을 참고부탁드립니다.
