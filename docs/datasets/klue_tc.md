---
layout: default
title: klue_tc
---

# klue_tc
{: .no_toc }

KLUE benchmark - Topic Classification(TC a.k.a. YANT, Yonhap News Agency Topic Classification) task.

For more details, see [KLUE Benchmark - TC Task - Overview description](https://klue-benchmark.com/tasks/66/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_tc/klue_tc.py)
* Version:
  * `1.0.0` False: Initial release.
  * `1.1.0` (default): KLUE 1.1.0
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `52.75 MiB`
* Dataset size: `16.76 MiB`
* Features:

  ```python
  FeaturesDict({
      'date': Text(shape=(), dtype=tf.string),
      'guid': Text(shape=(), dtype=tf.string),
      'label': Text(shape=(), dtype=tf.string),
      'predefined_news_category': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
      'url': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |45678|
  |dev  |9107|

* Examples:

  | |guid|title|predefined_news_category|label|url|date|
  |---|---|---|---|---|---|---|
  |1|ynat-v1_train_17751|게시판 카카오 대학생 프로그래밍 경진대회|IT과학|IT과학|https://news.naver.com/main/read.nhn?mode=LS2D&...|2018.06.15. 오후 5:53|
  |2|ynat-v1_train_45353|유엔 보고관 어산지에 대한 처우 생명에 위협적|세계|세계|https://news.naver.com/main/read.nhn?mode=LS2D&...|2019.11.02. 오전 12:26|
  |3|ynat-v1_train_16219|최영미 시인 호텔방 요청으로 구설…공짜 요구하지 않았다|생활문화|사회|https://news.naver.com/main/read.nhn?mode=LS2D&...|2017.09.10. 오후 8:00|
  |4|ynat-v1_train_06178|최지만 시즌 4번째 2루타…탬파베이는 5연승 질주|스포츠|스포츠|https://sports.news.naver.com/news.nhn?oid=001&...|2019.04.13 11:34|
  |5|ynat-v1_train_32586|동서 자기주식 62억원어치 취득 결정|경제|경제|https://news.naver.com/main/read.nhn?mode=LS2D&...|2018.09.20. 오전 11:21|
  |6|ynat-v1_train_11547|그래픽 네이마르 몸값 1위 등극|스포츠|스포츠|https://sports.news.naver.com/news.nhn?oid=001&...|2017.08.04 10:20|
  |7|ynat-v1_train_45194|대학 내 권력형 성범죄 해결하라|사회|사회|https://news.naver.com/main/read.nhn?mode=LS2D&...|2019.07.07. 오후 4:22|
  |8|ynat-v1_train_18677|SBS 뉴스 봄 개편…24시간 유튜브 라이브 시작|사회|생활문화|https://news.naver.com/main/read.nhn?mode=LS2D&...|2019.03.14. 오전 9:04|
  |9|ynat-v1_train_27743|레스터시티 우승 9개월 만에 라니에리 감독 경질|스포츠|스포츠|https://sports.news.naver.com/news.nhn?oid=001&...|2017.02.24 06:24|
  |10|ynat-v1_train_28721|트럼프 미군 철수 위협 반복…나토동맹국도 무조건 방어 안해종합|세계|세계|https://news.naver.com/main/read.nhn?mode=LS2D&...|2016.07.22. 오전 3:03|

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
  import tfds_korean.klue_tc

  dataset = tfds.load("klue_tc")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/66/overview/copyright).

<style> td {white-space: nowrap;} </style>
