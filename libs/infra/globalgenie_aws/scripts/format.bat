@echo off
REM ###########################################################################
REM # Format the globalgenie_aws library using ruff
REM # Usage: libs\infra\globalgenie_aws\scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "GLOBALGENIE_AWS_DIR=%CURR_DIR%\.."

ECHO.
ECHO ##################################################
ECHO # Formatting globalgenie_aws
ECHO ##################################################
ECHO.

REM Check if ruff is installed
python -c "import ruff" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] ruff is not installed. Please install it with: pip install ruff
    EXIT /B 1
)

ECHO.
ECHO ##################################################
ECHO # Running: ruff format %GLOBALGENIE_AWS_DIR%
ECHO ##################################################
ECHO.

python -m ruff format "%GLOBALGENIE_AWS_DIR%"

ECHO.
ECHO ##################################################
ECHO # Running: ruff check --select I --fix %GLOBALGENIE_AWS_DIR%
ECHO ##################################################
ECHO.

python -m ruff check --select I --fix "%GLOBALGENIE_AWS_DIR%"

ECHO [INFO] globalgenie_aws formatting complete.
EXIT /B 