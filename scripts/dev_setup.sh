#!/bin/bash

############################################################################
# GlobalGenie Development Setup
# - Create a virtual environment and install libraries in editable mode.
# - Please install uv before running this script.
# - Please deactivate the existing virtual environment before running.
# Usage: ./scripts/dev_setup.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
GLOBALGENIE_DIR="${REPO_ROOT}/libs/globalgenie"
GLOBALGENIE_DOCKER_DIR="${REPO_ROOT}/libs/infra/globalgenie_docker"
GLOBALGENIE_AWS_DIR="${REPO_ROOT}/libs/infra/globalgenie_aws"
source "${CURR_DIR}/_utils.sh"

VENV_DIR="${REPO_ROOT}/.venv"
PYTHON_VERSION=$(python3 --version)

print_heading "Development setup..."

print_heading "Removing virtual env"
print_info "rm -rf ${VENV_DIR}"
rm -rf ${VENV_DIR}

print_heading "Creating virtual env"
print_info "VIRTUAL_ENV=${VENV_DIR} uv venv --python 3.12"
VIRTUAL_ENV=${VENV_DIR} uv venv --python 3.12

print_heading "Installing globalgenie"
print_info "VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_DIR}/requirements.txt"
VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_DIR}/requirements.txt

print_heading "Installing globalgenie in editable mode with tests dependencies"
VIRTUAL_ENV=${VENV_DIR} uv pip install -U -e ${GLOBALGENIE_DIR}[tests]
VIRTUAL_ENV=${VENV_DIR} uv pip install yfinance

VIRTUAL_ENV=${VENV_DIR} uv pip install google-genai==1.17.0
VIRTUAL_ENV=${VENV_DIR} uv pip install mcp==1.9.2
VIRTUAL_ENV=${VENV_DIR} uv pip install crawl4ai==0.6.3

print_heading "Installing globalgenie-docker"
print_info "VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_DOCKER_DIR}/requirements.txt"
VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_DOCKER_DIR}/requirements.txt
VIRTUAL_ENV=${VENV_DIR} uv pip install yfinance

print_heading "Installing globalgenie-docker in editable mode with dev dependencies"
VIRTUAL_ENV=${VENV_DIR} uv pip install -e ${GLOBALGENIE_DOCKER_DIR}[dev]

print_heading "Installing globalgenie-aws"
print_info "VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_AWS_DIR}/requirements.txt"
VIRTUAL_ENV=${VENV_DIR} uv pip install -r ${GLOBALGENIE_AWS_DIR}/requirements.txt

print_heading "Installing globalgenie-aws in editable mode with dev dependencies"
VIRTUAL_ENV=${VENV_DIR} uv pip install -e ${GLOBALGENIE_AWS_DIR}[dev]

print_heading "uv pip list"
VIRTUAL_ENV=${VENV_DIR} uv pip list

print_heading "Development setup complete"
print_heading "Activate venv using: source .venv/bin/activate"
