# tfds-korean

A collection of Korean Text Datasets ready to use using [Tensorflow-Datasets](https://github.com/tensorflow/datasets).

[TensorFlow-Datasets](https://github.com/tensorflow/datasets)를 이용한 한국어/한글 데이터셋 모음입니다.

[**Dataset Catalog**](https://jeongukjae.github.io/tfds-korean) | [**pypi**](https://pypi.org/project/tfds-korean/) | [**CONTRIBUTING.md**](./CONTRIBUTING.md)

![PyPI - License](https://img.shields.io/pypi/l/tfds-korean)
![PyPI](https://img.shields.io/pypi/v/tfds-korean)
[![Test Python](https://github.com/jeongukjae/tfds-korean/actions/workflows/test-python.yml/badge.svg)](https://github.com/jeongukjae/tfds-korean/actions/workflows/test-python.yml)

## Usage

### Installation

```sh
pip install tfds-korean
```

### Loading dataset

```python
import tensorflow_datasets as tfds
import tfds_korean.nsmc # register nsmc dataset

ds = tfds.load('nsmc')

train_ds = ds['train'].batch(32)
test_ds = ds['test'].batch(128)

# define model
# ....
# ....

model.fit(train_ds)
model.evaluate(test_ds)
```

See [Dataset Catalog page](https://jeongukjae.github.io/tfds-korean) for dataset list and details of each dataset.

## Examples

* [Loading NSMC dataset](./examples/nsmc_loading_datasets.ipynb)
* [Training a classifier using Korean hate speech dataset](./examples/korean_hate_speech_lstm.ipynb)

## Licenses

The license for this repository and licenses for datasets are applied separately. It is recommended to use each dataset after checking the dataset's website.

본 레포지토리의 라이선스와 데이터셋의 라이선스는 별도로 적용됩니다. 데이터셋을 사용하기 전 각 데이터셋의 라이선스와 웹 사이트를 확인 후 사용하시길 권해드리며, 본 라이브러리는 데이터셋을 호스팅하거나 배포하지 않는 점을 참고부탁드립니다.
