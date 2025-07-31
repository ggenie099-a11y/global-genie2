# Windows Setup Commands for GlobalGenie Testing

This document provides Windows-specific commands and procedures for testing GlobalGenie installation and integration.

## Prerequisites

### 1. Python Installation Verification

```cmd
# Check if Python is installed
python --version
py --version
python3 --version

# Check Python installation paths
where python
where py

# List available Python versions (if using Python Launcher)
py -0
```

### 2. PowerShell vs Command Prompt

#### Command Prompt (cmd)
```cmd
# Basic commands
python --version
pip --version
pip list
```

#### PowerShell
```powershell
# Basic commands
python --version
pip --version
Get-Command python
Get-Command pip
```

## Virtual Environment Setup

### Using venv (Recommended)

#### Command Prompt
```cmd
# Create virtual environment
python -m venv gg_test_env

# Activate virtual environment
gg_test_env\Scripts\activate.bat

# Verify activation
where python
where pip

# Install GlobalGenie
pip install globalgenie

# Test installation
python -c "import globalgenie; print(globalgenie.__version__)"

# Deactivate
deactivate
```

#### PowerShell
```powershell
# Create virtual environment
python -m venv gg_test_env

# Activate virtual environment (may require execution policy change)
.\gg_test_env\Scripts\Activate.ps1

# If execution policy error occurs:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activation again
.\gg_test_env\Scripts\Activate.ps1

# Verify activation
Get-Command python
Get-Command pip

# Install GlobalGenie
pip install globalgenie

# Test installation
python -c "import globalgenie; print(globalgenie.__version__)"

# Deactivate
deactivate
```

## Running Test Scripts

### 1. Comprehensive Installation Test

```cmd
# Run the main installation test
python test_installation_comprehensive.py

# Run with output redirection
python test_installation_comprehensive.py > installation_test_output.txt 2>&1
```

### 2. Cross-Platform Test

```cmd
# Run cross-platform compatibility test
python test_cross_platform.py

# View results
type cross_platform_test_report.txt
```

### 3. Verification Without Dependencies

```cmd
# Run dependency-free verification
python verify_without_dependencies.py

# Check exit code
echo %ERRORLEVEL%
```

### 4. Comprehensive Test Suite

```cmd
# Run all tests
python run_comprehensive_tests.py

# Run in background with logging
start /B python run_comprehensive_tests.py > comprehensive_test.log 2>&1
```

## Testing Different Python Versions

### Using Python Launcher (py)

```cmd
# Test with Python 3.8
py -3.8 -m venv test_py38
test_py38\Scripts\activate.bat
pip install globalgenie
python -c "import globalgenie; print('Python 3.8:', globalgenie.__version__)"
deactivate

# Test with Python 3.9
py -3.9 -m venv test_py39
test_py39\Scripts\activate.bat
pip install globalgenie
python -c "import globalgenie; print('Python 3.9:', globalgenie.__version__)"
deactivate

# Test with Python 3.10
py -3.10 -m venv test_py310
test_py310\Scripts\activate.bat
pip install globalgenie
python -c "import globalgenie; print('Python 3.10:', globalgenie.__version__)"
deactivate

# Test with Python 3.11
py -3.11 -m venv test_py311
test_py311\Scripts\activate.bat
pip install globalgenie
python -c "import globalgenie; print('Python 3.11:', globalgenie.__version__)"
deactivate
```

## Package Manager Testing

### 1. Standard pip

```cmd
# Create test environment
python -m venv pip_test
pip_test\Scripts\activate.bat

# Test different pip commands
pip install globalgenie
pip install --upgrade globalgenie
pip install --force-reinstall globalgenie
pip uninstall globalgenie -y

deactivate
```

### 2. pip3 (if available)

```cmd
# Test pip3 command
pip3 --version
pip3 install --user globalgenie --dry-run
```

### 3. python -m pip

