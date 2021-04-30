---
layout: default
title: petitions_archive
---

# petitions_archive
{: .no_toc }

청와대 국민청원 데이터 아카이브

청와대 국민청원 게시판의 데이터를 월별로 수집한 데이터입니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/petitions_archive/petitions_archive.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/lovit/petitions_archive>
* Download size: `621.59 MiB`
* Dataset size: `631.02 MiB`
* Features:

  ```python
  FeaturesDict({
      'begin': Text(shape=(), dtype=tf.string),
      'category': Text(shape=(), dtype=tf.string),
      'content': Text(shape=(), dtype=tf.string),
      'end': Text(shape=(), dtype=tf.string),
      'num_agree': tf.int32,
      'petition_idx': Text(shape=(), dtype=tf.string),
      'status': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |436660|

* Examples:

  | |begin|category|content|end|num_agree|petition_idx|status|title|
  |---|---|---|---|---|---|---|---|---|
  |1|2017-09-18|저출산/고령화대책|안녕하세요 저는 경남 창원시에 거주 중인 36세 난임 여성 박은희라고 합니다. 이번 ...|2017-10-18|384|14496|청원종료|새로운 난임 정책 실제 부담감 줄지 않습니다.|
  |2|2018-10-25|육아/교육|저는 3자녀를 둔 엄마입니다~ 큰아이. 둘째아이는 초등학생이고 막내는 유치원생이고요~...|2018-11-24|3|419224|청원종료|유치원 에듀케어반 다자녀도 무조건1순위로 해주세요.|
  |3|2018-05-09|행정|몇일전 경찰서에 고발인 조서를 받으러가서 충격을 받았슴니다 . 사무실 출입이 폐쇄적으...|2018-06-08|2|228317|청원종료|경찰서에 설치된 장막 걷어치워 주세요|
  |4|2018-06-27|정치개혁|국민을 보호하지 않는 정부는 정부가 못 됩니다. 일제시대 임시정부의 수립 요건 안 배...|2018-07-27|58|286332|청원종료|예멘 난민 수용 반대|
  |5|2017-09-05|기타|소년법 폐지해주세요 부산여중생폭행사건 보복성 폭행이었습니다,, 가해자들은 처벌받지않는...|2017-12-04|0|4002|청원종료|소년법 폐지해주세요|
  |6|2018-10-31|성장동력|이제는 더 이상 기대 안 한다. 한국 경제는 패망의 길로 가고 있는데 새만금 갯벌에 ...|2018-11-30|27|426868|청원종료|한국 경제는 꼬꾸라지고 있는데 대통령이  태양광에 미쳐 있구나!|
  |7|2018-07-29|보건복지|지금 연금은 정해진 조건하에 죽을때까지 고정금액을 받게 되어 있읍니다 사실 나이를 먹...|2018-08-28|2|322556|청원종료|국민연금  개선합시다|
  |8|2018-10-14|기타|안녕하세요 저는 경기도의 한 초등학교 학생입니다 다름이 아니라 학교 체육시간에 피구처...|2018-11-13|3|406517|청원종료|학교에서 사용하는 공 재질을 규정해주세요|
  |9|2018-05-18|육아/교육|저는 로스쿨을 준비하고 있는 수험생입니다. 로스쿨에 우선 입학하려면 리트 라는 시험에...|2018-06-17|4|236257|청원종료|저는 로시생입니다|
  |10|2018-08-10|행정|담배를 판매하다 그만두었습니다. 청소년들이 속이고 담배를 사러 자꾸 옵니다. 안좋은일...|2018-09-09|4|334642|청원종료|청소년담배사는거  청소년과 보호자에게도 벌을 주세요.|

* Citation:

  ```text
  @misc{petitions_archive19
      title={Korean Petitions Archive},
      author={Hyunjoong Kim},
      howpublished={https://github.com/lovit/petitions_archive},
      year={2019}
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
  import tfds_korean.petitions_archive

  dataset = tfds.load("petitions_archive")
  ```

## License

[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

<style> td {white-space: nowrap;} </style>
