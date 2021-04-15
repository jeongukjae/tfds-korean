---
layout: default
title: nlp_challenge
---

# nlp_challenge
{: .no_toc }

네이버, 창원대가 함께하는 NLP Challenge 기술 대회의 NER/SRL 데이터

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

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|
  |train  |90000|1|

* Examples:

  | |tags|tokens|
  |---|---|---|
  |1|DAT_B<br>DAT_I<br>ORG_B<br>ORG_B<br>...|오는<br>12월<br>플라마가<br>쌍용이란<br>...|
  |2|PER_B<br>-<br>-<br>-<br>-|-제이미,<br>사건현장을<br>문안해<br>볼게요<br>.|
  |3|PER_B<br>-<br>PER_B<br>ORG_B<br>...|코토<br>·<br>우승미의<br>제니트,<br>...|
  |4|ORG_B<br>ORG_I<br>NUM_B<br>NUM_B<br>...|PSV<br>에인트호벤(네덜란드)을<br>20-0(합계<br>25-1)으로<br>...|
  |5|NUM_B<br>ORG_B<br>-|-16위입니다,<br>중앙여<br>.|
  |6|-<br>CVL_B<br>TRM_B<br>-<br>...|젊은<br>역사가들이<br>변화구를<br>못친다는<br>...|
  |7|PER_B<br>ANM_B<br>-<br>-<br>...|갈라타민의<br>손을<br>떠난<br>공은<br>...|
  |8|DAT_B<br>-<br>-<br>-<br>...|일일<br>이제<br>진행중인<br>자연보호계획이<br>...|
  |9|-<br>-<br>-<br>AFW_B<br>...|성제가<br>열린<br>축구경기장<br>절대악몽에는<br>...|
  |10|NUM_B<br>NUM_B<br>-<br>-<br>...|26,<br>14세트를<br>잇달아<br>내줄<br>...|

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

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|
  |train  |34857|1|

* Examples:

  | |tags|tokens|
  |---|---|---|
  |1|ARG1<br>-<br>-<br>ARG1<br>...|수부를<br>쓰는<br>영성적<br>노동은<br>...|
  |2|-<br>-<br>ARG1<br>-<br>...|국문<br>사회면의<br>술어를<br>빌리자면<br>...|
  |3|ARG1<br>ARGM-TMP<br>-<br>-<br>...|검사는<br>주말에만<br>하고<br>있으며<br>...|
  |4|-<br>ARG1<br>ARGM-LOC<br>-<br>...|프왑의<br>가르침은<br>동.서양에<br>대한<br>...|
  |5|-<br>-<br>ARG1<br>ARGM-EXT<br>-|두<br>새끼의<br>간이<br>콩알만큼<br>달랑해졌다.|
  |6|-<br>ARG1<br>-<br>ARGM-DIR<br>...|구수한<br>육수냄새가<br>중국식당들의<br>문틈으로<br>...|
  |7|ARG0<br>-<br>-<br>-<br>...|삼천리금수강산은<br>10년<br>피파<br>월드컵<br>...|
  |8|ARG2<br>-<br>-<br>ARG0<br>...|평교사에<br>대한<br>근무평정은<br>교감이<br>...|
  |9|-<br>-<br>ARG1<br>-<br>...|두<br>가국<br>관계는<br>중화민국의<br>...|
  |10|ARG0<br>ARG1<br>ARG3<br>-|소년은<br>하모니카를<br>입에<br>물었다.|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.nlp_challenge
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("nlp_challenge/srl")
  ```
