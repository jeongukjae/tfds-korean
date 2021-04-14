#!/bin/sh

set -e

TEST_CASES=`find tfds_korean -name "*test.py"`

for test_case in $TEST_CASES ; do
    module_name=`echo $test_case | sed -e 's/\.py$//g' -e 's/\//./g'`

    echo "\n\nRun $test_case ($module_name)\n"
    python -m $module_name
done
