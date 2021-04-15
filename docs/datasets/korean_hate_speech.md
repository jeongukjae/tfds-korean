---
layout: default
title: korean_hate_speech
---

# korean_hate_speech
{: .no_toc }

The human-annotated Korean corpus for toxic speech detection and the large unlabeled corpus.
The data is comments from the Korean entertainment news aggregation platform.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/korean_hate_speech/korean_hate_speech.py)
* Version:
* Homepage: <https://github.com/kocohub/korean-hate-speech>
* Citation:

  ```text
  @inproceedings{moon-etal-2020-beep,
      title = "{BEEP}! {K}orean Corpus of Online News Comments for Toxic Speech Detection",
      author = "Moon, Jihyung  and
        Cho, Won Ik  and
        Lee, Junbum",
      booktitle = "Proceedings of the Eighth International Workshop on Natural Language Processing for Social Media",
      month = jul,
      year = "2020",
      address = "Online",
      publisher = "Association for Computational Linguistics",
      url = "https://www.aclweb.org/anthology/2020.socialnlp-1.4",
      pages = "25--31",
      abstract = "Toxic comments in online platforms are an unavoidable social issue under the cloak of anonymity. Hate speech detection has been actively done for languages such as English, German, or Italian, where manually labeled corpus has been released. In this work, we first present 9.4K manually labeled entertainment news comments for identifying Korean toxic speech, collected from a widely used online news platform in Korea. The comments are annotated regarding social bias and hate speech since both aspects are correlated. The inter-annotator agreement Krippendorff{'}s alpha score is 0.492 and 0.496, respectively. We provide benchmarks using CharCNN, BiLSTM, and BERT, where BERT achieves the highest score on all tasks. The models generally display better performance on bias identification, since the hate speech detection is a more subjective issue. Additionally, when BERT is trained with bias label for hate speech detection, the prediction score increases, implying that bias and hate are intertwined. We make our dataset publicly available and open competitions with the corpus and benchmarks.",
  }
  ```

## Configs


### korean_hate_speech/labeled (default)

Korean hate speech dataset (labeled)

* Dataset size: `2.58 MiB`
* Download size: `1.85 MiB`
* Features:

  ```python
  FeaturesDict({
      'bias': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
      'comments': Text(shape=(), dtype=tf.string),
      'contain_gender_bias': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
      'hate': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
      'news_title': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|
  |train  |7896|1|
  |dev  |471|1|
  |test  |974|1|

* Examples:

  | |bias|comments|contain_gender_bias|hate|news_title|
  |---|---|---|---|---|---|
  |1|0|솔약국 다모인건 정말 대박이다|0|0|손현주, 이필모♥서수연 결혼식 사회 인증 “다시 뭉친 ‘솔약국집 아들들’”|
  |2|0|존예고만 어디가 안예뻐;;;|0|0|[배틀트립] “맛있어? 그럼 내가 다 사줄게” 아이 멘트에 감동하는 ‘모델’ 이현이-...|
  |3|0|그래도 김용진|0|0|[DA:리뷰] ‘복면가왕’ 독수리건, 新가왕 등극…왕밤빵 정체=뮤지 (종합)|
  |4|1|혜교가 한남자로 만족을 못하는듯..혜교는 작품 할때마다 연애하는게 맞는거 같네..중기...|1|1|'섹션TV' 송중기·송혜교, 합의이혼 아닌 이혼조정신청 택한 이유|
  |5|0|나은?인가 쟤는 진짜 이쁜데 건후 쟤는 솔직히 진짜 못생김|0|2|[종합] 박주호 부부, 셋째 출산…‘슈돌’ 측 “함께 방송하길 기대”|
  |6|0|피해자들이 보면 얼마나 가슴아플까요 굳이 올리는건..|0|0|[종합] 故 조민기 아내, 생일 축하 게시글에 갑론을박…"가족"VS"경솔"|
  |7|1|방금 구글에서 카톡내용 일부 보고왔는데 ,저 내용이 사실이라면 뭐랄까 김건모는 직업여...|1|2|[전문] 삼성전자 “주진모 해킹 피해 우리 문제 아냐…계정 외부유출 추정” (공식입장)|
  |8|1|조재현씨 웅원합니다 끝까지 무고죄 파헤쳐서 승소하기 바랍니다 -- 꼴페미년들의 인민 ...|1|1|[Oh!쎈 이슈] '한밤' 조재현 측 "다시 연예계 복귀 생각 無…A씨, 성폭행 아닌...|
  |9|0|솔직히 여자 멋지긴하다.마인드가.|0|0|[종합S] 유상무 "♥김연지, 나만 보는 사람…내가 잘할게"|
  |10|0|부인이 참 이쁘네|0|0|[종합S] 유상무 "♥김연지, 나만 보는 사람…내가 잘할게"|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.korean_hate_speech
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("korean_hate_speech/labeled")
  ```


### korean_hate_speech/unlabeled

Korean hate speech dataset (unlabeled)

* Dataset size: `481.82 MiB`
* Download size: `408.99 MiB`
* Features:

  ```python
  FeaturesDict({
      'comments': Text(shape=(), dtype=tf.string),
      'news_title': Text(shape=(), dtype=tf.string),
  })
  ```

* Splits:

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|
  |train  |2033893|8|

* Examples:

  | |comments|news_title|
  |---|---|---|
  |1|개존잼.|'SKY캐슬' 염정아, 김서형에 무릎 꿇고 오열 "비극 다 감수하겠다"(종합)|
  |2|박선영 역활이지만 꼴배기 싫었음. 그러는 지는 연하 미친 작가 무슨생각으로 글쓰냐.|'같이 살래요' 박선영, 유동근에 "지금처럼 혼자 살아달라" (종합)|
  |3|임시완빼내오고싶어속터지는줄 ㅠㅠ 웹툰안본사람이라 더기대되네요|'타인은 지옥이다' 임시완, 에덴고시원 정착…이중옥·박종환 이상행동에 '의심' [종합]|
  |4|열혈사제2 부탁드립니다|'열혈사제' 김남길, 흑화를 응원하게 되는 이유 "소중한 사람들 지킨다"|
  |5|유이 ㅋㅋㅋ 우는데 저리 공감안되게 안슬픈것도 처음이다|'하나뿐인 내편' 윤진이 "박성훈♥나혜미 결혼 절대 안돼"|
  |6|이쁜데.|구하라, 안검하수 수술 후 근황 공개…또렷해진 눈매|
  |7|클린봇이 부적절한 표현을 감지한 댓글입니다.|방탄소년단, 내일(24일) 글로벌 기자간담회 생중계 대체 "정부의 코로나19 대응 협...|
  |8|진짜 소속사가 아무것도 안하는듯... 아니 정산을 얼마를 받았는지 확실한것도 아닌 추...|[SC이슈] "멤버당 3억?"...워너원, 정산의 모든 것 (종합)|
  |9|미모가 피기 시작했네. 심은하 비슷하다.|[55회 백상] 'SKY 캐슬' 김혜윤, 신인상 수상 "잊지 못할 행복한 추억" 울컥|
  |10|애한테 폰많이 쥐어주는 맘충들이 드글드글~~ 저 언니 아는척 공감대놀이 할때가아니야 ...|'초통령' 헤이지니 "3년 교제 남자친구와 결혼…예쁘게 살게요" 깜짝 발표 [종합]|

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.korean_hate_speech
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("korean_hate_speech/unlabeled")
  ```
