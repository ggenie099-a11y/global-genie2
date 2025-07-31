#!/bin/bash

############################################################################
# Release globalgenie_aws to pypi
# Usage: ./libs/infra/globalgenie_aws/scripts/release_manual.sh
# Note:
#   build & twine must be available in the venv
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_AWS_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Releasing *globalgenie_aws*"

  cd ${GLOBALGENIE_AWS_DIR}
  print_heading "pwd: $(pwd)"

  print_heading "Proceed?"
  space_to_continue

  print_heading "Building globalgenie_aws"
  python3 -m build

  print_heading "Release globalgenie_aws to testpypi?"
  space_to_continue
  python3 -m twine upload --repository testpypi ${GLOBALGENIE_AWS_DIR}/dist/*

  print_heading "Release globalgenie_aws to pypi"
  space_to_continue
  python3 -m twine upload --repository pypi ${GLOBALGENIE_AWS_DIR}/dist/*
}

main "$@"
