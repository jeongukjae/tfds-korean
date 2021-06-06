---
layout: default
title: korean_wikipedia_corpus
---

# korean_wikipedia_corpus
{: .no_toc }

한국어 위키백과 말뭉치.

[kss](https://github.com/hyunwoongko/kss)를 사용하여 문장 단위로 분절되어 있는 위키백과 말뭉치입니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/korean_wikipedia_corpus/korean_wikipedia_corpus.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/jeongukjae/korean-wikipedia-corpus>
* Download size: `255.20 MiB`
* Dataset size: `748.35 MiB`
* Features:

  ```python
  FeaturesDict({
      'content': Sequence(Text(shape=(), dtype=tf.string)),
      'title': Text(shape=(), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |1106264|

* Examples:

  | |title|content|
  |---|---|---|
  |1|이태좌|이태좌(李台佐, 1660년 ~ 1739년)는 조선의 문신이다.<br>본관은 경주(慶州). 자는 국언(國彦), 호는 아곡(鵝谷)이다.<br>영조 때 좌의정을 지냈다.<br>이항복의 후손이며, 영의정을 지낸 이광좌의 재종형이다.<br>...|
  |2|자치현|자치현(自治县)은 중화인민공화국의 민족구역자치 행정 체제의 일종이다.<br>2003년 말을 기준으로 전국에 117개의 자치현이 있다.<br>자치구와 자치현의 차이는 명칭뿐이다.|
  |3|편편애상니|《편편애상니》(偏偏爱上你)는 2012년 방송되었던 중국의 드라마이다.|
  |4|전장포항 - 어항구역.|본 항의 어항구역은 다음과 같다.|
  |5|장간회 - 생애.|장간회의 출생 연도에 관해서는 알려져 있지 않다.<br>장윤신에게는 14명의 아들들이 있었는데, 장간회는 그 중의 한 사람이었다.<br>그 외에도 나머지 13명의 아들들 중에서는 오직 유주좌사마(幽州左司馬) 장간진(張簡眞...<br>(정확한 사망 연도는 불명)<br>...|
  |6|아칸소주 - 광업.|천연가스는 아칸소주의 지도적인 광물이며, 석유는 그 다음이다.<br>주의 천연가스는 거의 아코마 분지에서 찾아진다.<br>그 분지는 아칸소주의 서부로부터 오클라호마주로 들어가 뻗어있다.<br>아칸소주의 가장 큰 유전들은 남부 경계의 근처에 놓여있다.<br>...|
  |7|초용 - 강충원의 죽음.|1853년 6월, 강충원은 안휘순무가 되었다.<br>10월, 태평천국군은 남창의 포위를 풀고 서정을 시작했다.<br>강충원은 호북성의 전가진(田家鎭)에서 전투를 벌였지만, 패배를 당하고 무한으로 물러났다.<br>같은 해 12월, 여주를 지키려고 싸웠지만, 후이황이 이끄는 태평천국군에게 포위당했다.<br>1854년 1월 14일, 군량은 부족했고, 원군이 오지 않자 결국 성이 함락당했고, ...|
  |8|충신사|충신사는 충청북도 청주시 서원구에 있다.<br>2015년 4월 17일 청주시의 향토유적 제59호로 지정되었다.|
  |9|미케타|미케타 (Michetta 또는 rosetta)는 이탈리아의 흰색 빵으로 봉긋하게 부풀...<br>비슷한 빵으로는 마기올리노나 타르타루가가 있다.<br>북부 이탈리아의 롬바르디아주에서 오스트리아 지배 당시 유래했다.<br>오스트리아 제국의 사람들이 작은 장미를 닮은 카이저 롤을 가져왔던 것이 변형된 것이다.<br>...|
  |10|팀 제닉스 - 리그 오브 레전드.|2012년 2월 22일 제닉스는 리그 오브 레전드 팀을 창단, 팀 명칭을 제닉스 스톰...<br>2013년 2월 13일 기존의 제닉스 스톰 감독이었던 홍진호가 프론트로 자리를 옮겼으...<br>2013년 6월 기존 팀의 맴버 변경과 더불어 2팀 체제를 확립, 제닉스 블라스트(X...<br>기존 제닉스 리그 오브 레전드 팀은 PSKR이라는 업체에서 운영하고 제닉스는 네이밍 ...<br>이와 동시에 제닉스 블라스트의 멤버로 아마추어 팀 Midas FIO를 영입하여 Mid...|

* Citation:

  ```text
  @misc{korean_wikipedia_corpus21
      title={Korean Wikipedia Corpus},
      author={Ukjae Jeong},
      howpublished={https://github.com/jeongukjae/korean-wikipedia-corpus},
      year={2021}
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
  import tfds_korean.korean_wikipedia_corpus

  dataset = tfds.load("korean_wikipedia_corpus")
  ```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

<style> td {white-space: nowrap;} </style>
