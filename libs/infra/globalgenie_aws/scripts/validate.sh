#!/bin/bash

############################################################################
# Validate the globalgenie_aws library using ruff and mypy
# Usage: ./libs/infra/globalgenie_aws/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_AWS_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating globalgenie_aws"

print_heading "Running: ruff check ${GLOBALGENIE_AWS_DIR}"
ruff check ${GLOBALGENIE_AWS_DIR}

print_heading "Running: mypy ${GLOBALGENIE_AWS_DIR} --config-file ${GLOBALGENIE_AWS_DIR}/pyproject.toml"
mypy ${GLOBALGENIE_AWS_DIR} --config-file ${GLOBALGENIE_AWS_DIR}/pyproject.toml
