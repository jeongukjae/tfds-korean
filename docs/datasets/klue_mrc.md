---
layout: default
title: klue_mrc
---

# klue_mrc
{: .no_toc }

KLUE benchmark - Machine Reading Comprehension (MRC) task.

or more details, see [KLUE Benchmark - MRC Task - Overview description](https://klue-benchmark.com/tasks/72/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_mrc/klue_mrc.py)
* Version:
  * `1.0.0` False: Initial release.
  * `1.1.0` (default): KLUE 1.1.0
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `63.58 MiB`
* Dataset size: `62.91 MiB`
* Features:

  ```python
  FeaturesDict({
      'answers': Sequence({
          'answer_start': tf.int64,
          'text': Text(shape=(), dtype=tf.string),
      }),
      'context': Text(shape=(), dtype=tf.string),
      'guid': Text(shape=(), dtype=tf.string),
      'is_impossible': tf.bool,
      'news_category': Text(shape=(), dtype=tf.string),
      'question': Text(shape=(), dtype=tf.string),
      'question_type': tf.int64,
      'source': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |17554|
  |dev  |5841|

* Examples:

  | |guid|title|news_category|source|context|question|question_type|answers/text|answers/answer_start|is_impossible|
  |---|---|---|---|---|---|---|---|---|---|---|
  |1|klue-mrc-v1_train_08578|날개 다는 중동 비즈니스 ...한전·효성 등 대기업들 사우디 진출 확대|기획|hankyung|한국전력 LG전자 효성 두산중공업 포스코 등 박근혜 대통령 중동 순방 경제사절단에 포...|MOU 체결 서명식에 참여한 시공업체 개수는?|1|5개<br>5|318<br>318|False|
  |2|klue-mrc-v1_train_09718|CJ, 3년간 정규직 1만4000명 뽑는다|산업섹션|hankyung|CJ그룹이 올해부터 2017년까지 3년 동안 1만4000명의 정규직 신입사원을 채용한...|CJ가 2017년에 뽑으려고 하는 목표 신입사원 수는?|1|5500명<br>5500|210<br>210|False|
  |3|klue-mrc-v1_train_03248|데인인의 사적||wikipedia|삭소의 원본 필사본은 거의 소실되고, 파편 네 개만 남아 있다. 안게르스 파편, 라센...|페데르센을 도와준 덴마크 대주교의 이름은?|3|비르게르 군네르센|489|True|
  |4|klue-mrc-v1_train_14101|새 정부 최우선 과제는 ‘경기부양’ ‘신성장동력 확보’|기획|hankyung|‘경기부양으로 일자리를 창출하는 동시에 신성장 동력을 확보해야 한다.’국내 경제전문가...|설문조사에 참여한 일본인의 수는?|3|60명<br>60|148<br>148|True|
  |5|klue-mrc-v1_train_04259|대학||wikipedia|중세 중기의 십자군 원정을 통해 유럽이 아랍 문화와 접하게 되자 그 곳에 전수되었던 ...|1109년에 세워진 영국의 대학은?|3|파리 대학|816|True|
  |6|klue-mrc-v1_train_11410|“여죄수 벨마役 60세까지 하고 싶어요”|문화/TV|hankyung|“60세까지 ‘시카고’ 무대에 오르고 싶어요.”한국 뮤지컬의 ‘자존심’이자 ‘간판’인...|남여 주인공의 춤이 주가 되는 작품의 이름은?|3|디큐브아트센터|150|True|
  |7|klue-mrc-v1_train_07695|실물경기 주춤|경제|hankyung|회복세를 보이던 실물경기가 지난달 하락세로 돌아섰다. 하지만 정부는 1월 설연휴 등에...|산업활동동향이 두 달째 하락세인 산업은?|2|광공업생산|129|False|
  |8|klue-mrc-v1_train_04886|에어포트 조반||wikipedia|이 열차는 조반 선 경유로는 처음으로 나리타 국제 공항을 잇는 열차로, 2007년 1...|에어포트 조반의 평균 운행 시간은?|3|1시간 59분|91|True|
  |9|klue-mrc-v1_train_14469|실리콘밸리의 ‘특별한 하숙집’...예비창업자 3600弗 내면 혁신수업·이민설명회|국제|hankyung|스타트업의 메카 실리콘밸리에 창업 인큐베이터를 자처하는 특별한 하숙집이 생겼다. 미국...|클라우드 기반 관리 프로그램 사용자는?|3|프랑수아 디스포|396|True|
  |10|klue-mrc-v1_train_12169|M&A‘오뚝이’ GS … STX에너지 품고 자원개발 가속도|산업섹션|hankyung|정유사업 의존도가 높은 GS그룹이 STX에너지를 인수한다. 앞으로 발전사업 강화를 통...|합병 후 회사 내 불협화음이 잦다고 말한 사람은?|3|그룹 관계자|612|True|

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
  import tfds_korean.klue_mrc

  dataset = tfds.load("klue_mrc")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/72/overview/copyright).

<style> td {white-space: nowrap;} </style>
