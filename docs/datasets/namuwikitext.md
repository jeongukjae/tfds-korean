---
layout: default
title: namuwikitext
---

# namuwikitext
{: .no_toc }

Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/namuwikitext/namuwikitext.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/lovit/namuwikitext>
* Download size: `1.68 GiB`
* Dataset size: `4.68 GiB`
* Features:

  ```python
  FeaturesDict({
      'content': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |3906579|
  |dev  |19754|
  |test  |20274|

* Examples:

  | |content|title|
  |---|---|---|
  |1|양양몰 오픈! 지하 1층 식당가 양식당 운영기!<br>시즌3 보기<br>1화: 양양몰...|= = = 시즌3 = = =|
  |2|새시대를 맞는 경건하고 숙연한 입장에서 저는 제가 지닌 모든 재산을 완전히 공개함과 ...|= 대우재단 산하 대우학원 =|
  |3|최소 200세 이상 과거 모습을 보면 쿠치키 뱌쿠야나 이치마루 긴, 히사기 슈헤이 등...|= = 개요 = =|
  |4|아주 어려움 클리어 이후 공략 작성<br>저그에겐 혼종을 효과적으로 저지할 수 있는 ...|= = = = 저그 ( 비공식 ) = = = =|
  |5|해리 포터 시리즈에 나오는 말포이 가의 하인 집요정. 일반적으로 인식되는 아름다운 요...|= = 개요 = =|
  |6|네이버 베스트 도전만화 연재작 중에서 특히 잠재력과 작품성에 있어 주목할 만한 작품들...|= = = 개요 = = =|
  |7|쿄: 비키니 입고 싸우다니 서비스 좋은데.<br>아테나: 겉모습에 한 눈 팔다가 참패...|= = VS 쿠사나기 쿄 = =|
  |8|전반적인 게임 방법은 osu! 항목을 참고하도록 한다. 여기에서는 osu!droid만...|= = 플레이 = =|
  |9|철도차량 관련 정보<br>미국의 철도 환경|= = 관련 문서 = =|
  |10|2013년 8월부터 2014년 6월까지 개최된 Project『Shangri-la』 전...|= = = Project『Shangri-la』 다큐멘터리반 = = =|

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
  import tfds_korean.namuwikitext

  dataset = tfds.load("namuwikitext")
  ```
