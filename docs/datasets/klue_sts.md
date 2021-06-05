---
layout: default
title: klue_sts
---

# klue_sts
{: .no_toc }

KLUE benchmark - Semantic Textual Similarity(STS) task.

For more details, see [KLUE Benchmark - STS Task - Overview description](https://klue-benchmark.com/tasks/67/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_sts/klue_sts.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `10.22 MiB`
* Dataset size: `3.63 MiB`
* Features:

  ```python
  FeaturesDict({
      'binary-label': tf.int32,
      'guid': Text(shape=(), dtype=tf.string),
      'label': tf.float32,
      'real-label': tf.float32,
      'sentence1': Text(shape=(), dtype=tf.string),
      'sentence2': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |11668|
  |dev  |519|

* Examples:

  | |guid|sentence1|sentence2|label|real-label|binary-label|
  |---|---|---|---|---|---|---|
  |1|klue-sts-v1_train_04646|그 외에 숙소 근처 장소도 좋았습니다.|게다가, 숙소 근처도 좋았습니다.|3.7000|3.6667|1|
  |2|klue-sts-v1_train_00137|거실하고 안방 불 켜져 있는지 확인해봐|외출시에는 집안모드말고 방범모드를 꼭 확인하도록 협조 바랍니다.|0.4000|0.4000|0|
  |3|klue-sts-v1_train_05440|이 집의 가장 큰 장점은 고흐뮤지엄과 국립미술관에서 아주 가깝다는 것이고요,|이 집의 가장 큰 장점은 고흐 박물관과 국립 미술 박물관과 매우 가깝다는 것입니다.|4.3000|4.3333|1|
  |4|klue-sts-v1_train_04631|느낀적이 없는데 이 숙소는 정말 완벽합니다.|조금 통제적인게 있기는하나 걱정할 정도는 아니니 이 숙소는 추천할만 합니다.|1.3000|1.2857|0|
  |5|klue-sts-v1_train_06490|국회 증액은 코로나 피해 맞춤형 지원, 백신물량 확보, 2050 탄소중립을 위한 선제...|이밖에 2050 탄소중립 달성을 위한 기반 조성 예산 3000억원과 보육·돌봄 지원 ...|1.7000|1.6667|0|
  |6|klue-sts-v1_train_03613|올해부터 체납액이 2억원 이상인 고액·상습 체납자는 최대 30일간 유치장 등에 감치할...|오는 29일부터 코로나19 피해로 대출 상환이 어려운 개인 채무자는 최대 1년까지 가...|0.1000|0.1429|0|
  |7|klue-sts-v1_train_04524|그 친구 결혼기념일이 언제인지 말해 보게.|언제가 그 친구분 결혼기념일입니까?|3.8000|3.8333|1|
  |8|klue-sts-v1_train_04297|하지만 이정도는 모든 슉소가 다들 있다고 생각됩니다.|이 모든 것을 뷰랑 위치가 다 커버해줍니다.|0.1000|0.1429|0|
  |9|klue-sts-v1_train_05698|근처 공원언덕 올라가서 일몰 보는 것도 정말 멋집니다.|또한 근처 공원에서 야경을 보면 정말 예쁩니다.|2.4000|2.4286|0|
  |10|klue-sts-v1_train_10458|하루 일정을 여유롭게 잡으시길 권합니다.|하루 일정을 쉽게 잡으시길 권합니다.|3.6000|3.5714|1|

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
  import tfds_korean.klue_sts

  dataset = tfds.load("klue_sts")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/67/overview/copyright).

<style> td {white-space: nowrap;} </style>
