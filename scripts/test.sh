#!/bin/bash

############################################################################
# Run tests for all libraries
# Usage: ./scripts/test.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
GLOBALGENIE_DIR="${REPO_ROOT}/libs/globalgenie"
GLOBALGENIE_DOCKER_DIR="${REPO_ROOT}/libs/infra/globalgenie_docker"
GLOBALGENIE_AWS_DIR="${REPO_ROOT}/libs/infra/globalgenie_aws"
source ${CURR_DIR}/_utils.sh

print_heading "Running tests with coverage for all libraries"

# Run tests with coverage for each library
source ${GLOBALGENIE_DOCKER_DIR}/scripts/test.sh
source ${GLOBALGENIE_AWS_DIR}/scripts/test.sh
source ${GLOBALGENIE_DIR}/scripts/test.sh

# Combine coverage reports (optional)
coverage combine
coverage report
coverage html -d coverage_report
