---
layout: default
title: question_pair
---

# question_pair
{: .no_toc }

짝 지어진 두 개의 질문이 같은 질문인지 다른 질문인지 핸드 레이블을 달아둔 데이터.
사랑, 이별, 또는 일상과 같은 주제로 도메인 특정적이지 않음.

라이선스는 <https://github.com/songys/Question_pair/blob/master/LICENSE>에서 확인하실 수 있습니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/question_pair/question_pair.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/songys/Question_pair>
* Download size: `532.46 KiB`
* Dataset size: `972.14 KiB`
* Features:

  ```python
  FeaturesDict({
      'is_duplicate': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
      'question1': Text(shape=(), dtype=tf.string),
      'question2': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |6136|
  |test  |758|
  |validation  |682|

* Examples:

  | |is_duplicate|question1|question2|
  |---|---|---|---|
  |1|1|짝남한테 문자 왔는데 뭐라고 답하지|짝남이랑 어색해졌어 괜히 너무 나댔나|
  |2|0|발렌타인데이 선물 줄 사람이 없어|발렌타인데이인데 줄 사람이 없어|
  |3|1|와 진짜 너무 짜증나네|완전히 잊는다는게 쉽지 않네|
  |4|0|방에 먼지가 한가득|먼지가 쌓였네|
  |5|1|대기업 인턴하고 싶다.|인턴하고 대기업 입사면 좋겠다.|
  |6|1|정말 복합적으로 힘드네|정말 아직 너무 사랑합니다 잡고 싶습니다|
  |7|1|이별을 하고.|이별의 마무리|
  |8|0|예랑이가 대리효도시키는 건 아니겠지?|예랑이가 대리효도시키는 건 아니겠지?|
  |9|0|혼수 얼마나들까?|혼수 얼마야?|
  |10|0|뭐 보고 결혼 결심해?|보통 뭐 보고 결혼 결심해?|

* Citation:

  ```text
  @misc{questionpair20
      title={Paired Question},
      author={Youngsook Song},
      howpublished={https://github.com/songys/Question_pair},
      year={2020}
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
  import tfds_korean.question_pair

  dataset = tfds.load("question_pair")
  ```

## License

The MIT License (MIT)

<style> td {white-space: nowrap;} </style>
