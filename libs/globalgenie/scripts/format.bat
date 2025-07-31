@echo off
REM ###########################################################################
REM # Format the globalgenie library using ruff
REM # Usage: scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory and set GLOBALGENIE_DIR to parent folder
SET "CURR_DIR=%~dp0"
SET "GLOBALGENIE_DIR=%CURR_DIR%\.."
SET "VENV_PATH=%GLOBALGENIE_DIR%\.venv"

REM Normalize paths
FOR %%I IN ("%GLOBALGENIE_DIR%") DO SET "GLOBALGENIE_DIR=%%~fI"
FOR %%I IN ("%VENV_PATH%") DO SET "VENV_PATH=%%~fI"

REM Try to activate virtual environment if it exists
IF EXIST "%VENV_PATH%\Scripts\activate.bat" (
    ECHO [INFO] Activating virtual environment: %VENV_PATH%
    CALL "%VENV_PATH%\Scripts\activate.bat"
) ELSE (
    ECHO [INFO] No virtual environment found at %VENV_PATH%
)

ECHO.
ECHO ##################################################
ECHO # Formatting globalgenie
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
ECHO # Running: ruff format %GLOBALGENIE_DIR%
ECHO ##################################################
ECHO.

python -m ruff format "%GLOBALGENIE_DIR%"

ECHO.
ECHO ##################################################
ECHO # Running: ruff check --select I --fix %GLOBALGENIE_DIR%
ECHO ##################################################
ECHO.

python -m ruff check --select I --fix "%GLOBALGENIE_DIR%"

ECHO [INFO] globalgenie formatting complete.
EXIT /B
