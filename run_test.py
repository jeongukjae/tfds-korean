import glob
import importlib

import tensorflow_datasets as tfds


def main():
    test_files = [filename[:-3].replace("/", ".") for filename in glob.glob("tfds_korean/**/*_test.py")]
    for test_file in test_files:
        module = importlib.import_module(test_file)
        for name in dir(module):
            if name.endswith("Test"):
                globals().update({name: getattr(module, name)})

    tfds.testing.test_main()


if __name__ == "__main__":
    main()
