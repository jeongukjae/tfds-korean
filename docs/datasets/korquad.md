---
layout: default
title: korquad
---

# korquad
{: .no_toc }

The Korean Question Answering Dataset

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/korquad/korquad.py)
* Version:
* Homepage: <https://korquad.github.io/KorQuad%201.0/>
* Citation:

  ```text
  @@misc{lim2019korquad10,
        title={KorQuAD1.0: Korean QA Dataset for Machine Reading Comprehension},
        author={Seungyoung Lim and Myungji Kim and Jooyoul Lee},
        year={2019},
        eprint={1909.07005},
        archivePrefix={arXiv},
        primaryClass={cs.CL}
  }
  ```

## Configs


### korquad/1.0 (default)

KorQuAD 1.0

KorQuAD 1.0은 한국어 Machine Reading Comprehension을 위해 만든 데이터셋입니다.
모든 질의에 대한 답변은 해당 Wikipedia article 문단의 일부 하위 영역으로 이루어집니다.
Stanford Question Answering Dataset(SQuAD) v1.0과 동일한 방식으로 구성되었습니다.

* Dataset size: `93.33 MiB`
* Download size: `40.44 MiB`
* Features:

  ```python
  FeaturesDict({
      'answers': Sequence({
          'answer_start': tf.int64,
          'text': Text(shape=(), dtype=tf.string),
      }),
      'context': Text(shape=(), dtype=tf.string),
      'qa_id': Text(shape=(), dtype=tf.string),
      'question': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |60407|
  |dev  |5774|

* Examples:

  | |answers/answer_start|answers/text|context|qa_id|question|title|
  |---|---|---|---|---|---|---|
  |1|[222]|2명|세계 무역 센터 부지의 구조대원은 테러 하루 후 11편에 있었던 승객의 시신 일부를 ...|6533620-7-1|세계 무역 센터 테러 발생 후 2006년에 추가로 발견된 희생자 시신은 몇 명인가?|아메리칸_항공_11편_테러_사건|
  |2|[386]|원추 세포|돌연변이의 대표적인 사례로는 유전자 중복이 있다. 동물의 경우 매 천 년당 한 번 꼴...|6557516-5-2|눈의 망막은 어떤 유전자 중의 하나가 중복 이상을 일으켜 정상적인 기능을 할 수 없어...|진화|
  |3|[660]|14개|부산과 대구는 자체적으로 타당성 조사를 실시했다. 이 보고서에 따르면 두 지자체 모두...|6524243-2-2|2011년 기준으로 한국공항공사가 운영하는 공항은 몇 개인가?|영남권_신공항|
  |4|[83]|대기업|대한민국은 자본력이 부족한 환경에 따라 독특한 형태의 경제발전을 진행시켜 왔는데, 박...|6490879-26-0|박정희 정부 당시 계획경제체제를 시행하기 위해 축으로 세운 기업형태는?|대한민국|
  |5|[18]|프렌즈 위드 베네핏|2011년에는 윌 글럭 감독의 《프렌즈 위드 베네핏》에서 저스틴 팀버레이크와 밀라 쿠...|6458263-5-0|크레이지, 스투피드, 러브와  같은 연도에 개봉한 영화는?|엠마_스톤|
  |6|[158]|2016년|2015년에는 코스닥 상장회사인 (주)루보를 인수하였으며 사명을 (주)썬코어로 변경하...|6560008-0-1|썬테크노로지스의 대표이사가 된 해는?|최규선|
  |7|[342]|소극살합|당시 대신들은 순치제에게 빨리 돌아오라 종용하였으나 순치제는 끝내 듣지 않고 머리카락...|6486899-5-1|순치제 붕어 당시 형부상서는?|강희제|
  |8|[398]|임중경|2016년 12월 말, 한효주는 다음 작품으로 일본 작가 이사카 코타로의 동명 소설을...|6570191-10-2|영화 인랑에서 한효주가 마음에 동요를 일으키는 극중 인물은?|한효주|
  |9|[321]|메르센 조약|869년 로타르는 교황과의 접견을 통해 이혼에 대한 긍정적인 답변을 듣고 귀환하는 중...|6497078-7-2|로타르 2세가 사망한 후 로타르 2세의 삼촌들은 어떤 조약으로 로타르 2세의 영토를 ...|로타리우스_2세|
  |10|[148]|포토제니|프랑스의 루이 델뤼크(1890-1924)는 젊은 저널리스트 문학자였으며, 카뉴도의 영...|6541198-1-2|델뤼크는 영화의 영상이 단순한 사진적 의미가 아니라 유기적 내재성을 주장한다고 하며 ...|영화_이론|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.korquad
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("korquad/1.0")
  ```


### korquad/2.1 

KorQuAD 2.1

KorQuAD 2.1은 KorQuAD 1.0에서 질문답변 20,000+ 쌍을 포함하여 총 100,000+ 쌍으로 구성된 한국어 Machine Reading Comprehension 데이터셋 입니다.
KorQuAD 1.0과는 다르게 1~2 문단이 아닌 Wikipedia article 전체에서 답을 찾아야 합니다. 매우 긴 문서들이 있기 때문에 탐색 시간에 대한 고려가 필요할 것 입니다.
또한 표와 리스트도 포함되어 있기 때문에 HTML tag를 통한 문서의 구조 이해도 필요합니다.
이 데이터셋을 통해서 다양한 형태와 길이의 문서들에서도 기계독해가 가능해질 것 입니다.

