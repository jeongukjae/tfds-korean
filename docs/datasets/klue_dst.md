---
layout: default
title: klue_dst
---

# klue_dst
{: .no_toc }

KLUE benchmark - Dialogue State Tracking(DST, WoS, Wizard of Seoul) task.

For more details, see [KLUE Benchmark - DST Task - Overview description](https://klue-benchmark.com/tasks/73/overview/description)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/klue_dst/klue_dst.py)
* Version:
  * `1.0.0` False: Initial release.
  * `1.1.0` (default): KLUE 1.1.0
* Homepage: <https://github.com/KLUE-benchmark/KLUE>
* Download size: `52.10 MiB`
* Dataset size: `28.14 MiB`
* Features:

  ```python
  FeaturesDict({
      'dialogue': Sequence({
          'role': Text(shape=(), dtype=tf.string),
          'state': Sequence(Text(shape=(), dtype=tf.string)),
          'text': Text(shape=(), dtype=tf.string),
      }),
      'domains': Sequence(Text(shape=(), dtype=tf.string)),
      'guid': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |8000|
  |dev  |1000|

* Examples:

  | |guid|domains|dialogue/role|dialogue/text|dialogue/state|
  |---|---|---|---|---|---|
  |1|wos-v1_train_05482|숙소|user<br>sys<br>user<br>sys<br>...|서울 남쪽에 적당한 가격대의 호텔을 예약하려고 하는데요.<br>안녕하세요. 예약 도와드리겠습니다. 찾으시는 조건에 맞는 호텔이 강남구에 포레스트 호...<br>주차가 가능해야 하는데 어디가 되나요?<br>두 곳 다 주차 가능합니다.<br>...|[숙소-가격대-적당, 숙소-종류-호텔, 숙소-지역-서울 남쪽]<br>[]<br>[숙소-가격대-적당, 숙소-종류-호텔, 숙소-지역-서울 남쪽, 숙소-주차 가능-yes]<br>[]<br>...|
  |2|wos-v1_train_04381|식당<br>관광|user<br>sys<br>user<br>sys<br>...|여보세요? 안녕하세요. 제가 서울에 놀러왔는데요. 저렴한 한식당 좀 찾아주실래요?<br>네 안녕하세요. 식당위치는 상관없으세요?<br>네 위치는 상관없어요.<br>그렇다면 서울 중구에 위치한 이럴순없는대가 평점 4점으로 만족도가 높습니다. 이곳으로...<br>...|[식당-가격대-저렴, 식당-종류-한식당]<br>[]<br>[식당-가격대-저렴, 식당-지역-dontcare, 식당-종류-한식당]<br>[]<br>...|
  |3|wos-v1_train_01629|숙소|user<br>sys<br>user<br>sys<br>...|안녕하세요. 숙소를 찾고있는데요. 가격대가 어느정도있는 비싼가격대의 숙소를 찾아주셨으...<br>안녕하세요. 반갑습니다. 찾고계신 숙소의 종류와 원하시는 위치가 있으신가요?<br>종류는 상관없습니다. 위치는 서울내면 어디든 괜찮습니다. 화요일부터 2일동안 머무를 ...<br>몇분이서 지내실 곳을 찾고계신가요?<br>...|[숙소-가격대-비싼]<br>[]<br>[숙소-가격대-비싼, 숙소-종류-dontcare, 숙소-지역-dontcare, 숙소-예약 요일-화요일, 숙소-예약 기간-2]<br>[]<br>...|
  |4|wos-v1_train_05828|숙소<br>식당<br>관광|user<br>sys<br>user<br>sys<br>...|여보세요? 안녕하세요. 저희가 가려던곳이 갑자기 문을 닫아서 예약 좀 도와주실수 있을까요?<br>안녕하세요. 네 물론입니다. 무엇을 도와드릴까요?<br>일단 서울 서쪽에 있는 적당한 가격의 에어비엔비를 알아봐주세요.<br>네 해당 조건에 예약가능한 에어비엔비가 없습니다. 혹시 호텔로 한번 더 찾아봐드릴까요?<br>...|[]<br>[]<br>[숙소-가격대-적당, 숙소-종류-에어비엔비, 숙소-지역-서울 서쪽]<br>[]<br>...|
  |5|wos-v1_train_02046|관광|user<br>sys<br>user<br>sys<br>...|안녕하세요. 저 학교 과제때문에 서울을 오기는 왔는데.. 처음이라서 막막해요. 도와주세요!<br>안녕하세요. 네, 궁금한 점 있으시면 말씀해 주세요. 성심성의껏 도와드리겠습니다.<br>학교 과제가 서울 문화 예술과 관련된 관광지에 다녀오기인데.. 이런 곳을 찾아주실 수...<br>네, 물론 찾아드릴 수 있습니다. 좀 더 구체화하기 위하여 원하시는 지역과 관광의 종...<br>...|[]<br>[]<br>[관광-문화 예술-yes]<br>[]<br>...|
  |6|wos-v1_train_00533|식당|user<br>sys<br>user<br>sys<br>...|안녕하세요. 친구들이랑 여행중인데 서울 동쪽에 좀 저렴한 한식당이 어디 있을까요?<br>안녕하세요, 네 한 곳 찾았습니다. 올림픽공원역과 가까운 순두부찌개가 대표메뉴인 두부...<br>네 일요일 12시로 7명 예약부탁해요.<br>죄송하지만 말씀주신 시간은 예약마감되셨네요.<br>...|[식당-가격대-저렴, 식당-지역-서울 동쪽, 식당-종류-한식당]<br>[]<br>[식당-가격대-저렴, 식당-지역-서울 동쪽, 식당-종류-한식당, 식당-예약 요일-일요일, ...]<br>[]<br>...|
  |7|wos-v1_train_06787|숙소|user<br>sys<br>user<br>sys<br>...|서울 북쪽에 흡연 가능한 모텔 예약할라는데요.<br>안녕하세요. 생각하시는 가격대는 있으실까요?<br>아뇨 별로 상관없어요.<br>원하시는 숙소 두 곳 뜨시는데... 왕십리역과 가까운 모텔 킹은 어떠세요? 인터넷 제...<br>...|[숙소-종류-모텔, 숙소-지역-서울 북쪽, 숙소-흡연 가능-yes]<br>[]<br>[숙소-가격대-dontcare, 숙소-종류-모텔, 숙소-지역-서울 북쪽, 숙소-흡연 가능-yes]<br>[]<br>...|
  |8|wos-v1_train_03152|택시|user<br>sys<br>user<br>sys<br>...|이에스시에서 출발할껀데 고급 택시 하나만 불러주세요.<br>출발시간은 어떻게 되시나요?<br>도착시간만 맞춰주세요.<br>그럼 도착시간과 도착지가 어디인가요?<br>...|[택시-출발지-이에스시, 택시-종류-고급]<br>[]<br>[택시-출발 시간-dontcare, 택시-출발지-이에스시, 택시-종류-고급]<br>[]<br>...|
  |9|wos-v1_train_06598|관광<br>숙소<br>지하철|user<br>sys<br>user<br>sys<br>...|관광지를 찾고 있습니다. 경치가 좋은 공원을 가고 싶은데 어디로 가면 좋을지 추천해주...<br>안녕하세요. 어느 지역에 있는 공원으로 안내해드릴까요?<br>지역은 어디든 괜찮습니다.<br>그럼 북한산 국립공원이나 여의도 한강공원, 낙산공원, 인왕산 등이 있는데 마음에 드시...<br>...|[관광-종류-공원, 관광-경치 좋은-yes]<br>[]<br>[관광-종류-공원, 관광-지역-dontcare, 관광-경치 좋은-yes]<br>[]<br>...|
  |10|wos-v1_train_01173|식당<br>숙소|user<br>sys<br>user<br>sys<br>...|친구가 오랜만에 서울에 와서 한식당을 가고 싶다는데 저렴한 곳이 있을까요?<br>지역은 어디가 좋을까요?<br>숙소도 찾아야 하니까 숙소랑 식당이랑 가까이 있으면 좋겠어요.<br>숙소에 대한 조건은 없으시구요?<br>...|[식당-가격대-저렴, 식당-종류-한식당]<br>[]<br>[식당-가격대-저렴, 식당-종류-한식당]<br>[]<br>...|

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
  import tfds_korean.klue_dst

  dataset = tfds.load("klue_dst")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
See also [Copyright notice](https://klue-benchmark.com/tasks/73/overview/copyright).

<style> td {white-space: nowrap;} </style>
