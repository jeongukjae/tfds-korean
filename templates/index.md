---
layout: default
title: Catalog
---

# tfds-korean(`{{version}}`) Catalog

## Usage

* Install using pip: `pip install tfds-korean`
* Download and prepare dataset using tensorflow-datasets

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.nsmc

  for example in tfds.load("nsmc"):
      ...
  ```

* For more details, see [tfds docs(https://www.tensorflow.org/datasets)](https://www.tensorflow.org/datasets).

## All datasets

{% for dataset_name in dataset_names %}* [{{ dataset_name }}](./datasets/{{ dataset_name }}.md)
{% endfor %}

## Licenses

The license for this repository and licenses for datasets are applied separately. It is recommended to use each dataset after checking the dataset's website.