```cmd
# Create test environment
python -m venv pip_module_test
pip_module_test\Scripts\activate.bat

# Test module-based pip
python -m pip install globalgenie
python -m pip list
python -m pip show globalgenie
python -m pip uninstall globalgenie -y

deactivate
```

## CLI Testing

### 1. Test Entry Points

```cmd
# After installation, test CLI commands
gg --help
globalgenie --help

# If commands not found, test module execution
python -m globalgenie.cli.entrypoint --help
```

### 2. Test in Different Shells

#### Command Prompt
```cmd
# Test in cmd
gg --version
globalgenie --version
```

#### PowerShell
```powershell
# Test in PowerShell
gg --version
globalgenie --version

# Test with full path if needed
& "C:\path\to\venv\Scripts\gg.exe" --version
```

## Troubleshooting Common Windows Issues

### 1. Execution Policy Issues (PowerShell)

```powershell
# Check current execution policy
Get-ExecutionPolicy

# Set execution policy for current user
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Temporarily bypass execution policy
powershell -ExecutionPolicy Bypass -File script.ps1
```

### 2. Path Issues

```cmd
# Check PATH variable
echo %PATH%

# Add Python to PATH (if needed)
set PATH=%PATH%;C:\Python39;C:\Python39\Scripts

# Make permanent (requires admin)
setx PATH "%PATH%;C:\Python39;C:\Python39\Scripts"
```

### 3. Permission Issues

```cmd
# Install to user directory
pip install --user globalgenie

# Check user site-packages
python -m site --user-site
```

### 4. Long Path Issues

```cmd
# Enable long paths (Windows 10/11, requires admin)
# Run in admin Command Prompt:
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1
```

## Automated Testing Script

Create a batch file `test_globalgenie.bat`:

```batch
@echo off
echo GlobalGenie Windows Installation Test
echo =====================================

echo.
echo 1. Testing Python availability...
python --version
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python not found
    exit /b 1
)

echo.
echo 2. Creating test environment...
python -m venv gg_windows_test
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

echo.
echo 3. Activating environment...
call gg_windows_test\Scripts\activate.bat

echo.
echo 4. Installing GlobalGenie...
pip install globalgenie
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to install GlobalGenie
    call deactivate
    exit /b 1
)

echo.
echo 5. Testing import...
python -c "import globalgenie; print('SUCCESS: GlobalGenie version', globalgenie.__version__)"
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to import GlobalGenie
    call deactivate
    exit /b 1
)

echo.
echo 6. Testing CLI...
gg --help > nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo WARNING: gg command not available, testing module execution...
    python -m globalgenie.cli.entrypoint --help > nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo ERROR: CLI not accessible
    ) else (
        echo SUCCESS: CLI accessible via module
    )
) else (
    echo SUCCESS: gg command available
)

echo.
echo 7. Cleaning up...
call deactivate
rmdir /s /q gg_windows_test

echo.
echo Windows installation test completed!
```

## Running the Automated Test

```cmd
# Make the batch file executable and run it
test_globalgenie.bat

# Or run with logging
test_globalgenie.bat > test_results.txt 2>&1
```

## Environment Variables for Testing

```cmd
# Set test-specific environment variables
set GLOBALGENIE_TEST_MODE=1
set PYTHONPATH=%PYTHONPATH%;%CD%

# Test with environment variables
python test_installation_comprehensive.py
```

## Performance Testing on Windows

```cmd
# Time the installation process
powershell "Measure-Command { pip install globalgenie }"

# Monitor resource usage during tests
# Use Task Manager or Resource Monitor during test execution
```

## Cleanup Commands

```cmd
# Remove all test environments
for /d %%i in (gg_test_*, test_py*, *_test) do rmdir /s /q "%%i"

# Remove test result files
del *test*.json *test*.txt *test*.log

# Clear pip cache
pip cache purge
```

This guide provides comprehensive Windows-specific commands for testing GlobalGenie installation across different scenarios and environments.