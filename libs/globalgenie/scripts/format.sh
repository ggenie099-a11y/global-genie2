#!/bin/bash

############################################################################
# Format the globalgenie library using ruff
# Usage: ./libs/globalgenie/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting globalgenie"

print_heading "Running: ruff format ${GLOBALGENIE_DIR}"
ruff format ${GLOBALGENIE_DIR}

print_heading "Running: ruff check --select I --fix ${GLOBALGENIE_DIR}"
ruff check --select I --fix ${GLOBALGENIE_DIR}
