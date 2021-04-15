# tfds-korean

A collection of Korean Text Datasets ready to use using Tensorflow-Datasets.

[**documentation**](https://jeongukjae.github.io/tfds-korean) | [**pypi**](https://pypi.org/project/tfds-korean/)

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

## Licenses

The license for this repository and licenses for datasets are applied separately. It is recommended to use each dataset after checking the dataset's website.
