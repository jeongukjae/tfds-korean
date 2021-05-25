# CONTRIBUTING

이 파일은 tfds-korean과 관련된 개발 방법을 설명하는 문서입니다.

## 데이터셋을 추가하는 법

[tfds cli](https://www.tensorflow.org/datasets/cli)를 활용합니다. 새로운 데이터셋을 추가할 때는 [tfds cli - implementing a new dataset](https://www.tensorflow.org/datasets/cli#tfds_new_implementing_a_new_dataset)을 참고하시면 됩니다.

1. `cd tfds_korean; tfds new DATASET_NAME`
2. 데이터셋 관련 코드 구현
3. `tfds build tfds_korean/DATASET_NAME --register_checksums`

데이터셋 문서 페이지는 직접 빌드하지 않으셔도 됩니다.

## 코드 스타일

미리 세팅된 black, isort, flake8을 따라 코드 스타일을 맞추어 주시면 됩니다. 최신버전을 따라가는 것을 기본으로 하며, 아래 명령어로 확인합니다.

```sh
flake8 tfds_korean setup.py run_test.py
black --check tfds_korean setup.py run_test.py
isort --check tfds_korean setup.py run_test.py
```

## 아이디어 공유/데이터셋 추가 요청

데이터셋 추가 요청은 현재 [이슈](https://github.com/jeongukjae/tfds-korean/issues)로 받고 있습니다. 이슈 템플릿을 활용해 추가해주시면 됩니다.

아이디어 공유는 [discussion 기능](https://github.com/jeongukjae/tfds-korean/discussions)을 활용하고 있습니다. 이슈로 적기 힘든 사항은 간단하게 discussion으로 공유해주시기 바랍니다.
