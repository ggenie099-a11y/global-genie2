#!/bin/bash

############################################################################
# Run tests for the globalgenie library
# Usage: ./libs/globalgenie/scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests for globalgenie"

print_heading "Running: pytest ${GLOBALGENIE_DIR} with coverage"
pytest ${GLOBALGENIE_DIR}/tests/unit --cov=${GLOBALGENIE_DIR}/globalgenie --cov-report=term-missing --cov-report=html
