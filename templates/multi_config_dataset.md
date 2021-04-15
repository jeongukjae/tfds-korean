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
* Citation:

  ```text{% set citation_lines = citation.split('\n') %}{% for line in citation_lines %}
  {{ line }}{% endfor %}
  ```

## Configs

{% for config in configs %}
### {{name}}/{{config.name}} {{ config.name == configs[0].name and '(default)' }}

{{ config.description | safe }}

* Dataset size: `{{ config.dataset_size }}`
* Download size: `{{ config.download_size }}`
* Features:

  ```python{% set feature_lines = config.features.split('\n') %}{% for line in feature_lines %}
  {{ line }}{% endfor %}
  ```

* Splits:

  | Split Name | Num Examples        | Num Shards        |
  |------------|--------------------:|------------------:|{% for l in config.splits %}
  |{{ l[0] }}  |{{l[1].num_examples}}|{{l[1].num_shards}}|{% endfor %}

* Examples:

  | |{%for col in config.examples['columns'] %}{{col}}|{% endfor %}
  |---|{%for col in config.examples['columns'] %}---|{% endfor %}{% for row in config.examples['rows'] %}
  |{{loop.index}}|{% for cell in row %}{{cell}}|{% endfor %}{% endfor %}

* Use this dataset

  ```python
  import tensorflow_datasets as tfds
  import tfds_korean.{{ name }}
  # Install tfds-korean with `pip install tfds-korean`

  dataset = tfds.load("{{ name }}/{{ config.name }}")
  ```

{% endfor %}
