# tfds-korean

A collection of Korean Text Datasets ready to use using Tensorflow-Datasets.

## Registered Datasets

* [`nsmc`](https://github.com/e9t/nsmc)
* [`korsts` & `kornli`](https://github.com/kakaobrain/KorNLUDatasets)
* [`question_pair`](https://github.com/songys/Question_pair)
* [`paraKQC`](https://github.com/warnikchow/paraKQC)

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