* Dataset size: `18.90 GiB`
* Download size: `1.28 GiB`
* Features:

  ```python
  FeaturesDict({
      'answer': FeaturesDict({
          'answer_start': tf.int64,
          'html_answer_start': tf.int64,
          'html_answer_text': Text(shape=(), dtype=tf.string),
          'text': Text(shape=(), dtype=tf.string),
      }),
      'context': Text(shape=(), dtype=tf.string),
      'qa_id': Text(shape=(), dtype=tf.string),
      'question': Text(shape=(), dtype=tf.string),
      'raw_html': Text(shape=(), dtype=tf.string),
      'title': Text(shape=(), dtype=tf.string),
      'url': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |83486|
  |dev  |10165|

* Examples:

  | |answer/answer_start|answer/html_answer_start|answer/html_answer_text|answer/text|context|qa_id|question|raw_html|title|url|
  |---|---|---|---|---|---|---|---|---|---|---|
  |1|2794|14187|&lt;a href="/wiki/%EB%8F%85%EC%9D%BC_%EC%97%AC%...|&lt;a&gt;독일&lt;/a&gt;|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|16399|2019년 FIFA 여자 월드컵 유럽 지역 예선전에서 1위를 차지한 팀은 어디인가요?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|2019년_FIFA_여자_월드컵_유럽_지역_예선|https://ko.wikipedia.org/wiki/2019년_FIFA_여자_월드컵...|
  |2|3763|18751|&lt;p&gt;영화는 1992년 가을에 &lt;a href="/wiki/%EA%B7...|&lt;p&gt;영화는 1992년 가을에 &lt;a&gt;그리니치빌리지&lt;/a&g...|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|1680|맨해튼 미스터리가 촬영되었을 때 촬영장의 상황은 어땠을까?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|맨해튼_미스터리|https://ko.wikipedia.org/wiki/맨해튼_미스터리|
  |3|11817|41953|15명|15명|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|103740|2012년 신인 드래프트에서 지명된 선수는 몇 명인가?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|NC_다이노스|https://ko.wikipedia.org/wiki/NC_다이노스|
  |4|5592|19741|&lt;td&gt;&lt;a href="/wiki/%EC%8B%A0%ED%95%9C%...|&lt;td&gt;&lt;a&gt;신한민주당&lt;/a&gt;&lt;/td&gt;|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|17307|유성환이 제12대 총선에 출마하였을 때 소속되어 있던 정당의 이름은 무엇인가?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|유성환|https://ko.wikipedia.org/wiki/유성환|
  |5|7445|21851|&lt;table class="wikitable"&gt;<br>&lt;tbody&gt...|&lt;table&gt;<br>&lt;tbody&gt;&lt;tr&gt;<br>&lt...|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|27051|거북이 특공대 Z의 시즌2 미국판과 한국판의 제목을 비교한 목록은 어떠한가요?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|거북이_특공대_Z|https://ko.wikipedia.org/wiki/거북이_특공대_Z|
  |6|2051|11998|&lt;a href="/wiki/%EB%A6%AC%ED%95%98%EB%A5%B4%E...|&lt;a&gt;리하르트 바그너&lt;/a&gt;|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|73873|로엘그린의 작곡자는 누구일까?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|뮌헨_오페라_페스티벌|https://ko.wikipedia.org/wiki/뮌헨_오페라_페스티벌|
  |7|3101|19037|&lt;p&gt;&lt;a href="/wiki/%ED%94%84%EB%9E%91%E...|&lt;p&gt;&lt;a&gt;프랑스&lt;/a&gt;에서 처음 생긴 국민보수주의는...|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|70594|국민보수주의의 개요는?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|국민보수주의|https://ko.wikipedia.org/wiki/국민보수주의|
  |8|3603|19916|&lt;a href="/wiki/%EC%A1%B0%EC%88%AD" title="조숭...|&lt;a&gt;조숭&lt;/a&gt;|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|67082|조조의 부친의 이름은 뭐야?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|조조의_서주_침공|https://ko.wikipedia.org/wiki/조조의_서주_침공|
  |9|5736|22710|약 100 AU|약 100 AU|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|90112|발견 당일, 세드나가 이동했다고 추측되는 거리는?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|90377_세드나|https://ko.wikipedia.org/wiki/90377_세드나|
  |10|10951|33791|2개|2개|&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;he...|94654|샘프러스는 총 몇 개의 호주 오픈 타이틀을 획득하였는가?|&lt;!DOCTYPE html&gt;<br>&lt;html class="client...|피트_샘프러스|https://ko.wikipedia.org/wiki/피트_샘프러스|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.korquad
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("korquad/2.1")
  ```



## License

* KorQuAD 2.0의 데이터셋은 [CC BY-ND 2.0 KR 라이센스](https://creativecommons.org/licenses/by-nd/2.0/kr/)를 따릅니다.
* KorQuAD 1.0의 데이터셋은 [CC BY-ND 2.0 KR 라이센스](https://creativecommons.org/licenses/by-nd/2.0/kr/)를 따릅니다.

<style> td {white-space: nowrap;} </style>
