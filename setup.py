import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

_REQUIRES = ["tensorflow-datasets", "tensorflow"]

setup(
    name="tfds-korean",
    version="0.0.1a3",
    author="Ukjae Jeong",
    author_email="jeongukjae@gmail.com",
    description="A collection of Korean Text Datasets ready to use using Tensorflow-Datasets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jeongukjae/tfds-korean",
    install_requires=_REQUIRES,
    keywords=["tensorflow", "machine learning", "dataset"],
    packages=find_packages(),
    include_package_data=True,
    package_data={"tfds_korean": ["*/checksums.tsv"]},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
