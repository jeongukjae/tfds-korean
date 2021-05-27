---
layout: default
title: sae4k
---

# sae4k
{: .no_toc }

**sae4K: Structured Argument Extraction for Korean**

Label Description

* Questions - [Question-Argument] pairs w/ question type label
    * Yes/no (label 0)
    * Alternative (label 1)
    * Wh- (label 2)
* Commands - [Command-Argument] pairs w/ negativeness label
    * Prohibition (label 3)
    * Requirement (label 4)
    * Strong requirement (label 5)

For more details, see <https://github.com/warnikchow/sae4k>.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/sae4k/sae4k.py)
* Version:
* Homepage: <https://github.com/warnikchow/sae4k>
* Citation:

  ```text
  @article{cho2019machines,
      title={Machines Getting with the Program: Understanding Intent Arguments of Non-Canonical Directives},
      author={Cho, Won Ik and Moon, Young Ki and Moon, Sangwhan and Kim, Seok Min and Kim, Nam Soo},
      journal={arXiv preprint arXiv:1912.00342},
      year={2019}
  }
  ```

## Configs


### sae4k/original (default)

Original Corpus

* Dataset size: `3.85 MiB`
* Download size: `2.43 MiB`
* Features:

  ```python
  FeaturesDict({
      'command': Text(shape=(), dtype=tf.string),
      'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
      'question': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |30837|

* Examples:

  | |command|label|question|
  |---|---|---|---|
  |1|장마철에 음식 조심하기|4|장마철에는 특히 음식 조심해야 돼요|
  |2|눈치봐서 일하기|4|눈치 봐서 일하자 불똥 튄다|
  |3|휴지통에 메일 있는지|0|휴지통에 메일이 있니|
  |4|오늘 메일 왔는지|0|오늘 온 메일 있니|
  |5|내일 오후 서울날씨|2|내일 오후 서울날씨 검색해줘|
  |6|선풍기 전원 켜져있는지|0|선풍기 전원 켜져있는지 확인해줘|
  |7|시험시간표|2|시험시간표를 확인해서 알려줄 수 있니|
  |8|일출시간 구름 여부|0|일출시간 때 구름 끼니|
  |9|둘째 담임 선생님 방문일|2|둘째 담임 선생님 방문일이 언제야|
  |10|교무실로 가기|4|선생님이 교무실로 오라던데|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.sae4k
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("sae4k/original")
  ```


### sae4k/augmented 

Augmented Corpus

* Dataset size: `6.94 MiB`
* Download size: `4.54 MiB`
* Features:

  ```python
  FeaturesDict({
      'command': Text(shape=(), dtype=tf.string),
      'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
      'question': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |50837|

* Examples:

  | |command|label|question|
  |---|---|---|---|
  |1|지난주에 보낸메일 모두 삭제하기|4|지난주에 보낸메일 모두 삭제해줄수있니|
  |2|전기 검침일|2|전기 검침일이 언제지|
  |3|일본 도메인으로 메일 보낼 때 발신지 중국으로 하기|5|일본 도메인으로 메일을 보낼 땐 발신지를 미국보다는 중국으로 하는 것이 좋습니다|
  |4|뮤지컬 보러 오기|5|연극은 볼만한 게 없던데 뮤지컬을 보러 올래|
  |5|이번 달 받은 학회 메일 모두 지우기|5|다른 중요한 메일보다는 이번 달에 받은 학회메일을 지워줘|
  |6|자외선 지수|2|자외선 지수가 어떤지 체크해줄래|
  |7|칠월 이십칠일에 누나 생일 표시하기|4|칠월 이십칠일에 누나 생일 표시해줄래|
  |8|화장실 불 켜져있는지|0|화장실 불 켜져 있는지 확인해|
  |9|나한테쓴 메일 다 지워졌는지|0|나한테쓴 메일 다 지워졌니|
  |10|교양수업 오늘 휴강 확실한지|0|우리 교양수업 오늘 휴강된 거 확실해|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.sae4k
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("sae4k/augmented")
  ```



## License

[This work is licensed under a CC-BY-SA-4.0 License.](https://github.com/warnikchow/sae4k/blob/master/LICENSE)

<style> td {white-space: nowrap;} </style>
