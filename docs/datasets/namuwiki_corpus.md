---
layout: default
title: namuwiki_corpus
---

# namuwiki_corpus
{: .no_toc }

나무위키 말뭉치.

[kss](https://github.com/hyunwoongko/kss)를 사용하여 문장 단위로 분절되어 있는 나무위키 말뭉치입니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/namuwiki_corpus/namuwiki_corpus.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/jeongukjae/namuwiki-corpus>
* Download size: `1.70 GiB`
* Dataset size: `4.93 GiB`
* Features:

  ```python
  FeaturesDict({
      'content': Sequence(Text(shape=(), dtype=tf.string)),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |3692228|

* Examples:

  | |title|content|
  |---|---|---|
  |1|첸틀 프로젝트 - 개요 - OG 시리즈|첫등장은 OG 외전.<br>슈타인백의 후원으로 극비리에 연구를 진행하고 있으며 크라이울브즈에게 아인스트 레지세이...<br>제2차 슈퍼로봇대전 OG에선 아예 가이아 세이버즈가 강룡전대와 대립하는 포지션이라 복...<br>하지만 후반에 그것이 전부 거짓말임을 밝히면서 흡수당하는 알베로를 조롱한다.<br>...|
  |2|노아 슈냅 - 개요|미국에서 활동하는 캐나다계 미국인 배우.|
  |3|아키디자인 - 상세|건축설계 실무에 사용되는 것을 고려하여 그에 관련된 기능이 좀 더 보강되어 있다.<br>그 외에 보통 캐드 프로그램들이 가진 기능도 전부 존재하는 편이다.<br>한국 개발 소프트웨어다 보니 국내 건축업계들의 피드백을 받아들여 업데이트를 진행중이다.<br>무료 버전이 배포되고 있었으나 5월 6일 이후 갑작스런 서비스 변경으로 종료 스텐다드...<br>...|
  |4|스칼로맨스 아카데미|스칼로맨스 아카데미|
  |5|시마 타마히코 - 작중 행적|본래는 사랑받지 못한 집안 특성상 염세적이고 날선 모습이었지만, 여주인공 유즈키와 가...<br>그러나 무기력에 빠져 학업을 잇는 걸 포기해 아버지에게 죽은 자식 취급을 받는다.<br>독서를 좋아해서 종종 책을 읽는 장면이 자주 나온다.<br>원래는 친동생 타마코가 가출해왔을 때도 그녀를 반기지 않을 정도로 날선 관계였다.<br>...|
  |6|김태현(축구선수) - 플레이 스타일|187cm의 장신에 흔치 않은 왼발잡이 센터백이다.<br>힘과 높이, 대인 수비는 물론 예리한 왼발 패스를 통한 빌드업 능력을 갖추었으며, 주...<br>공격력과 수비력을 겸비한 한국 축구의 차세대 센터백으로 기대를 받고 있다.|
  |7|마기아 레코드 마법소녀 마도카☆마기카 외전/가챠/2021년 - 목록 - ⏰ 모모에 나...|픽업 기간 : 2021년 2월 5일 17:00 ~ 2월 12일 15:00|
  |8|무녀(노 게임 노 라이프) - 작중 행적 - 3권|동부연합과의 게임에서 승리하여 대륙의 모든 자원을 얻은 『 』에게 동부연합 측에서 한...<br>직후『 』남매가 지브릴의 도움을 받아 자신이 있는 곳으로 오자.<br>일단, 손님은 손님이니 정중하게 자기소개를 한 후. 그들에게 "___어데, 감히 이딴...<br>그도 그럴 것이 현 동부연합의 상황은 대륙 영토. 즉, 대륙 자원을 빼앗기면 정치고 ...<br>...|
  |9|ROBOCRAFT/부품/플라즈마 런처 - 장점과 단점 - 장점|*높은 순간화력 - 플라즈마의 최대 장점으로 순간화력은 근접전 전용인 이온과 테슬라와...<br>게다가 이 둘과는 다르게 중거리 포격이 가능하기 때문에, 실질적인 체감 화력은 플라즈...<br>*범위 데미지 - 일렉트로 쉴드와 공간장갑을 뚫고 데미지가 들어간다.<br>게다가 어느 정도 빗맞춰도 온전히 피해가 들어가기 때문에, 중대형 지상로보 상대로는 ...<br>*곡사 - 낙차가 크지는 않아서 패널티가 되는 경우가 많지만, 지형을 잘 활용하면 보...|
  |10|AIBO VS 왕님·사장·범골·마리크 - 사용 오리카 - 리리컬족 - 블랙 나이트 매...|효과 일람<br>상대가 드로할때마다 레벨업하여 1500포인트씩 공격력 상승. LV3(소녀기)까지 오오...<br>이 카드가 특수 소환 되었을 때 자신의 패/덱/묘지에서 WDMG를 특수 소환할수 있다.<br>이 카드는 상대의 함정카드의 효과를 받지 않는다.<br>...|

* Citation:

  ```text
  @misc{namuwiki_corpus21
      title={Namuwiki Corpus},
      author={Ukjae Jeong},
      howpublished={https://github.com/jeongukjae/namuwiki-corpus},
      year={2021}
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
  import tfds_korean.namuwiki_corpus

  dataset = tfds.load("namuwiki_corpus")
  ```

## License

This work is licensed under a [CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/).

<style> td {white-space: nowrap;} </style>
