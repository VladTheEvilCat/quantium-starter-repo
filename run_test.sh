#!/bin/bash

# Virtual environment
. ./venv/bin/activate

# Run test suite
python -m pytest test_pink_morsel_visualizer.py

# Get exit code
# 0 if all pass
TEST_EXIT_CODE=$?

# Return exit code 0 if all pass, else 1
if [ $TEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi