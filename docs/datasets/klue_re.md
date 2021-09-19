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
  * `1.0.0` False: Initial release.
  * `1.1.0` (default): KLUE 1.1.0
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

  | |guid|sentence|subject_entity/word|subject_entity/start_idx|subject_entity/end_idx|subject_entity/type|object_entity/word|object_entity/start_idx|object_entity/end_idx|object_entity/type|label|source|
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  |1|klue-re-v1_train_28110|응우옌 콩푸엉, 일본 수비수 도미야스 다케히로 등 성장 가능성이 높은 선수들을 키워내...|도미야스 다케히로|16|24|PER|수비수|12|14|POH|per:title|wikitree|
  |2|klue-re-v1_train_16650|스기타 쇼이치(1924년 7월 1일 ~ 1945년 4월 15일)는 태평양 전쟁 당시에...|일본 제국 해군|48|55|ORG|1945년|22|26|DAT|no_relation|wikipedia|
  |3|klue-re-v1_train_11917|그러나 베아트리스가 어머니인 빅토리아 여왕으로부터 혈우병 인자를 물려받은 탓에 그녀의...|빅토리아 여왕|16|22|PER|베아트리스|4|8|PER|per:children|wikipedia|
  |4|klue-re-v1_train_19166|하지만, 이후 크로노스는 키클롭스와 헤카톤케이레스를 타르타로스에 다시 감금했는데, 헤...|헤카톤케이레스|70|76|PER|타르타로스|29|33|PER|no_relation|wikipedia|
  |5|klue-re-v1_train_12447|"카스가노 우라라"(うらら 한국명:"김초원")는 토에이 애니메이션 제작의 애니메이션《...|카스가노 우라라|1|8|PER|프리큐어|52|55|POH|per:employee_of|wikipedia|
  |6|klue-re-v1_train_22309|동고트족 왕 테오다하드가 교황 아가피토 1세를 콘스탄티노폴리스에 보내었으나 유스티니아...|유스티니아누스|42|48|PER|콘스탄티노폴리스|26|33|LOC|no_relation|wikipedia|
  |7|klue-re-v1_train_05928|노무현 정부에서 사학 비리 척결을 위해 사학법 개정을 추진하자 사학 자율권 침해를 이...|이명박|74|76|PER|개신교|92|94|POH|no_relation|wikipedia|
  |8|klue-re-v1_train_12418|외질은 4-0으로 이긴 애스턴 빌라와의 마지막 프리미어리그 경기에서 올리비에 지루의 ...|토트넘 홋스퍼|68|74|ORG|프리미어리그|26|31|POH|org:member_of|wikipedia|
  |9|klue-re-v1_train_00228|오스트리아의 마리 테레즈(1638년 9월 10일 ~ 1683년 7월 30일)는 프랑스...|루이 14세|54|59|PER|마리 테레즈|7|12|PER|per:spouse|wikipedia|
  |10|klue-re-v1_train_19438|국방부는 구타행위가 계속 적발됨에 따라 향후 인성결함자들의 입영을 차단하기 위해 인성...|병무청|75|77|ORG|국방부|0|2|ORG|org:member_of|wikipedia|

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
