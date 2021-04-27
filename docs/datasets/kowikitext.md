---
layout: default
title: kowikitext
---

# kowikitext
{: .no_toc }

Wikitext format Korean corpus

한국어 위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/kowikitext/kowikitext.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/lovit/kowikitext>
* Download size: `383.95 MiB`
* Dataset size: `1.05 GiB`
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
  |train  |2155299|
  |dev  |11134|
  |test  |11112|

* Examples:

  | |content|title|
  |---|---|---|
  |1|텍사스주는 주요한 제조업 주들 중의 하나이며, 캘리포니아주를 빼고 여러 주보다 더 많...|= = = 제조업  = = =|
  |2|진구포자충목 (Eucoccidiorida)<br>아델레아아목 (Adeleorina)<...|= = 하위 분류  = =|
  |3||= 분류:가나의 업종별 기업 =|
  |4|WPO는 다음을 의미한다.<br>전체 프로그램 최적화(Whole program opt...|= WPO =|
  |5|코너 스티븐 랜들(Connor Steven Randall, 1995년 10월 21일 ...|= 코너 랜들 =|
  |6|우천학원 - 우신고등학교 학교법인|= = 하이트진로 관계 계열사  = =|
  |7|그해 4월에는 3승을 올렸는데도 불구하고 평균 자책점이 6점대로 나올 정도의 안정감이...|= = = = 2014년  = = = =|
  |8|내판역(內板驛)은 세종특별자치시 연동면 내판리에 있는 경부선의 철도역이다. 현재는 모...|= 내판역 =|
  |9||= 분류:미평가 품질 힙합 문서 =|
  |10|HN-2 - 러시아 Kh-55의 중국산 카피, 사거리 1,800 km<br>HN-3 ...|= = 더 보기  = =|

* Citation:

  ```text
  @misc{kowikitext20
      title={Ko-wikitext},
      author={Hyunjoong Kim},
      howpublished={https://github.com/lovit/kowikitext},
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
  import tfds_korean.kowikitext

  dataset = tfds.load("kowikitext")
  ```

## License

[CC-BY-SA 3.0](https://www.creativecommons.org/licenses/by-sa/3.0/) which [kowiki](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EC%A0%80%EC%9E%91%EA%B6%8C) dump dataset is licensed
