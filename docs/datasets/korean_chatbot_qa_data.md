---
layout: default
title: korean_chatbot_qa_data
---

# korean_chatbot_qa_data
{: .no_toc }

Chatbot_data_for_Korean v1.0

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/korean_chatbot_qa_data/korean_chatbot_qa_data.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/songys/Chatbot_data>
* Download size: `868.99 KiB`
* Dataset size: `1.25 MiB`
* Features:

  ```python
  FeaturesDict({
      'A': Text(shape=(), dtype=tf.string),
      'Q': Text(shape=(), dtype=tf.string),
      'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |11823|

* Examples:

  | |A|Q|label|
  |---|---|---|---|
  |1|짝사랑이 그런가봐요.|짝사랑 중인데 나혼자 영화찍어.|2|
  |2|제습기를 돌려보세요.|날씨가 너무 눅눅해|0|
  |3|기념일이 있나봐요.|문득 달력을 보니|1|
  |4|지금처럼 참지 말고 표현하세요.|정말 힘드네|1|
  |5|이젠 기억을 접어두세요.|여자친구와 이별한지 정확히 1년이 되는 날이네|1|
  |6|더 떨렸겠어요.|먼저 인사하려고 했는데 짝남이 먼저 인사해줬어.|2|
  |7|적게 먹고 많이 움직이세요.|살이 안빠져|0|
  |8|또 다른 친구를 사귈 수 있을 거예요.|친구가 없어|0|
  |9|쉽지 않은 결정이었나봐요.|한순간에, 무너진 느낌이었습니다|1|
  |10|환승은 진짜 예의가 없네요.|군인입니다 환승이별.|1|

* Citation:

  ```text
  
  ```

## How to use this dataset

* Installation:

  ```sh
  pip install tfds-korean
  ```

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.korean_chatbot_qa_data

  dataset = tfds.load("korean_chatbot_qa_data")
  ```
