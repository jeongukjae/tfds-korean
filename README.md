# tfds-korean

A collection of Korean Text Datasets ready to use using Tensorflow-Datasets.

## Registered Datasets

* [`nsmc`](https://github.com/e9t/nsmc)
* [`korsts` & `kornli`](https://github.com/kakaobrain/KorNLUDatasets)
* [`question_pair`](https://github.com/songys/Question_pair)
* [`para_kqc`](https://github.com/warnikchow/paraKQC)
* [`korean_hate_speech/labeled`, `korean_hate_speech/unlabeled`](https://github.com/kocohub/korean-hate-speech)
* [`korean_chatbot_qa_data`](https://github.com/songys/Chatbot_data)

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
