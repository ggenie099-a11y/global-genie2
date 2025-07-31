#!/bin/bash

############################################################################
# Validate the globalgenie_docker library using ruff and mypy
# Usage: ./libs/infra/globalgenie_docker/scripts/validate.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

print_heading "Validating globalgenie_docker"

print_heading "Running: ruff check ${GLOBALGENIE_DOCKER_DIR}"
ruff check ${GLOBALGENIE_DOCKER_DIR}

print_heading "Running: mypy ${GLOBALGENIE_DOCKER_DIR} --config-file ${GLOBALGENIE_DOCKER_DIR}/pyproject.toml"
mypy ${GLOBALGENIE_DOCKER_DIR} --config-file ${GLOBALGENIE_DOCKER_DIR}/pyproject.toml
