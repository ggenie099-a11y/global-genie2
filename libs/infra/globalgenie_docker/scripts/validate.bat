@echo off
REM ###########################################################################
REM # Validate the globalgenie_docker library using ruff and mypy
REM # Usage: libs\infra\globalgenie_docker\scripts\validate.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "GLOBALGENIE_DOCKER_DIR=%CURR_DIR%\.."

ECHO.
ECHO ##################################################
ECHO # Validating globalgenie_docker
ECHO ##################################################
ECHO.

REM Check if ruff and mypy are installed
python -c "import ruff" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] ruff is not installed. Please install it with: pip install ruff
    EXIT /B 1
)

python -c "import mypy" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] mypy is not installed. Please install it with: pip install mypy
    EXIT /B 1
)

ECHO.
ECHO ##################################################
ECHO # Running: ruff check %GLOBALGENIE_DOCKER_DIR%
ECHO ##################################################
ECHO.

python -m ruff check "%GLOBALGENIE_DOCKER_DIR%"
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] ruff check failed with exit code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)

ECHO.
ECHO ##################################################
ECHO # Running: mypy %GLOBALGENIE_DOCKER_DIR% --config-file %GLOBALGENIE_DOCKER_DIR%\pyproject.toml
ECHO ##################################################
ECHO.

python -m mypy "%GLOBALGENIE_DOCKER_DIR%" --config-file "%GLOBALGENIE_DOCKER_DIR%\pyproject.toml"
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] mypy validation failed with exit code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)

ECHO [INFO] globalgenie_docker validation complete.
EXIT /B 0 