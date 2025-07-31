@echo off
REM ###########################################################################
REM # GlobalGenie Development Setup (Windows)
REM # - Create a virtual environment and install libraries in editable mode.
REM # - Please deactivate the existing virtual environment before running.
REM # Usage: scripts\dev_setup.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "REPO_ROOT=%CURR_DIR%\.."
SET "GLOBALGENIE_DIR=%REPO_ROOT%\libs\globalgenie"
SET "GLOBALGENIE_DOCKER_DIR=%REPO_ROOT%\libs\infra\globalgenie_docker"
SET "GLOBALGENIE_AWS_DIR=%REPO_ROOT%\libs\infra\globalgenie_aws"
SET "VENV_DIR=%REPO_ROOT%\.venv"

REM Function to print headings
CALL :print_heading "Development setup..."

CALL :print_heading "Removing virtual env"
ECHO [INFO] Removing %VENV_DIR%
rmdir /s /q "%VENV_DIR%" 2>nul

CALL :print_heading "Creating virtual env"
ECHO [INFO] Creating virtual environment in %VENV_DIR%
python -m venv "%VENV_DIR%"

REM Activate virtual environment
CALL :activate_venv

CALL :print_heading "Installing globalgenie"
ECHO [INFO] Installing dependencies from %GLOBALGENIE_DIR%\requirements.txt
pip install -r "%GLOBALGENIE_DIR%\requirements.txt"

CALL :print_heading "Installing globalgenie in editable mode with tests dependencies"
pip install -e "%GLOBALGENIE_DIR%[tests]"

CALL :print_heading "Installing globalgenie-docker"
ECHO [INFO] Installing dependencies from %GLOBALGENIE_DOCKER_DIR%\requirements.txt
pip install -r "%GLOBALGENIE_DOCKER_DIR%\requirements.txt"

CALL :print_heading "Installing globalgenie-docker in editable mode with dev dependencies"
pip install -e "%GLOBALGENIE_DOCKER_DIR%[dev]"

CALL :print_heading "Installing globalgenie-aws"
ECHO [INFO] Installing dependencies from %GLOBALGENIE_AWS_DIR%\requirements.txt
pip install -r "%GLOBALGENIE_AWS_DIR%\requirements.txt"

CALL :print_heading "Installing globalgenie-aws in editable mode with dev dependencies"
pip install -e "%GLOBALGENIE_AWS_DIR%[dev]"

CALL :print_heading "pip list"
pip list

CALL :print_heading "Development setup complete"
ECHO.
ECHO Activate venv using: .\.venv\Scripts\activate
ECHO.
EXIT /B

REM Function to print headings
:print_heading
ECHO.
ECHO ##################################################
ECHO # %1
ECHO ##################################################
ECHO.
EXIT /B

REM Function to activate virtual environment
:activate_venv
ECHO [INFO] Activating virtual environment...
CALL "%VENV_DIR%\Scripts\activate"
EXIT /B