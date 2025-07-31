@echo off
echo GlobalGenie Installation for Windows
echo ====================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Starting installation...
echo.

REM Run the simple installation script
python install_globalgenie_simple.py

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================
    echo Installation completed successfully!
    echo ========================================
    echo.
    echo To test your installation, run:
    echo   python test_globalgenie_installation.py
    echo.
    echo To get started with GlobalGenie, check out:
    echo   - README.md for basic usage
    echo   - EXAMPLES.md for code examples
    echo.
) else (
    echo.
    echo ========================================
    echo Installation encountered issues
    echo ========================================
    echo.
    echo Please check the installation report for details.
    echo You can also try running the fixer:
    echo   python fix_globalgenie_installation.py
    echo.
)

pause