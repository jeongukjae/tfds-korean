---
layout: default
title: kmounlp_ner
---

# kmounlp_ner
{: .no_toc }

한국어 개체명 정의 및 표지 표준화 기술보고서와 이를 기반으로 제작된 개체명 형태소 말뭉치

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/kmounlp_ner/kmounlp_ner.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/kmounlp/NER>
* Download size: `22.67 MiB`
* Dataset size: `28.81 MiB`
* Features:

  ```python
  FeaturesDict({
      'lemma': Tensor(shape=(None,), dtype=tf.string),
      'named_entity': Tensor(shape=(None,), dtype=tf.string),
      'pos': Tensor(shape=(None,), dtype=tf.string),
      'recognized': Text(shape=(), dtype=tf.string),
      'text': Text(shape=(), dtype=tf.string),
      'tokens': Tensor(shape=(None,), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |23964|

* Examples:

  | |lemma|named_entity|pos|recognized|text|tokens|
  |---|---|---|---|---|---|---|
  |1|그리고<br>_<br>25<br>일<br>...|O<br>O<br>B-DAT<br>I-DAT<br>...|MAJ<br>_<br>SN<br>NNB<br>...|그리고 <25일:DAT> 현재까지 <4박:NOH><5일:NOH>을 먹고 자며 생활하고...|그리고 25일 현재까지 4박5일을 먹고 자며 생활하고 있다.|그리고<br>_<br>25<br>일<br>...|
  |2|동부<br>_<br>선수<br>들<br>...|B-ORG<br>O<br>O<br>O<br>...|NNP<br>_<br>NNG<br>XSN<br>...|<동부:ORG> 선수들은 <3차:NOH>전 패배 후 “욕심을 버리고 평상시 플레이를 ...|동부 선수들은 3차전 패배 후 “욕심을 버리고 평상시 플레이를 하라”는 전창진 감독의...|동부<br>_<br>선수<br>들<br>...|
  |3|윤<br>_<br>장관<br>은<br>...|B-PER<br>O<br>O<br>O<br>...|NNP<br>_<br>NNG<br>JX<br>...|<윤:PER> 장관은 "미세먼지 대책에 평점을 준다면 몇 점을 주겠느냐"는 또 다른 ...|윤 장관은 "미세먼지 대책에 평점을 준다면 몇 점을 주겠느냐"는 또 다른 질문에 대해...|윤<br>_<br>장관<br>은<br>...|
  |4|그렇<br>었<br>던<br>_<br>...|O<br>O<br>O<br>O<br>...|VA<br>EP<br>ETM<br>_<br>...|그랬던 그가 ‘<비박:ORG>’ ‘<탈박:ORG>’의 대표 인사로 분류되니 실감이 안...|그랬던 그가 ‘비박’ ‘탈박’의 대표 인사로 분류되니 실감이 안 날 수밖에. 이번 인...|그<br>랬<br>던<br>_<br>...|
  |5|영화<br>_<br>감독<br>_<br>...|O<br>O<br>O<br>O<br>...|NNG<br>_<br>NNG<br>_<br>...|영화 감독 <장예모:PER>가 개막식의 총 연출을 맡은 개막식은 <8시:TIM>부터 ...|영화 감독 장예모가 개막식의 총 연출을 맡은 개막식은 8시부터 3시간 반 동안 진행되...|영화<br>_<br>감독<br>_<br>...|
  |6|동부<br>_<br>김주성<br>은<br>...|B-ORG<br>O<br>B-PER<br>O<br>...|NNP<br>_<br>NNP<br>JX<br>...|<동부:ORG> <김주성:PER>은 <9일:DAT> <안양실내체육관:LOC>에서 열린...|동부 김주성은 9일 안양실내체육관에서 열린 07~08 SK텔레콤 T 프로농구 4강 플...|동부<br>_<br>김주성<br>은<br>...|
  |7|브레댄코<br>_<br>베이커리<br>창업<br>...|B-PER<br>O<br>O<br>O<br>...|NNG<br>_<br>NNG<br>NNG<br>...|<브레댄코:PER> 베이커리창업 및 특수상권 개발 문의는 전화(<02-532-6419...|브레댄코 베이커리창업 및 특수상권 개발 문의는 전화(02-532-6419)로 확인할 ...|브레댄코<br>_<br>베이커리<br>창업<br>...|
  |8|한국공항공사<br>_<br>청주<br>지사<br>...|B-ORG<br>I-ORG<br>I-ORG<br>I-ORG<br>...|NNP<br>_<br>NNP<br>NNG<br>...|<한국공항공사 청주지사:ORG> 측은 이 같은 <청주공항:ORG>의 성장 배경을 △<...|한국공항공사 청주지사 측은 이 같은 청주공항의 성장 배경을 △2008년 시작된 24시...|한국공항공사<br>_<br>청주<br>지사<br>...|
  |9|●<br>왜<br>_<br>호나우두<br>...|O<br>O<br>O<br>B-PER<br>...|SW<br>MAG<br>_<br>NNP<br>...|●왜 <호나우두:PER>는 세계 최고인가 ?|●왜 호나우두는 세계 최고인가 ?|●<br>왜<br>_<br>호나우두<br>...|
  |10|북한<br>이<br>_<br>열병식<br>...|B-ORG<br>O<br>O<br>O<br>...|NNP<br>JKS<br>_<br>NNG<br>...|<북한:ORG>이 열병식에 전략무기들을 총동원한 것은 <도널드 트럼프:PER> <미국...|북한이 열병식에 전략무기들을 총동원한 것은 도널드 트럼프 미국 행정부의 거세지는 대북...|북한<br>이<br>_<br>열병식<br>...|

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
  import tfds_korean.kmounlp_ner

  dataset = tfds.load("kmounlp_ner")
  ```
