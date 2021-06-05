---
layout: default
title: korean_chatbot_qa_data
---

# korean_chatbot_qa_data
{: .no_toc }

Chatbot_data_for_Korean v1.0

인공데이터입니다.일부 이별과 관련된 질문에서 다음카페 "[사랑보다 아름다운 실연](http://cafe116.daum.net/_c21_/home?grpid=1bld)"에서 자주 나오는 이야기들을 참고하여 제작하였습니다.
가령 "이별한 지 열흘(또는 100일) 되었어요"라는 질문에 챗봇이 위로한다는 취지로 답변을 작성하였습니다.

챗봇 트레이닝용 문답 페어 11,876개
일상다반서 0, 이별(부정) 1, 사랑(긍정) 2로 레이블링

자세한 정보는 <https://github.com/songys/Chatbot_data>를 참고하세요.
라이선스는 <https://github.com/songys/Chatbot_data/blob/master/LICENSE>에서 확인하실 수 있습니다.

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

  | |Q|A|label|
  |---|---|---|---|
  |1|짝사랑 중인데 나혼자 영화찍어.|짝사랑이 그런가봐요.|2|
  |2|날씨가 너무 눅눅해|제습기를 돌려보세요.|0|
  |3|문득 달력을 보니|기념일이 있나봐요.|1|
  |4|정말 힘드네|지금처럼 참지 말고 표현하세요.|1|
  |5|여자친구와 이별한지 정확히 1년이 되는 날이네|이젠 기억을 접어두세요.|1|
  |6|먼저 인사하려고 했는데 짝남이 먼저 인사해줬어.|더 떨렸겠어요.|2|
  |7|살이 안빠져|적게 먹고 많이 움직이세요.|0|
  |8|친구가 없어|또 다른 친구를 사귈 수 있을 거예요.|0|
  |9|한순간에, 무너진 느낌이었습니다|쉽지 않은 결정이었나봐요.|1|
  |10|군인입니다 환승이별.|환승은 진짜 예의가 없네요.|1|

* Citation:

  ```text
  @misc{koreanchatbotqa18
      title={Chatbot data for Korean},
      author={Youngsook Song},
      howpublished={https://github.com/songys/Chatbot_data},
      year={2018}
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
  import tfds_korean.korean_chatbot_qa_data

  dataset = tfds.load("korean_chatbot_qa_data")
  ```

## License

MIT License

<style> td {white-space: nowrap;} </style>
