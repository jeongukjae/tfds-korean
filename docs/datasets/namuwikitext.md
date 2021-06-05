---
layout: default
title: namuwikitext
---

# namuwikitext
{: .no_toc }

Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.

[lovit/namuwikitext#10](https://github.com/lovit/namuwikitext/issues/10)과 같은 이슈로 홈페이지에 적힌 수대로 train, dev, test가 나오지는 않습니다.
또한 `content` 피쳐가 비어있는 값이 나올 가능성이 있으니 주의하여 사용하시길 바랍니다.

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

  | |title|content|
  |---|---|---|
  |1|= = = 시즌3 = = =|양양몰 오픈! 지하 1층 식당가 양식당 운영기!<br>시즌3 보기<br>1화: 양양몰...|
  |2|= 대우재단 산하 대우학원 =|새시대를 맞는 경건하고 숙연한 입장에서 저는 제가 지닌 모든 재산을 완전히 공개함과 ...|
  |3|= = 개요 = =|최소 200세 이상 과거 모습을 보면 쿠치키 뱌쿠야나 이치마루 긴, 히사기 슈헤이 등...|
  |4|= = = = 저그 ( 비공식 ) = = = =|아주 어려움 클리어 이후 공략 작성<br>저그에겐 혼종을 효과적으로 저지할 수 있는 ...|
  |5|= = 개요 = =|해리 포터 시리즈에 나오는 말포이 가의 하인 집요정. 일반적으로 인식되는 아름다운 요...|
  |6|= = = 개요 = = =|네이버 베스트 도전만화 연재작 중에서 특히 잠재력과 작품성에 있어 주목할 만한 작품들...|
  |7|= = VS 쿠사나기 쿄 = =|쿄: 비키니 입고 싸우다니 서비스 좋은데.<br>아테나: 겉모습에 한 눈 팔다가 참패...|
  |8|= = 플레이 = =|전반적인 게임 방법은 osu! 항목을 참고하도록 한다. 여기에서는 osu!droid만...|
  |9|= = 관련 문서 = =|철도차량 관련 정보<br>미국의 철도 환경|
  |10|= = = Project『Shangri-la』 다큐멘터리반 = = =|2013년 8월부터 2014년 6월까지 개최된 Project『Shangri-la』 전...|

* Citation:

  ```text
  @misc{namuwikitext20
      title={Namuwikitext},
      author={Hyunjoong Kim},
      howpublished={https://github.com/lovit/namuwikitext},
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
  import tfds_korean.namuwikitext

  dataset = tfds.load("namuwikitext")
  ```

## License

["CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/") which [Namuwiki dump dataset](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84) is licensed

<style> td {white-space: nowrap;} </style>
