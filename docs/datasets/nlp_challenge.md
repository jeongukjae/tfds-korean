---
layout: default
title: nlp_challenge
---

# nlp_challenge
{: .no_toc }

네이버, 창원대가 함께하는 NLP Challenge 기술 대회의 NER/SRL 데이터.

자세한 정보는 <https://air.changwon.ac.kr/?page_id=14>와 <https://air.changwon.ac.kr/?page_id=10>를 참고하세요.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/nlp_challenge/nlp_challenge.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/naver/nlp-challenge>
* Citation:

  ```text
  @misc{Naver2018,
    author = {Naver},
    title = {NLP Challenge},
    year = {2018},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/naver/nlp-challenge}},
    commit = {a51654472e0da75cd37c6e73ffe583db78e68323}
  }
  ```

## Configs


### nlp_challenge/ner (default)

NLP Challenge NER dataset

* Dataset size: `18.33 MiB`
* Download size: `16.16 MiB`
* Features:

  ```python
  FeaturesDict({
      'tags': Tensor(shape=(None,), dtype=tf.string),
      'tokens': Tensor(shape=(None,), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |90000|

* Examples:

  | |tokens|tags|
  |---|---|---|
  |1|오는<br>12월<br>플라마가<br>쌍용이란<br>...|DAT_B<br>DAT_I<br>ORG_B<br>ORG_B<br>...|
  |2|-제이미,<br>사건현장을<br>문안해<br>볼게요<br>.|PER_B<br>-<br>-<br>-<br>-|
  |3|코토<br>·<br>우승미의<br>제니트,<br>...|PER_B<br>-<br>PER_B<br>ORG_B<br>...|
  |4|PSV<br>에인트호벤(네덜란드)을<br>20-0(합계<br>25-1)으로<br>...|ORG_B<br>ORG_I<br>NUM_B<br>NUM_B<br>...|
  |5|-16위입니다,<br>중앙여<br>.|NUM_B<br>ORG_B<br>-|
  |6|젊은<br>역사가들이<br>변화구를<br>못친다는<br>...|-<br>CVL_B<br>TRM_B<br>-<br>...|
  |7|갈라타민의<br>손을<br>떠난<br>공은<br>...|PER_B<br>ANM_B<br>-<br>-<br>...|
  |8|일일<br>이제<br>진행중인<br>자연보호계획이<br>...|DAT_B<br>-<br>-<br>-<br>...|
  |9|성제가<br>열린<br>축구경기장<br>절대악몽에는<br>...|-<br>-<br>-<br>AFW_B<br>...|
  |10|26,<br>14세트를<br>잇달아<br>내줄<br>...|NUM_B<br>NUM_B<br>-<br>-<br>...|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.nlp_challenge
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("nlp_challenge/ner")
  ```


### nlp_challenge/srl 

NLP Challenge SRL dataset

* Dataset size: `7.16 MiB`
* Download size: `6.31 MiB`
* Features:

  ```python
  FeaturesDict({
      'tags': Tensor(shape=(None,), dtype=tf.string),
      'tokens': Tensor(shape=(None,), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |34857|

* Examples:

  | |tokens|tags|
  |---|---|---|
  |1|수부를<br>쓰는<br>영성적<br>노동은<br>...|ARG1<br>-<br>-<br>ARG1<br>...|
  |2|국문<br>사회면의<br>술어를<br>빌리자면<br>...|-<br>-<br>ARG1<br>-<br>...|
  |3|검사는<br>주말에만<br>하고<br>있으며<br>...|ARG1<br>ARGM-TMP<br>-<br>-<br>...|
  |4|프왑의<br>가르침은<br>동.서양에<br>대한<br>...|-<br>ARG1<br>ARGM-LOC<br>-<br>...|
  |5|두<br>새끼의<br>간이<br>콩알만큼<br>달랑해졌다.|-<br>-<br>ARG1<br>ARGM-EXT<br>-|
  |6|구수한<br>육수냄새가<br>중국식당들의<br>문틈으로<br>...|-<br>ARG1<br>-<br>ARGM-DIR<br>...|
  |7|삼천리금수강산은<br>10년<br>피파<br>월드컵<br>...|ARG0<br>-<br>-<br>-<br>...|
  |8|평교사에<br>대한<br>근무평정은<br>교감이<br>...|ARG2<br>-<br>-<br>ARG0<br>...|
  |9|두<br>가국<br>관계는<br>중화민국의<br>...|-<br>-<br>ARG1<br>-<br>...|
  |10|소년은<br>하모니카를<br>입에<br>물었다.|ARG0<br>ARG1<br>ARG3<br>-|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.nlp_challenge
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("nlp_challenge/srl")
  ```



## License

> 제공되는 코퍼스는 Data.ly에서 제작한 것으로, 연구 및 리더보드를 위한 학습으로 사용 가능하며 상업적인 목적으로 사용될 수 없음을 알려드립니다. 추가문의가 필요한 경우 메일을 남겨주세요.

<style> td {white-space: nowrap;} </style>
