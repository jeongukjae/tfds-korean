---
layout: default
title: kmounlp_ner
---

# kmounlp_ner
{: .no_toc }

한국어 개체명 정의 및 표지 표준화 기술보고서와 이를 기반으로 제작된 개체명 형태소 말뭉치.

자세한 정보는 <https://github.com/kmounlp/NER/blob/master/NER%20Guideline%20(ver%201.0).pdf>를 참고하세요.
라이선스는 <https://github.com/kmounlp/NER/blob/master/LICENSE>에서 확인하실 수 있습니다.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/kmounlp_ner/kmounlp_ner.py)
* Version:
  * `1.0.0` (default): Initial release.
* Homepage: <https://github.com/kmounlp/NER>
* Download size: `22.67 MiB`
* Dataset size: `28.81 MiB`
* Features:

  ```python
  FeaturesDict({
      'lemma': Tensor(shape=(None,), dtype=tf.string),
      'named_entity': Tensor(shape=(None,), dtype=tf.string),
      'pos': Tensor(shape=(None,), dtype=tf.string),
      'recognized': Text(shape=(), dtype=tf.string),
      'text': Text(shape=(), dtype=tf.string),
      'tokens': Tensor(shape=(None,), dtype=tf.string),
  })
  ```

* Supervised keys: `None`
* Splits:

  | Split Name | Num Examples        |
  |------------|--------------------:|
  |train  |23964|

* Examples:

  | |text|recognized|tokens|lemma|pos|named_entity|
  |---|---|---|---|---|---|---|
  |1|김건희 교원 대리는 “전용 태블릿PC를 사용해 아이들이 ‘딴짓’ 없이 집중할 수 있어...|&lt;김건희:PER&gt; 교원 대리는 “전용 태블릿PC를 사용해 아이들이 ‘딴짓’...|김건희<br>_<br>교원<br>_<br>...|김건희<br>_<br>교원<br>_<br>...|NNP<br>_<br>NNG<br>_<br>...|B-PER<br>O<br>O<br>O<br>...|
  |2|저수지 주변으로 1km가량 제주올레 13코스가 지난다.|저수지 주변으로 &lt;1km:NOH&gt;가량 &lt;제주올레 13코스:LOC&gt...|저수지<br>_<br>주변<br>으로<br>...|저수지<br>_<br>주변<br>으로<br>...|NNG<br>_<br>NNG<br>JKB<br>...|O<br>O<br>O<br>O<br>...|
  |3|파머는 원칙적으로 윌리엄스의 생각에 동의했다 .|&lt;파머:PER&gt;는 원칙적으로 &lt;윌리엄스:PER&gt;의 생각에 동의했다 .|파머<br>는<br>_<br>원칙적<br>...|파머<br>는<br>_<br>원칙적<br>...|NNP<br>JX<br>_<br>NNG<br>...|B-PER<br>O<br>O<br>O<br>...|
  |4|성완종 리스트 파문이 불거지자 선거전략을 바꾼 것이다.|&lt;성완종 리스트:POH&gt; 파문이 불거지자 선거전략을 바꾼 것이다.|성완종<br>_<br>리스트<br>_<br>...|성완종<br>_<br>리스트<br>_<br>...|NNP<br>_<br>NNG<br>_<br>...|B-POH<br>I-POH<br>I-POH<br>O<br>...|
  |5|신 씨는 그때 현금 5000만 원을 갖고 있었지만 파워보트는 시가 1억 원 정도였다.|&lt;신:PER&gt; 씨는 그때 현금 &lt;5000만 원:MNY&gt;을 갖고 ...|신<br>_<br>씨<br>는<br>...|신<br>_<br>씨<br>는<br>...|NNP<br>_<br>NNB<br>JX<br>...|B-PER<br>O<br>O<br>O<br>...|
  |6|30여평 크기의 아담한 사무실에 직원은 사장까지 합쳐 11명밖에 안된다.|&lt;30여평:NOH&gt; 크기의 아담한 사무실에 직원은 사장까지 합쳐 &lt;1...|30<br>여<br>평<br>_<br>...|30<br>여<br>평<br>_<br>...|SN<br>XSN<br>NNB<br>_<br>...|B-NOH<br>I-NOH<br>I-NOH<br>O<br>...|
  |7|그는 SBS 예능 ‘동상이몽’에 유재석 보조 MC로 출연해 탁월한 진행능력과 끼를 드...|그는 &lt;SBS:ORG&gt; 예능 ‘&lt;동상이몽:POH&gt;’에 &lt;유...|그<br>는<br>_<br>SBS<br>...|그<br>는<br>_<br>SBS<br>...|NP<br>JX<br>_<br>SL<br>...|O<br>O<br>O<br>B-ORG<br>...|
  |8|강 씨는 “아무리 가상공간이라고 하지만 도를 넘어선 언어 성희롱이 판친다”며 “범죄인...|&lt;강:PER&gt; 씨는 “아무리 가상공간이라고 하지만 도를 넘어선 언어 성희롱...|강<br>_<br>씨<br>는<br>...|강<br>_<br>씨<br>는<br>...|NNP<br>_<br>NNB<br>JX<br>...|B-PER<br>O<br>O<br>O<br>...|
  |9|최근 손예진의 ‘비밀은 없다’와 김혜수의 ‘굿바이 싱글’이 연이어 개봉해 여배우의 활...|최근 &lt;손예진:PER&gt;의 ‘&lt;비밀은 없다:POH&gt;’와 &lt;김...|최근<br>_<br>손예진<br>의<br>...|최근<br>_<br>손예진<br>의<br>...|NNG<br>_<br>NNP<br>JKG<br>...|O<br>O<br>B-PER<br>O<br>...|
  |10|경륜훈련원 MTB코스는 국내 최초 MTB 전용코스로 한국산악자전거연맹 공인 1등급 코스다.|경륜훈련원 MTB코스는 국내 최초 MTB 전용코스로 &lt;한국산악자전거연맹:ORG&...|경륜<br>훈련원<br>_<br>MTB<br>...|경륜<br>훈련원<br>_<br>MTB<br>...|NNG<br>NNG<br>_<br>SL<br>...|O<br>O<br>O<br>O<br>...|

* Citation:

  ```text
  @misc{kmounlpner19
      title={Kmounlp NER},
      author={Min-Ah Cheon and Jae-Hoon Kim},
      howpublished={https://github.com/kmounlp/NER},
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
  import tfds_korean.kmounlp_ner

  dataset = tfds.load("kmounlp_ner")
  ```

## License

```
NER License

DO NOT use this dataset for commercial use.
MIT License for non-commercial use.

---------------------------------------------------------------------------------

MIT License

Copyright (c) 2019 한국해양대학교 자연언어처리연구실

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

<style> td {white-space: nowrap;} </style>
