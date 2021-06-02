---
layout: default
title: klue_ner
---

# klue_ner
{: .no_toc }

KLUE benchmark - Named Entity Recognition(NER) task.

For more details, see [KLUE Benchmark - NER Task - Overview description](https://klue-benchmark.com/tasks/69/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_ner/klue_ner.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `12.59 MiB`
* Dataset size: `11.70 MiB`
* Features:

  ```python
  FeaturesDict({
      'labels': Sequence(Text(shape=(), dtype=tf.string)),
      'tokens': Sequence(Text(shape=(), dtype=tf.string)),
  })
  ```

* Supervised keys: `('token', 'label')`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |21008|
  |dev  |5000|

* Examples:

  | |labels|tokens|
  |---|---|---|
  |1|B-PS<br>I-PS<br>O<br>O<br>...|존<br>스<br><br>부<br>...|
  |2|B-DT<br>I-DT<br>O<br>O<br>...|3<br>월<br>에<br>는<br>...|
  |3|B-PS<br>I-PS<br>I-PS<br>I-PS<br>...|김<br><br>참<br>관<br>...|
  |4|B-PS<br>I-PS<br>I-PS<br>O<br>...|박<br>인<br>비<br>(<br>...|
  |5|B-PS<br>I-PS<br>I-PS<br>I-PS<br>...|안<br><br>시<br>인<br>...|
  |6|O<br>O<br>O<br>B-PS<br>...|앞<br>서<br><br>레<br>...|
  |7|O<br>O<br>O<br>O<br>...|감<br>독<br>의<br><br>...|
  |8|B-DT<br>I-DT<br>I-DT<br>O<br>...|1<br>4<br>일<br>(<br>...|
  |9|O<br>O<br>O<br>O<br>...|이<br><br>해<br>커<br>...|
  |10|O<br>O<br>O<br>O<br>...|조<br>사<br><br>과<br>...|

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
  import tfds_korean.klue_ner

  dataset = tfds.load("klue_ner")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/69/overview/copyright).

<style> td {white-space: nowrap;} </style>
