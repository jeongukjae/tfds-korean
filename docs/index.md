---
layout: default
title: Dataset Catalog
---

# tfds-korean(`0.1.0`) Catalog

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
