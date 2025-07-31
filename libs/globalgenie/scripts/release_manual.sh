#!/bin/bash

############################################################################
# Release globalgenie to pypi
# Usage: ./libs/globalgenie/scripts/release_manual.sh
# Note:
#   build & twine must be available in the venv
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBALGENIE_DIR="$(dirname ${CURR_DIR})"
source ${CURR_DIR}/_utils.sh

main() {
  print_heading "Releasing *globalgenie*"

  cd ${GLOBALGENIE_DIR}
  print_heading "pwd: $(pwd)"

  print_heading "Proceed?"
  space_to_continue

  print_heading "Building globalgenie"
  python3 -m build

  print_heading "Release globalgenie to testpypi?"
  space_to_continue
  python3 -m twine upload --repository testpypi ${GLOBALGENIE_DIR}/dist/*

  print_heading "Release globalgenie to pypi"
  space_to_continue
  python3 -m twine upload --repository pypi ${GLOBALGENIE_DIR}/dist/*
}

main "$@"
