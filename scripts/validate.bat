@echo off
REM ###########################################################################
REM # Validate all libraries
REM # Usage: scripts\validate.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "REPO_ROOT=%CURR_DIR%\.."
SET "GLOBALGENIE_DIR=%REPO_ROOT%\libs\globalgenie"
SET "GLOBALGENIE_DOCKER_DIR=%REPO_ROOT%\libs\infra\globalgenie_docker"
SET "GLOBALGENIE_AWS_DIR=%REPO_ROOT%\libs\infra\globalgenie_aws"

REM Function to print headings
CALL :print_heading "Validating all libraries"

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

REM Validate all libraries
SET GLOBALGENIE_VALIDATE="%GLOBALGENIE_DIR%\scripts\validate.bat"
IF EXIST %GLOBALGENIE_VALIDATE% (
    ECHO [INFO] Running %GLOBALGENIE_VALIDATE%
    CALL %GLOBALGENIE_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %GLOBALGENIE_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_VALIDATE% does not exist, skipping
)

SET GLOBALGENIE_DOCKER_VALIDATE="%GLOBALGENIE_DOCKER_DIR%\scripts\validate.bat"
IF EXIST %GLOBALGENIE_DOCKER_VALIDATE% (
    ECHO [INFO] Running %GLOBALGENIE_DOCKER_VALIDATE%
    CALL %GLOBALGENIE_DOCKER_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %GLOBALGENIE_DOCKER_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_DOCKER_VALIDATE% does not exist, skipping
)

SET GLOBALGENIE_AWS_VALIDATE="%GLOBALGENIE_AWS_DIR%\scripts\validate.bat"
IF EXIST %GLOBALGENIE_AWS_VALIDATE% (
    ECHO [INFO] Running %GLOBALGENIE_AWS_VALIDATE%
    CALL %GLOBALGENIE_AWS_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %GLOBALGENIE_AWS_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %GLOBALGENIE_AWS_VALIDATE% does not exist, skipping
)

ECHO [INFO] All validations complete.
EXIT /B 0

REM Function to print headings
:print_heading
ECHO.
ECHO ##################################################
ECHO # %1
ECHO ##################################################
ECHO.
EXIT /B 