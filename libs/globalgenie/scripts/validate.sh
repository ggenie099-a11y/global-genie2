#!/bin/bash

############################################################################
# Validate the globalgenie library using ruff and mypy
# Usage: ./libs/globalgenie/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating globalgenie"

print_heading "Running: ruff check ${GLOBALGENIE_DIR}"
ruff check ${GLOBALGENIE_DIR}

print_heading "Running: mypy ${GLOBALGENIE_DIR} --config-file ${GLOBALGENIE_DIR}/pyproject.toml"
mypy ${GLOBALGENIE_DIR} --config-file ${GLOBALGENIE_DIR}/pyproject.toml
