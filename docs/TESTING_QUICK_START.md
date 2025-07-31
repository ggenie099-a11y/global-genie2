# GlobalGenie Testing Quick Start Guide

Based on your test results, here's how to quickly test and fix GlobalGenie installation issues.

## Current Status Analysis

From your verification results, we identified:
- ✅ Python 3.12.7 (compatible)
- ✅ GlobalGenie package installed
- ❌ Missing core dependencies (gitpython, python_dotenv, python_multipart, pyyaml)
- ❌ Missing OpenAI dependency for models
- ❌ Version info not accessible
- ❌ Windows encoding issues with Unicode characters

## Quick Fix Options

### Option 1: Automated Complete Installation (Recommended)

```cmd
# Run the complete installer (handles all dependencies)
python install_globalgenie_complete.py

# Or use the Windows batch file
install_globalgenie.bat
```

### Option 2: Fix Current Installation

```cmd
# Run the installation fixer
python fix_globalgenie_installation.py
```

### Option 3: Manual Dependency Installation

```cmd
# Install missing core dependencies
pip install gitpython python-dotenv python-multipart pyyaml

# Install OpenAI support (for models)
pip install openai

# Reinstall GlobalGenie to ensure everything works
pip install --force-reinstall globalgenie
```

## Testing Your Installation

### Quick Verification (30 seconds)
```cmd
# Run the fixed verification script
python verify_without_dependencies.py
```

### Comprehensive Testing (5-15 minutes)
```cmd
# Run all installation tests
python test_installation_comprehensive.py
```

### Full Test Suite (20-30 minutes)
```cmd
# Run everything with consolidated reporting
python run_comprehensive_tests.py
```

## Expected Results After Fix

After running the fixes, you should see:
- ✅ All core imports working
- ✅ Version information accessible
- ✅ CLI commands functional
- ✅ Example scripts runnable
- ✅ Clean uninstall process

## Windows-Specific Notes

### Character Encoding
The scripts now use Windows-compatible characters instead of Unicode symbols:
- `[PASS]` instead of `✓`
- `[FAIL]` instead of `✗`

### Virtual Environment Recommendation
For best results on Windows, use a virtual environment:

```cmd
# Create virtual environment
python -m venv globalgenie_env

# Activate it
globalgenie_env\Scripts\activate.bat

# Install GlobalGenie
pip install globalgenie

# Install additional dependencies
pip install openai anthropic

# Test installation
python -c "import globalgenie; print('Success!')"
```

### PowerShell vs Command Prompt
Both should work, but if you have issues with PowerShell execution policy:

```powershell
# Allow script execution (run as administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Troubleshooting Common Issues

### Issue: "Module not found" errors
**Solution**: Install missing dependencies
```cmd
pip install --upgrade pip
pip install globalgenie[all]  # Install with all optional dependencies
```

### Issue: Permission errors
**Solution**: Use user installation or virtual environment
```cmd
pip install --user globalgenie
# OR
python -m venv myenv && myenv\Scripts\activate.bat && pip install globalgenie
```

### Issue: CLI commands not found
**Solution**: Use module execution
```cmd
python -m globalgenie.cli.entrypoint --help
```

### Issue: Version not accessible
**Solution**: Reinstall with force
```cmd
pip uninstall globalgenie -y
pip install globalgenie
```

## Next Steps After Successful Installation

1. **Test basic functionality**:
   ```cmd
   python test_globalgenie_installation.py
   ```

2. **Try example scripts**:
   ```python
   from globalgenie.agent import Agent
   from globalgenie.models.openai import OpenAIChat
   
   # Set your API key
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key-here"
   
   # Create an agent
   agent = Agent(
       model=OpenAIChat(id="gpt-4"),
       instructions="You are a helpful assistant."
   )
   
   # Test it
   response = agent.run("Hello, how are you?")
   print(response.content)
   ```

3. **Explore advanced features**:
   - Check `EXAMPLES.md` for comprehensive examples
   - Review `README.md` for feature overview
   - Visit documentation for detailed guides

## File Overview

| File | Purpose | When to Use |
|------|---------|-------------|
| `install_globalgenie_complete.py` | Complete fresh installation | First time setup or major issues |
| `fix_globalgenie_installation.py` | Fix existing installation | When verification shows issues |
| `verify_without_dependencies.py` | Quick verification check | After any changes to test status |
| `test_installation_comprehensive.py` | Thorough installation testing | Before production deployment |
| `run_comprehensive_tests.py` | Full test suite | Complete validation needed |
| `install_globalgenie.bat` | Windows batch installer | Easy one-click installation |

## Getting Help

If you continue to have issues:

1. **Check the logs**: All scripts generate detailed logs
2. **Review error messages**: Look for specific error details
3. **Try virtual environment**: Isolates dependency conflicts
4. **Update Python/pip**: Ensure you have recent versions
5. **Check system requirements**: Verify OS compatibility

## Success Indicators

You'll know GlobalGenie is properly installed when:
- ✅ `import globalgenie` works without errors
- ✅ `globalgenie.__version__` returns a version number
- ✅ Agent creation works (even without API keys)
- ✅ CLI commands are accessible
- ✅ Example scripts run successfully

Run the verification script after any fixes to confirm success!