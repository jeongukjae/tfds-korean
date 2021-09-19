---
layout: default
title: klue_dp
---

# klue_dp
{: .no_toc }

KLUE benchmark - Dependency Parsing(DP) task.

For more details, see [KLUE Benchmark - DP Task - Overview description](https://klue-benchmark.com/tasks/71/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_dp/klue_dp.py)
* Version:
  * `1.0.0` False: Initial release.
  * `1.1.0` (default): KLUE 1.1.0
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `7.11 MiB`
* Dataset size: `6.40 MiB`
* Features:

  ```python
  FeaturesDict({
      'dependency_relation': Sequence(Text(shape=(), dtype=tf.string)),
      'head': Sequence(tf.int64),
      'lemma': Sequence(Text(shape=(), dtype=tf.string)),
      'pos': Sequence(Text(shape=(), dtype=tf.string)),
      'word_form': Sequence(Text(shape=(), dtype=tf.string)),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |10000|
  |dev  |2000|

* Examples:

  | |word_form|lemma|pos|head|dependency_relation|
  |---|---|---|---|---|---|
  |1|미국과<br>쿠바<br>정상이<br>회동한<br>...|미국 과<br>쿠바<br>정상 이<br>회동 하 ㄴ<br>...|NNP+JC<br>NNP<br>NNG+JKS<br>NNG+XSV+ETM<br>...|2<br>3<br>4<br>5<br>...|NP_CNJ<br>NP<br>NP_SBJ<br>VP_MOD<br>...|
  |2|두<br>번째<br>의상은<br>'흰색<br>...|두<br>번 째<br>의상 은<br>' 희 ㄴ 색<br>...|MMN<br>NNB+XSN<br>NNG+JX<br>SS+VA+ETM+NNB<br>...|2<br>3<br>5<br>5<br>...|DP<br>NP<br>NP_SBJ<br>NP<br>...|
  |3|요원은<br>아이를<br>안고서<br>수영장<br>...|요원 은<br>아이 를<br>안 고서<br>수영장<br>...|NNG+JX<br>NNG+JKO<br>VV+EC<br>NNG<br>...|12<br>3<br>6<br>5<br>...|NP_SBJ<br>NP_OBJ<br>VP<br>NP<br>...|
  |4|스린야시장이<br>가까운것만으로도<br>사실상<br>별5개가<br>부족합니다.|스린야시장 이<br>가깝 ㄴ 것 만 으로 도<br>사실 상<br>별 5 개 가<br>부족 하 ㅂ니다 .|NNP+JKS<br>VA+ETM+NNB+JX+JKB+JX<br>NNG+XSN<br>NNG+SN+NNB+JKS<br>NNG+XSA+EF+SF|2<br>5<br>5<br>5<br>0|NP_SBJ<br>NP_AJT<br>AP<br>NP_SBJ<br>VP|
  |5|지인들에게<br>돈을<br>빌리고<br>제때<br>...|지인 들 에게<br>돈 을<br>빌리 고<br>제때<br>...|NNG+XSN+JKB<br>NNG+JKO<br>VV+EC<br>NNG<br>...|3<br>3<br>5<br>5<br>...|NP_AJT<br>NP_OBJ<br>VP<br>AP<br>...|
  |6|정보<br>당국과<br>관련<br>실무<br>...|정보<br>당국 과<br>관련<br>실무<br>...|NNG<br>NNG+JKB<br>NNG<br>NNG<br>...|2<br>5<br>5<br>5<br>...|NP<br>NP_CNJ<br>NP<br>NP<br>...|
  |7|질병관리본부는<br>지난<br>3월부터<br>전국<br>...|질병관리본부 는<br>지나 ㄴ<br>3 월 부터<br>전국<br>...|NNP+JX<br>VV+ETM<br>SN+NNB+JX<br>NNG<br>...|21<br>3<br>9<br>6<br>...|NP_SBJ<br>VP_MOD<br>NP_AJT<br>NP<br>...|
  |8|통일부는<br>북한이<br>24일<br>판문점<br>...|통일부 는<br>북한 이<br>24 일<br>판문점<br>...|NNP+JX<br>NNP+JKS<br>SN+NNB<br>NNP<br>...|27<br>7<br>7<br>6<br>...|NP_SBJ<br>NP_SBJ<br>NP_AJT<br>NP<br>...|
  |9|또다시<br>우승컵을<br>들어올린<br>박인비는<br>...|또 다시<br>우승 컵 을<br>들 어 올리 ㄴ<br>박인비 는<br>...|MAG+MAG<br>NNG+NNG+JKO<br>VV+EC+VV+ETM<br>NNP+JX<br>...|3<br>3<br>4<br>17<br>...|AP<br>NP_OBJ<br>VP_MOD<br>NP_SBJ<br>...|
  |10|모델<br>장윤주<br>씨가<br>SNS를<br>...|모델<br>장윤주<br>씨 가<br>SNS 를<br>...|NNG<br>NNP<br>NNB+JKS<br>SL+JKO<br>...|3<br>3<br>9<br>5<br>...|NP<br>NP<br>NP_SBJ<br>NP_OBJ<br>...|

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
  import tfds_korean.klue_dp

  dataset = tfds.load("klue_dp")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/71/overview/copyright).

<style> td {white-space: nowrap;} </style>
