@echo off
REM ###########################################################################
REM # Format all libraries
REM # Usage: scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "REPO_ROOT=%CURR_DIR%\.."
SET "GLOBALGENIE_DIR=%REPO_ROOT%\libs\globalgenie"
SET "GLOBALGENIE_DOCKER_DIR=%REPO_ROOT%\libs\infra\globalgenie_docker"
SET "GLOBALGENIE_AWS_DIR=%REPO_ROOT%\libs\infra\globalgenie_aws"
SET "READYGENIE_DIR=%REPO_ROOT%\readygenie"

REM Function to print headings
CALL :print_heading "Formatting all libraries"

REM Check if directories exist
IF NOT EXIST "%GLOBALGENIE_DIR%" (
    ECHO [ERROR] GLOBALGENIE_DIR: %GLOBALGENIE_DIR% does not exist
    EXIT /B 1
)

IF NOT EXIST "%GLOBALGENIE_DOCKER_DIR%" (
    ECHO [ERROR] GLOBALGENIE_DOCKER_DIR: %GLOBALGENIE_DOCKER_DIR% does not exist
    EXIT /B 1
)

IF NOT EXIST "%GLOBALGENIE_AWS_DIR%" (
    ECHO [ERROR] GLOBALGENIE_AWS_DIR: %GLOBALGENIE_AWS_DIR% does not exist
    EXIT /B 1
)

IF NOT EXIST "%READYGENIE_DIR%" (
    ECHO [ERROR] READYGENIE_DIR: %READYGENIE_DIR% does not exist
    EXIT /B 1
)

REM Format all libraries
SET GLOBALGENIE_FORMAT="%GLOBALGENIE_DIR%\scripts\format.bat"
IF EXIST %GLOBALGENIE_FORMAT% (
    ECHO [INFO] Running %GLOBALGENIE_FORMAT%
    CALL %GLOBALGENIE_FORMAT%
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_FORMAT% does not exist, skipping
)

SET GLOBALGENIE_DOCKER_FORMAT="%GLOBALGENIE_DOCKER_DIR%\scripts\format.bat"
IF EXIST %GLOBALGENIE_DOCKER_FORMAT% (
    ECHO [INFO] Running %GLOBALGENIE_DOCKER_FORMAT%
    CALL %GLOBALGENIE_DOCKER_FORMAT%
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_DOCKER_FORMAT% does not exist, skipping
)

SET GLOBALGENIE_AWS_FORMAT="%GLOBALGENIE_AWS_DIR%\scripts\format.bat"
IF EXIST %GLOBALGENIE_AWS_FORMAT% (
    ECHO [INFO] Running %GLOBALGENIE_AWS_FORMAT%
    CALL %GLOBALGENIE_AWS_FORMAT%
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_AWS_FORMAT% does not exist, skipping
)

REM Format all readygenie examples
SET READYGENIE_FORMAT="%READYGENIE_DIR%\scripts\format.bat"
IF EXIST %READYGENIE_FORMAT% (
    ECHO [INFO] Running %READYGENIE_FORMAT%
    CALL %READYGENIE_FORMAT%
) ELSE (
    ECHO [WARNING] %READYGENIE_FORMAT% does not exist, skipping
)

ECHO [INFO] All formatting complete.
EXIT /B

REM Function to print headings
:print_heading
ECHO.
ECHO ##################################################
ECHO # %1
ECHO ##################################################
ECHO.
EXIT /B 