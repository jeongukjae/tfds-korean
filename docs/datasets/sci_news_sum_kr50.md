---
layout: default
title: sci_news_sum_kr50
---

# sci_news_sum_kr50
{: .no_toc }

네이버 뉴스 중 IT/과학 분야에서 50개를 선정해서 요약에 해당하는 문장을 태깅해둔 데이터셋입니다.
파일 한개당 뉴스 하나를 뜻하며, 원본 출처가 기록되어 있습니다. 비상업적인 실험에만 사용해주세요.

summaries가 sentences 중 요약에 해당하는 문장의 index입니다. 이걸 정답셋으로 사용하시면 됩니다.

자세한 정보는 <https://github.com/theeluwin/sci-news-sum-kr-50>를 참고하세요.
라이선스는 <https://github.com/theeluwin/sci-news-sum-kr-50/blob/master/LICENSE>에서 확인하실 수 있습니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/sci_news_sum_kr50/sci_news_sum_kr50.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/theeluwin/sci-news-sum-kr-50>
* Download size: `159.89 KiB`
* Dataset size: `158.73 KiB`
* Features:

  ```python
  FeaturesDict({
      'length': tf.int32,
      'sentences': Tensor(shape=(None,), dtype=tf.string),
      'slug': Text(shape=(), dtype=tf.string),
      'source': Text(shape=(), dtype=tf.string),
      'summaries': Tensor(shape=(None,), dtype=tf.int32),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |dev  |50|

* Examples:

  | |title|summaries|sentences|source|slug|length|
  |---|---|---|---|---|---|---|
  |1|NASA vs 스페이스X “화성 땅 첫 발자국 우리가 먼저”|1<br>2<br>4<br>6<br>...|화성 유인탐사 경쟁 후끈<br>1969년 인류가 달에 첫발을 내디딘 후, 사람들은 다음 목표로 화성을 주목해 왔다<br>47년이 흐른 지금, 40대 이상의 무인 우주선이 화성으로 떠났지만 아직 인류의 발자...<br>인류는 언제쯤 화성에 도착할 수 있을까<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|nasa-vs-seupeiseux-hwaseong-ddang-ceos-baljagug...|40|
  |2|헬리콥터를 개조해 만든 경주용차|6<br>10<br>17|- 기어 조작은 베트남 전쟁 당시 기관총 조작에 쓰였던 조종간이다<br>- 배기량 3리터, 출력 210 마력의 엔진은 부서진 2002년형 아우디 V6 엔진에...<br>엔진 가격은 450달러<br>- 폰툰은 1988년형 선 트래커 보트에서 가져왔고, 강철로 보강했다<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|helrikobteoreul-gaejohae-mandeun-gyeongjuyongca|24|
  |3|'도구의 인간'...도구의 원숭이도 있다|0<br>9<br>10<br>12<br>...|인류가 오늘날 지능을 갖게 된 것은 도구를 이용하면서부터다<br>손을 이용해 복잡한 도구를 만들면서 인간 뇌 용량이 점점 커졌고 복잡한 사고까지 할 ...<br>인류 역사가 도구와 함께 발전한 점을 강조하는 ‘호보파베르(도구의 인간)’란 말이 나...<br>지구에 사는 모든 생물종을 통틀어 도구를 사용하는 동물은 많지 않다<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|doguyi-ingan-doguyi-weonsungido-issda|23|
  |4|[과학 핫이슈]투명망토 현실화할 `메타물질`|9<br>12<br>13<br>14<br>...|소리를 통과시키는 음향 투명망토가 개발됐다<br>콘서트 홀 중간 중간에 위치한 기둥에 음향 투명망토를 코팅해 놓으면 마치 기둥이 없는...<br>멀리서도 더 웅장한 소리를 들을 수 있게 된다<br>기존에는 기둥에 소리가 부딪쳐 막혔다<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|gwahag-hasisyu-tumyeongmangto-hyeonsilhwahal-me...|42|
  |5|'리튬이온 전지보다 100배 빨리 충전'…새 배터리 개발|1<br>2<br>6|KAIST 강정구 교수팀 특급 논문 게재…"전기차 등에 핵심 기술 전망"<br>IT(정보기술) 기기와 전기차에 널리 쓰이는 리튬이온 배터리보다 최대 100배 더 빠...<br>미래창조과학부는 한국과학기술원(KAIST) 신소재공학과 강정구 교수팀이 이런 '하이브...<br>리튬이온 배터리는 전기를 많이 저장할 수 있어 스마트폰·노트북·전기차 등에 많이 쓰이...<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|rityumion-jeonjiboda-100bae-bbalri-cungjeon-sae...|9|
  |6|흡연로봇 나왔다…용도는?|1<br>2<br>4<br>10|만성 폐쇄성 폐질환 연구 목적<br>흡연이 폐에 어떤 영향을 미치는 지 정확히 연구할 수 있는 흡연로봇이 개발돼 주목을 ...<br>미국 하버드 대학 위스 응용 생물학 공학 연구소(Wyss Institute for B...<br>이를 통해 연구진은 만성 폐쇄성 폐질환(COPD)과 전자담배에 대한 이해가 깊어질 수...<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|heubyeonrobos-nawassda-yongdoneun|11|
  |7|[과학을 읽다]폐암 조기진단 가능해진다|0<br>2<br>3<br>8<br>...|국내 연구팀, 특정 단백질 증가 현상 찾아내…폐암 조기 진단 키트·신약 개발 기대<br>정상폐와 폐암에서의 USE1의 조절 메커니즘<br>[아시아경제 정종오 기자] 폐암을 조기에 진단할 수 있는 생화학 마커를 국내 연구팀이...<br>폐암환자의 92.5%에서 'USE1' 단백질이 증가돼 있고 이중 13%에서는 USE1...<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|gwahageul-ilgda-pyeam-jogijindan-ganeunghaejinda|23|
  |8|[영화 'Her'의 그녀, 어떻게 인간의 말동무가 되었나] DB따라 음성인식→딥러닝→...|9<br>12<br>16|애플 '시리'·SKT '누구' 등<br>음성인식 기술 활용 잇따라<br>소음속 음성인식 등은 과제<br>아이폰에서 시리(Siri)를 작동시킨 화면<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|yeonghwa-her-yi-geunyeo-eoddeohge-inganyi-maldo...|41|
  |9|"AI 시대엔 노동시간 줄이고 재교육 기회 넓혀야"|2<br>4<br>9|임지선 박사 "자기계발 여가부터 보장돼야 변화 대처 가능"<br>인간의 일자리를 위협하는 인공지능 기술<br>인공지능(AI)이 인간의 일자리를 대거 대체하는 '4차 산업혁명'으로 발생할 수 있는...<br>복잡한 정신노동까지 인간 대신 기계가 하게 되는 이런 시기에 노동자들이 자생력을 키우...<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|ai-sidaeen-nodongsigan-juligo-jaegyoyug-gihoe-n...|11|
  |10|'변이 암세포도 숨을 곳 없다' 새 표적항암제 기술 개발|2<br>4<br>6<br>7|KIST 김영수 박사 유전자 변이로 모습을 바꾼 암세포도 감쪽같이 타격하는 표적항암제...<br>KIST 연구진, 유전자 변이 영향없는 새 표적 단백질 발견<br>유전자 변이로 모습을 바꾼 암세포도 감쪽같이 타격하는 표적항암제를 만들 수 있는 기초...<br>암 치료에서 '마법의 탄환'으로 꼽히지만, 유전자 변이 현상 앞에서는 '오발탄'이 되...<br>...|http://news.naver.com/main/read.nhn?mode=LS2D&m...|byeoni-amsepodo-sumeul-gos-eobsda-sae-pyojeogha...|12|

* Citation:

  ```text
  @misc{scinewssumkr16
      title={sci-news-sum-kr-50},
      author={Jamie J. Seol},
      howpublished={https://github.com/theeluwin/sci-news-sum-kr-50},
      year={2016}
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
  import tfds_korean.sci_news_sum_kr50

  dataset = tfds.load("sci_news_sum_kr50")
  ```

## License

MIT License

<style> td {white-space: nowrap;} </style>
