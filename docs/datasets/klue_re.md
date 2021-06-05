---
layout: default
title: klue_re
---

# klue_re
{: .no_toc }

KLUE benchmark - Relation Extraction(RE) task.

For more details, see [KLUE Benchmark - RE Task - Overview description](https://klue-benchmark.com/tasks/70/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_re/klue_re.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `26.26 MiB`
* Dataset size: `23.81 MiB`
* Features:

  ```python
  FeaturesDict({
      'guid': Text(shape=(), dtype=tf.string),
      'label': Text(shape=(), dtype=tf.string),
      'object_entity': FeaturesDict({
          'end_idx': tf.int64,
          'start_idx': tf.int64,
          'type': Text(shape=(), dtype=tf.string),
          'word': Text(shape=(), dtype=tf.string),
      }),
      'sentence': Text(shape=(), dtype=tf.string),
      'source': Text(shape=(), dtype=tf.string),
      'subject_entity': FeaturesDict({
          'end_idx': tf.int64,
          'start_idx': tf.int64,
          'type': Text(shape=(), dtype=tf.string),
          'word': Text(shape=(), dtype=tf.string),
      }),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |32470|
  |dev  |7765|

* Examples:

  | |guid|label|object_entity/end_idx|object_entity/start_idx|object_entity/type|object_entity/word|sentence|source|subject_entity/end_idx|subject_entity/start_idx|subject_entity/type|subject_entity/word|
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  |1|klue-re-v1_train_28110|per:title|14|12|POH|수비수|응우옌 콩푸엉, 일본 수비수 도미야스 다케히로 등 성장 가능성이 높은 선수들을 키워내...|wikitree|24|16|PER|도미야스 다케히로|
  |2|klue-re-v1_train_16650|no_relation|26|22|DAT|1945년|스기타 쇼이치(1924년 7월 1일 ~ 1945년 4월 15일)는 태평양 전쟁 당시에...|wikipedia|55|48|ORG|일본 제국 해군|
  |3|klue-re-v1_train_11917|per:children|8|4|PER|베아트리스|그러나 베아트리스가 어머니인 빅토리아 여왕으로부터 혈우병 인자를 물려받은 탓에 그녀의...|wikipedia|22|16|PER|빅토리아 여왕|
  |4|klue-re-v1_train_19166|no_relation|33|29|PER|타르타로스|하지만, 이후 크로노스는 키클롭스와 헤카톤케이레스를 타르타로스에 다시 감금했는데, 헤...|wikipedia|76|70|PER|헤카톤케이레스|
  |5|klue-re-v1_train_12447|per:employee_of|55|52|POH|프리큐어|"카스가노 우라라"(うらら 한국명:"김초원")는 토에이 애니메이션 제작의 애니메이션《...|wikipedia|8|1|PER|카스가노 우라라|
  |6|klue-re-v1_train_22309|no_relation|33|26|LOC|콘스탄티노폴리스|동고트족 왕 테오다하드가 교황 아가피토 1세를 콘스탄티노폴리스에 보내었으나 유스티니아...|wikipedia|48|42|PER|유스티니아누스|
  |7|klue-re-v1_train_05928|no_relation|94|92|POH|개신교|노무현 정부에서 사학 비리 척결을 위해 사학법 개정을 추진하자 사학 자율권 침해를 이...|wikipedia|76|74|PER|이명박|
  |8|klue-re-v1_train_12418|org:member_of|31|26|POH|프리미어리그|외질은 4-0으로 이긴 애스턴 빌라와의 마지막 프리미어리그 경기에서 올리비에 지루의 ...|wikipedia|74|68|ORG|토트넘 홋스퍼|
  |9|klue-re-v1_train_00228|per:spouse|12|7|PER|마리 테레즈|오스트리아의 마리 테레즈(1638년 9월 10일 ~ 1683년 7월 30일)는 프랑스...|wikipedia|59|54|PER|루이 14세|
  |10|klue-re-v1_train_19438|org:member_of|2|0|ORG|국방부|국방부는 구타행위가 계속 적발됨에 따라 향후 인성결함자들의 입영을 차단하기 위해 인성...|wikipedia|77|75|ORG|병무청|

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
  import tfds_korean.klue_re

  dataset = tfds.load("klue_re")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/70/overview/copyright).

<style> td {white-space: nowrap;} </style>
