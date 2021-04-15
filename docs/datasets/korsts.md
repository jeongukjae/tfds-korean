---
layout: default
title: korsts
---

# korsts
{: .no_toc }

The dataset for the paper [_KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding_](https://arxiv.org/abs/2004.03289).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/korsts/korsts.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/kakaobrain/KorNLUDatasets>
* Download size: `1.53 MiB`
* Dataset size: `2.30 MiB`
* Features:

  ```python
  FeaturesDict({
      'filename': Text(shape=(), dtype=tf.string),
      'genre': Text(shape=(), dtype=tf.string),
      'score': tf.float32,
      'sentence1': Text(shape=(), dtype=tf.string),
      'sentence2': Text(shape=(), dtype=tf.string),
      'year': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|
  |train  |5749|1|
  |dev  |1500|1|
  |test  |1379|1|

* Examples:

  | |filename|genre|score|sentence1|sentence2|year|
  |---|---|---|---|---|---|---|
  |1|images|main-captions|3.4000|한 남자가 폭포 근처에 물속에 서 있다.|한 남자가 물속으로 걸어 들어가 물이 떨어지는 것을 지켜본다.|2015|
  |2|MSRvid|main-captions|0.0000|고양이가 TV를 보고 있다.|남자가 휴가를 갈고 있다.|2012test|
  |3|images|main-captions|3.2000|분수 앞에 푸른 셔츠를 입은 남자.|푸른 셔츠와 황갈색 바지를 입은 한 남자가 자갈 돌로 포장된 광장에 있는 한 남자의 ...|2014|
  |4|deft-news|main-news|3.4000|배시스템은 영국의 가장 큰 방위회사이다.|배제도는 영국에서 가장 큰 군대이다|2014|
  |5|headlines|main-news|3.6000|푸틴 사인 범죄수사국|09 : 32명의 푸틴이 범죄 합병을 금지|2015|
  |6|MSRvid|main-captions|2.4000|그 여자는 감자를 잘랐다.|남자가 감자를 자르고 있다.|2012test|
  |7|deft-forum|main-forum|1.8000|죄 많은 사람들은 천국에 가지 못한다.|죄는 천국으로 들어가면 없어진다.|2014|
  |8|MSRvid|main-captions|0.2500|고양이가 피아노를 치고 있다.|고양이가 발을 핥고 있다.|2012train|
  |9|deft-forum|main-forum|4.8000|이것은 에 있는 옛 기록을 능가한다.|이것은 에 설정된 일일 기록을 깨뜨린다.|2014|
  |10|images|main-captions|4.2000|거실에는 식탁이 배경으로 놓여 있다.|배경에 식당이 있는 거실의 보기.|2014|

* Citation:

  ```text
  @article{ham2020kornli,
      title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
      author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
      journal={arXiv preprint arXiv:2004.03289},
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
  import tfds_korean.korsts

  dataset = tfds.load("korsts")
  ```
