---
layout: default
title: kornli
---

# kornli
{: .no_toc }

The dataset for the paper [_KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding_](https://arxiv.org/abs/2004.03289).

For more details, see <https://github.com/kakaobrain/KorNLUDatasets>.
This work is licensed under the [Creative Commons Attribution-ShareAlike license (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/kornli/kornli.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/kakaobrain/KorNLUDatasets>
* Download size: `156.00 MiB`
* Dataset size: `201.43 MiB`
* Features:

  ```python
  FeaturesDict({
      'gold_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
      'sentence1': Text(shape=(), dtype=tf.string),
      'sentence2': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |mnli_train  |392702|
  |snli_train  |550152|
  |xnli_dev  |2490|
  |xnli_test  |5010|

* Examples:

  | |sentence1|sentence2|gold_label|
  |---|---|---|---|
  |1|음-흠 그래, 만약 그것이 그들 나라에 있다면, 그들이 그 중 일부를 감상하는 데 확...|사람들은 그들의 나라에서 온 것만을 감상한다|0|
  |2|내가 갈 거라고 기대했는데 2주 후에 물건을 내려놓고 돌아가면 그녀가 그걸 끝냈다는 ...|내가 갈 줄 알았는데 네가 물건을 떨어뜨릴 줄 알았어.|2|
  |3|아니, 우린 파크 파크 플라자 파크 스위트룸에 있었어|우리는 파크 플라자 스위트룸에 방을 구할 수 없었다.|1|
  |4|KENNEDY, J.는 STEVENS, SOUTER, GINSBURG 및 BREYER...|J. 케네디는 법원의 의견을 밝혔다.|2|
  |5|그러나 우리의 편견은 보여주고 있다.|우리는 분명히 인종차별주의자였다.|0|
  |6|그러나 이집트인들은 끈질긴 가게 주인이고 그들의 판매 투구를 무시하려면 강철과 유머감...|당신은 세일즈 투구를 피하는 데 큰 어려움을 겪지 않을 것이다.|1|
  |7|음, 나는 내가 테니스를 친지 30년이 지났을 거라고 확신해.|나는 10년 이상 테니스를 치지 않은 것 같다.|2|
  |8|큰 광장으로 양쪽 끝에 정박해 있는 웅장한 도로는 양쪽 측면에 대칭적인 거리 패턴을 ...|큰 도로의 양쪽 끝에 큰 광장이 있다.|2|
  |9|그리고 그 이유들은 무엇인가?|그것 말고 다른 이유가 있나요?|0|
  |10|랄피 디너의 이름을 딴 남자의 안도감 같은 게 있는데 알고 보니 오리올스에서 일했는데...|랄피의 식당은 오리올스의 매니저의 이름을 따서 지어졌다.|0|

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
  import tfds_korean.kornli

  dataset = tfds.load("kornli")
  ```

## License

[Creative Commons Attribution-ShareAlike license (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

<style> td {white-space: nowrap;} </style>
