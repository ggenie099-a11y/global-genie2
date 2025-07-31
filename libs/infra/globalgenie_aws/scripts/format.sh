#!/bin/bash

############################################################################
# Format the globalgenie_aws library using ruff
# Usage: ./libs/infra/globalgenie_aws/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_AWS_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting globalgenie_aws"

print_heading "Running: ruff format ${GLOBALGENIE_AWS_DIR}"
ruff format ${GLOBALGENIE_AWS_DIR}

print_heading "Running: ruff check --select I --fix ${GLOBALGENIE_AWS_DIR}"
ruff check --select I --fix ${GLOBALGENIE_AWS_DIR}
