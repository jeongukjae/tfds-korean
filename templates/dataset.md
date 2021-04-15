---
layout: default
title: {{ name }}
---

# {{ name }}
{: .no_toc }

{{ description | safe }}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Dataset Informations

* [See codes in GitHub](https://github.com/jeongukjae/tfds-korean/blob/main/tfds_korean/{{name}}/{{name}}.py)
* Version:{% for note in release_notes %}
  * `{{ note[0] }}` {{ version == note[0] and '(default)' }}: {{ note[1] }}{% endfor %}
* Homepage: <{{ homepage }}>
* Download size: `{{ download_size }}`
* Dataset size: `{{ dataset_size }}`
* Features:

  ```python{% set feature_lines = features.split('\n') %}{% for line in feature_lines %}
  {{ line }}{% endfor %}
  ```

* Supervised keys: `{{ supervised_keys }}`
* Splits:

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|{% for l in splits %}
  |{{ l[0] }}  |{{l[1].num_examples}}|{{l[1].num_shards}}|{% endfor %}

* Examples:

  | |{%for col in examples['columns'] %}{{col}}|{% endfor %}
  |---|{%for col in examples['columns'] %}---|{% endfor %}{% for row in examples['rows'] %}
  |{{loop.index}}|{% for cell in row %}{{cell}}|{% endfor %}{% endfor %}

* Citation:

  ```text{% set citation_lines = citation.split('\n') %}{% for line in citation_lines %}
  {{ line }}{% endfor %}
  ```

## How to use this dataset

* Installation:

  ```sh
  pip install tfds-korean
  ```

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.{{ name }}

  dataset = tfds.load("{{ name }}")
  ```
