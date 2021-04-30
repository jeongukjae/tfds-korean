---
layout: default
title: nsmc
---

# nsmc
{: .no_toc }

Naver sentiment movie corpus v1.0

This is a movie review dataset in the Korean language. Reviews were scraped from [Naver Movies](http://movie.naver.com/movie/point/af/list.nhn).
The dataset construction is based on the method noted in [Large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) from Maas et al., 2011.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/nsmc/nsmc.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/e9t/nsmc>
* Download size: `18.62 MiB`
* Dataset size: `23.58 MiB`
* Features:

  ```python
  FeaturesDict({
      'document': Text(shape=(), dtype=tf.string),
      'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
  })
  ```

* Supervised keys: `('document', 'label')`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |150000|
  |test  |50000|

* Examples:

  | |document|label|
  |---|---|---|
  |1|테리 길리암을 믿었는데... 감독 극본 연출 모두 조델 퍼랜드일꺼 같은 느낌-_-|0|
  |2|불가능이란 없는 것. 감동적이네요|1|
  |3|후쿠사카 킨지가 이영화찍는도중 사망하여 그아들이 바톤받아 제작했지만결국 전작의 원작을...|0|
  |4|작가가 중학교를 체 졸업하지 못한 것 같은 드라마. 중2병이 보면 재미있을수도 있겠다...|0|
  |5|다양한 역설적 요소들은 이해하더라도 공감하고 즐기기에는 힘들다..|0|
  |6|마치 돌고있는 회전목마에서는 하차할 수 없다는 느낌같은 것이 문뜩 들었다.|1|
  |7|어디로 비상하는건여??? 왜 19금이여???? 이런영화는 그만....|0|
  |8|달팽이의 별에서 온 남자의 느리고 아름다운 세상체험기. 세상과 연인에 대한 그의 사랑...|1|
  |9|장면 장면의 센스는 돋보이나 전체적으로 유치하기 짝이없다|0|
  |10|재밌나? 우린 죽을 맛이다|0|

* Citation:

  ```text
  @misc{nsmc16
      title={Naver Sentiment Movie Corpus},
      author={Lucy Park},
      howpublished={https://github.com/e9t/nsmc},
      year={2016}
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
  import tfds_korean.nsmc

  dataset = tfds.load("nsmc")
  ```

## License

[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

<style> td {white-space: nowrap;} </style>
