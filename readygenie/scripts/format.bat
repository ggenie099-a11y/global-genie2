@echo off
REM ###########################################################################
REM # Format the readygenie using ruff
REM # Usage: readygenie\scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "READYGENIE_DIR=%CURR_DIR%\.."

ECHO.
ECHO ##################################################
ECHO # Formatting readygenie
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
ECHO # Running: ruff format %READYGENIE_DIR%
ECHO ##################################################
ECHO.

python -m ruff format "%READYGENIE_DIR%"

ECHO.
ECHO ##################################################
ECHO # Running: ruff check --select I --fix %READYGENIE_DIR%
ECHO ##################################################
ECHO.

python -m ruff check --select I --fix "%READYGENIE_DIR%"

ECHO [INFO] readygenie formatting complete.
EXIT /B 