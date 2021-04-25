---
layout: default
title: Dataset Catalog
---

# tfds-korean(`0.0.1a4`) Catalog

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

## All datasets

* [kmounlp_ner](./datasets/kmounlp_ner.html)
* [korean_chatbot_qa_data](./datasets/korean_chatbot_qa_data.html)
* [korean_hate_speech](./datasets/korean_hate_speech.html)
* [korean_parallel_corpora](./datasets/korean_parallel_corpora.html)
* [kornli](./datasets/kornli.html)
* [korsts](./datasets/korsts.html)
* [nlp_challenge](./datasets/nlp_challenge.html)
* [nsmc](./datasets/nsmc.html)
* [para_kqc](./datasets/para_kqc.html)
* [question_pair](./datasets/question_pair.html)


## Licenses

The license for this repository and licenses for datasets are applied separately. It is recommended to use each dataset after checking the dataset's website.
