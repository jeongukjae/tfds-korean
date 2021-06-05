---
layout: default
title: para_kqc
---

# para_kqc
{: .no_toc }

Parallel dataset of Korean Questions and Commands

paper: https://www.aclweb.org/anthology/2020.lrec-1.842/

Class description (For more details, see paper)
* `topic`: `0`) Email, `1`) Scheduling, `2`) S. Home, `3`) Weather
* `act`: `0`) Alt. Q, `1`) Wh- Q, `2`) PH, `3`) Str. REQ

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/para_kqc/para_kqc.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/warnikchow/paraKQC>
* Download size: `688.45 KiB`
* Dataset size: `696.30 KiB`
* Features:

  ```python
  FeaturesDict({
      'act': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
      'text': Tensor(shape=(10,), dtype=tf.string),
      'topic': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |1000|

* Examples:

  | |text|topic|act|
  |---|---|---|---|
  |1|지금 거실 조명 상태를 확인하려면 어떻게 해야 돼?<br>거실 조명 상태를 확인할 수 있는 방법이 뭐야?<br>거실 불이 켜져있는지 어떻게 확인해?<br>거실에 조명이 켜져있는지 확인할 수 있는 방법 좀 알려줘<br>...|2|2|
  |2|지난 달 말고 이번 달에 받은 학회 메일은 모두 지워줘.<br>다른 메일 말고 이번 달에 받은 학회 메일은 삭제해.<br>이번 달에 학교에서 온 메일 말고 학회에서 온 메일은 모두 지워.<br>메일함 용량이 부족하지 않도록 이번 달에 받은 학회 메일은 모두 삭제해.<br>...|0|0|
  |3|경기내륙 예상 강수량은?<br>경기내륙에는 얼마나 비가 올 예정이야?<br>경기내륙은 비가 얼마나 올 것으로 예상합니까?<br>경기내륙에는 비가 얼마나 올 것으로 추정되나요?<br>...|3|3|
  |4|다음주 자원봉사 시간이 어떻게 돼?<br>다음주에 자원봉사 하기로 한 거 시간이 언제야?<br>자원봉사 다음주에 어느 때에 한대?<br>자원봉사 다음주 어느 시간으로 잡혔어?<br>...|1|1|
  |5|일반 메일 말고 전체 공지메일은 수신거부 처리해주세요.<br>결제메일 말고 공지메일만 수신거부 처리해<br>전체 공지가 너무 많아 중요한 메일을 놓치면 안되니 공지메일은 수신하지 않겠습니다.<br>공지메일을 매번 지우지 말고 수신거부해줘<br>...|0|0|
  |6|네이버 메일 첨부파일 전송속도가 어떻게 돼?<br>네이버 메일에서 파일 첨부 시 빠르기가 어떻게 되나요?<br>네이버 메일 파일 첨부시 속도가 얼마나 나오나요?<br>네이버 메일이 제공하는 첨부파일 전송 속도가 얼마나 나와요?<br>...|0|0|
  |7|외부 습도는 어떻게 알 수 있어?<br>바깥 습도는 어떻게 확인할 수 있어?<br>바깥 습도를 알 수 있는 방법 좀 알려줘<br>바깥 습도를 확인하려면 어떻게 해야 돼?<br>...|2|2|
  |8|주말에 약속 잡을 거면 오전 말고 오후에 잡아.<br>주말로 약속 잡을 생각이면 오전이 아니라 오후로 하자.<br>약속 날짜를 주말로 정할 거면 오전 대신 오후로 했으면 좋겠어.<br>주말 약속은 오전에 잡지 말고 오후에 잡으세요.<br>...|1|1|
  |9|약속장소를 애매하게 잡으면 찾기 어려우니까 그렇게 하지 마세요.<br>애매하게 약속장소를 잡아 놓으면 가기 어려우니 그러지 마.<br>약속 장소가 애매하면 근처에서 헤매니까 애매하게 잡지 마.<br>근처에서 헤매고 있기 싫으니까 약속 장소 애매하게 잡지 말아 줄래?<br>...|1|1|
  |10|공지 메일 수신거부하는 방법 좀 알려줘<br>공지 메일은 어떻게 수신거부 해?<br>공지 메일 수신 거부 방법이 어떻게 되지?<br>공지 메일 수신 거부는 어떻게 할 수 있나요?<br>...|0|0|

* Citation:

  ```text
  @inproceedings{cho2020discourse,
      title={Discourse Component to Sentence (DC2S): An Efficient Human-Aided Construction of Paraphrase and Sentence Similarity Dataset},
      author={Cho, Won Ik and Kim, Jong In and Moon, Young Ki and Kim, Nam Soo},
      booktitle={Proceedings of The 12th Language Resources and Evaluation Conference},
      pages={6819--6826},
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
  import tfds_korean.para_kqc

  dataset = tfds.load("para_kqc")
  ```

## License



<style> td {white-space: nowrap;} </style>
