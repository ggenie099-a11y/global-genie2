#!/bin/bash

############################################################################
# Run tests for the globalgenie library
# Usage: ./libs/infra/globalgenie_docker/scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests for globalgenie"

print_heading "Running: pytest ${GLOBALGENIE_DOCKER_DIR}"
pytest ${GLOBALGENIE_DOCKER_DIR}/tests
