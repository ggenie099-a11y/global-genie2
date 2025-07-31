#!/bin/bash

############################################################################
# Format all libraries
# Usage: ./scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
GLOBALGENIE_DIR="${REPO_ROOT}/libs/globalgenie"
GLOBALGENIE_DOCKER_DIR="${REPO_ROOT}/libs/infra/globalgenie_docker"
GLOBALGENIE_AWS_DIR="${REPO_ROOT}/libs/infra/globalgenie_aws"
READYGENIE_DIR="${REPO_ROOT}/readygenie"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting all libraries"
source ${GLOBALGENIE_DIR}/scripts/format.sh
source ${GLOBALGENIE_DOCKER_DIR}/scripts/format.sh
source ${GLOBALGENIE_AWS_DIR}/scripts/format.sh

# Format all readygenie examples
source ${READYGENIE_DIR}/scripts/format.sh
