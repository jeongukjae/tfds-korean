# CONTRIBUTING

이 파일은 tfds-korean과 관련된 개발 방법을 설명하는 문서입니다.

## 이 라이브러리에서 다루는 기능의 범위

이 라이브러리는 최소한의 기능으로 가능한 한국어/힌글 데이터셋을 많이 담고 있는 것이 목표입니다.
이 라이브러리 별도의 기능을 개발하는 일은 거의 없도록 하고 최대한 tensorflow, tensorflow-datasets만의 기능을 활용하여 개발합니다.

추가할 한국어/한글 데이터셋의 범위는 아래와 같이 생각하고 있습니다. (Discussion/Issue로 더 제안해주셔도 무방합니다)

* 한국어, 한글이 포함된 데이터셋 전체 (텍스트, 오디오)
* 다운로드에 제한이 없는 자유롭게 사용이 가능한 데이터셋
  * 상업적 이용과 별도입니다. 최대한 수동 다운로드를 하지 않고 사용 가능한 데이터셋을 최우선으로 지원하려 합니다.
* TensorFlow Datasets에 존재하지 않는 데이터셋

## 아이디어 공유/데이터셋 추가 요청

데이터셋 추가 요청은 현재 [이슈](https://github.com/jeongukjae/tfds-korean/issues)로 받고 있습니다. 이슈 템플릿을 활용해 추가해주시면 됩니다.

아이디어 공유는 [discussion 기능](https://github.com/jeongukjae/tfds-korean/discussions)을 활용하고 있습니다. 이슈로 적기 힘든 사항은 간단하게 discussion으로 공유해주시기 바랍니다.

## 데이터셋을 추가하는 법

[tfds cli](https://www.tensorflow.org/datasets/cli)를 활용합니다. 새로운 데이터셋을 추가할 때는 [tfds cli - implementing a new dataset](https://www.tensorflow.org/datasets/cli#tfds_new_implementing_a_new_dataset)을 참고하시면 됩니다.

1. `cd tfds_korean; tfds new DATASET_NAME`
2. 데이터셋 관련 코드 구현
3. `tfds build tfds_korean/DATASET_NAME --register_checksums`

데이터셋 문서 페이지는 직접 빌드하지 않으셔도 됩니다.

## 개발 시 참고 사항

아래 섹션들과 함께 아래 사항을 참고하여 개발 중입니다.

* GitHub에서 배포되는 데이터셋일 경우 최대한 특정 브랜치를 참고하는 것이 아닌 특정 커밋을 기준으로 다운로드하도록 합니다.
* GitHub과 다른 웹사이트에서 같은 데이터셋이 동시에 배포될 경우 GitHub을 참고하도록 하고 있습니다.
* GitHub이 아닌 여러 사이트에서 배포될 경우 최대한 안정적으로 여겨지는 사이트를 참고하도록 하고 있습니다.

### 코드 스타일

미리 세팅된 black, isort, flake8을 따라 코드 스타일을 맞추어 주시면 됩니다. 최신버전을 따라가는 것을 기본으로 하며, 아래 명령어로 확인합니다.

```sh
flake8 tfds_korean setup.py run_test.py
black --check tfds_korean setup.py run_test.py
isort --check tfds_korean setup.py run_test.py
```

### 테스트 실행

`run_test.py`는 `tfds_korean/` 경로 밑의 import 가능한 테스트들을 import하여 테스트를 실행합니다. 아래 명령어로 실행할 수 있습니다.

```sh
python run_test.py
```

특정 테스트(예시: nsmc)만 실행하고 싶은 경우 아래와 같이 실행할 수 있습니다.

```sh
python -m tfds_korean.nsmc.nsmc_test
```

### 데이터셋 카탈로그

TensorFlow Datasets에서 직접 카탈로그 빌드가 되지 않아 간단한 스크립트를 작성하였습니다.

`templates/` 폴더가 실제 렌더링될 카탈로그 템플릿을 담고 있고, `docs/datasets`가 렌더링될 타겟 디렉토리입니다.
빌드하는 스크립트는 `tfds_korean/build_catalog.py`에 존재합니다.
아래처럼 실행할 수 있습니다.

```sh
python -m tfds_korean.build_catalog
```
