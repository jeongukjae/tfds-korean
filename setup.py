from setuptools import find_packages, setup

_REQUIRES = [
    "tensorflow-datasets",
]

setup(
    name="tfds-korean",
    version="0.0.1a2",
    author="Ukjae Jeong",
    author_email="jeongukjae@gmail.com",
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
