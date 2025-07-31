#!/bin/bash

############################################################################
# Format the readygenie using ruff
# Usage: ./libs/globalgenie/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
READYGENIE_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting readygenie"

print_heading "Running: ruff format ${READYGENIE_DIR}"
ruff format ${READYGENIE_DIR}

print_heading "Running: ruff check --select I --fix ${READYGENIE_DIR}"
ruff check --select I --fix ${READYGENIE_DIR}
