---
layout: default
title: klue_nli
---

# klue_nli
{: .no_toc }

KLUE benchmark - Natural Language Inference(NLI) task.

For more details, see [KLUE Benchmark - NLI Task - Overview description](https://klue-benchmark.com/tasks/68/overview/description)

* label order: `["entailment", "contradiction", "neutral"]`

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_nli/klue_nli.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `13.42 MiB`
* Dataset size: `7.33 MiB`
* Features:

  ```python
  FeaturesDict({
      'gold_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
      'guid': Text(shape=(), dtype=tf.string),
      'hypothesis': Text(shape=(), dtype=tf.string),
      'premise': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |24998|
  |dev  |3000|

* Examples:

  | |guid|premise|hypothesis|gold_label|
  |---|---|---|---|---|
  |1|klue-nli-v1_train_01497|개인 주차공간이 있어 굉장히 편리합니다.|개인 주차공간이 있습니다.|0|
  |2|klue-nli-v1_train_23345|한가지 단점은 와이파이가 좀 불안정하네요.|단점은 와이파이가 좀 불안정한 것 뿐이네요.|0|
  |3|klue-nli-v1_train_21179|청년층 또는 취업취약계층을 우선적으로 선발하고 직무교육을 통해 인공지능 디지털 역량과...|청년층 또는 취업취약계층을 먼저 선발하여 직무교육을 시행한다.|0|
  |4|klue-nli-v1_train_18496|전기제품을 쓸때 신경써야할 부분 입니다.|전기제품을 사용할 때 신경써야하는 부분입니다.|0|
  |5|klue-nli-v1_train_22887|프랭크는 베트남전의 혼란한 상황을 틈타 직접 태국과 베트남을 오가며 마약 밀수를 시작...|프랭크는 마약 판매로 부와 명예를 쌓는다.|0|
  |6|klue-nli-v1_train_17150|이에 따라, 도쿄에서 아키타를 거쳐 아오모리까지 운행하는 아케보노는 2014년 3월 ...|아케보노는 2016년에 은퇴한다.|1|
  |7|klue-nli-v1_train_05519|다음부터 작가가 누군지 꼭 확인하고 시청해야지|계속 작가를 모른 채 시청해야지.|1|
  |8|klue-nli-v1_train_20411|직원들이 지방 사업장을 오갈 때 인터넷에서 신청하면 사용할 수 있는 헬기라는 것이다.|지방 사업장은 거리가 멀기 때문에 직원에게 경비를 지급한다.|2|
  |9|klue-nli-v1_train_12486|아즈마는 신입 기쿠치를 데리고 사건 수사를 시작하고, 용의자를 차고 때리는 폭력 행위...|아즈마가 파헤친 범행은 극악무도한 살인 사건이었다.|2|
  |10|klue-nli-v1_train_20707|집에 처음 찾아갈때 약간 헷갈릴 수 있습니다.|처음 집을 찾아가면 약간 헷갈릴 수 있습니다.|0|

* Citation:

  ```text
  @misc{park2021klue,
      title={KLUE: Korean Language Understanding Evaluation},
      author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
      year={2021},
      eprint={2105.09680},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
  }
  ```

## How to use this dataset

* Installation:

  ```sh
  pip install tfds-korean
  ```

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.klue_nli

  dataset = tfds.load("klue_nli")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/68/overview/copyright).

<style> td {white-space: nowrap;} </style>
