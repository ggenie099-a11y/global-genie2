#!/bin/bash

############################################################################
# Release globalgenie_docker to pypi
# Usage: ./libs/infra/globalgenie_docker/scripts/release_manual.sh
# Note:
#   build & twine must be available in the venv
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DOCKER_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Releasing *globalgenie_docker*"

  cd ${GLOBALGENIE_DOCKER_DIR}
  print_heading "pwd: $(pwd)"

  print_heading "Proceed?"
  space_to_continue

  print_heading "Building globalgenie_docker"
  python3 -m build

  print_heading "Release globalgenie_docker to testpypi?"
  space_to_continue
  python3 -m twine upload --repository testpypi ${GLOBALGENIE_DOCKER_DIR}/dist/*

  print_heading "Release globalgenie_docker to pypi"
  space_to_continue
  python3 -m twine upload --repository pypi ${GLOBALGENIE_DOCKER_DIR}/dist/*
}

main "$@"
