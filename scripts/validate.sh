#!/bin/bash

############################################################################
# Validate all libraries
# Usage: ./scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
GLOBALGENIE_DIR="${REPO_ROOT}/libs/globalgenie"
GLOBALGENIE_DOCKER_DIR="${REPO_ROOT}/libs/infra/globalgenie_docker"
GLOBALGENIE_AWS_DIR="${REPO_ROOT}/libs/infra/globalgenie_aws"
source ${CURR_DIR}/_utils.sh

print_heading "Validating all libraries"
source ${GLOBALGENIE_DIR}/scripts/validate.sh
source ${GLOBALGENIE_DOCKER_DIR}/scripts/validate.sh
source ${GLOBALGENIE_AWS_DIR}/scripts/validate.sh
