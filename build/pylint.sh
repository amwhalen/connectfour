#!/bin/bash

## || exit 0 because pylint only exits with 0 if everything is correct
pylint --rcfile=build/pylint.cfg $(find . -maxdepth 1 -name "*.py" -print) connectfour/ > build/logs/pylint.log || exit 0