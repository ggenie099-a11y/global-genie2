#!/bin/bash

############################################################################
# Format the globalgenie_docker library using ruff
# Usage: ./libs/infra/globalgenie_docker/scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting globalgenie_docker"

print_heading "Running: ruff format ${GLOBALGENIE_DOCKER_DIR}"
ruff format ${GLOBALGENIE_DOCKER_DIR}

print_heading "Running: ruff check --select I --fix ${GLOBALGENIE_DOCKER_DIR}"
ruff check --select I --fix ${GLOBALGENIE_DOCKER_DIR}
