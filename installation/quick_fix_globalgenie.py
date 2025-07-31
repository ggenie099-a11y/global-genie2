#!/usr/bin/env python3
"""
Quick Fix for GlobalGenie Installation Issues
Addresses the specific problems identified in verification
"""

import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_pip_command(packages):
    """Run pip install command with proper Windows handling"""
    cmd = [sys.executable, "-m", "pip", "install"] + packages
    
    logger.info(f"Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode == 0:
            logger.info("✓ Success")
            return True
        else:
            logger.error(f"✗ Failed: {result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"✗ Error: {e}")
        return False

def main():
    """Quick fix for the identified issues"""
    print("GlobalGenie Quick Fix")
    print("=" * 30)
    print("Fixing the issues identified in your verification...")
    print()
    
    # Step 1: Install missing core dependencies
    print("Step 1: Installing missing core dependencies...")
    missing_deps = [
        "gitpython",
        "python-dotenv", 
        "python-multipart",
        "pyyaml"
    ]
    
    success_count = 0
    for dep in missing_deps:
        print(f"Installing {dep}...")
        if run_pip_command([dep]):
            success_count += 1
    
    print(f"Core dependencies: {success_count}/{len(missing_deps)} installed")
    print()
    
    # Step 2: Install OpenAI for models support
    print("Step 2: Installing OpenAI support...")
    openai_success = run_pip_command(["openai"])
    print()
    
    # Step 3: Reinstall GlobalGenie to ensure everything works
    print("Step 3: Reinstalling GlobalGenie...")
    gg_success = run_pip_command(["--force-reinstall", "globalgenie"])
    print()
    
    # Step 4: Test the installation
    print("Step 4: Testing installation...")
    
    tests_passed = 0
    total_tests = 0
    
    # Test basic import
    total_tests += 1
    try:
        import globalgenie
        print("✓ GlobalGenie import: SUCCESS")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ GlobalGenie import: FAILED - {e}")
    
    # Test version access
    total_tests += 1
    try:
        import globalgenie
        version = getattr(globalgenie, '__version__', None)
        if version:
            print(f"✓ Version access: SUCCESS - {version}")
            tests_passed += 1
        else:
            print("⚠ Version access: PARTIAL - No version attribute")
    except Exception as e:
        print(f"✗ Version access: FAILED - {e}")
    
    # Test agent import
    total_tests += 1
    try:
        from globalgenie.agent import Agent
        print("✓ Agent import: SUCCESS")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ Agent import: FAILED - {e}")
    
    # Test models import
    total_tests += 1
    try:
        from globalgenie.models.openai import OpenAIChat
        print("✓ OpenAI models import: SUCCESS")
        tests_passed += 1
    except ImportError as e:
        print(f"⚠ OpenAI models import: FAILED - {e}")
    
    # Test CLI import
    total_tests += 1
    try:
        from globalgenie.cli.entrypoint import globalgenie_cli
        print("✓ CLI import: SUCCESS")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ CLI import: FAILED - {e}")
    
    print()
    print("=" * 40)
    print("QUICK FIX SUMMARY")
    print("=" * 40)
    print(f"Tests Passed: {tests_passed}/{total_tests}")
    
    success_rate = (tests_passed / total_tests) * 100 if total_tests > 0 else 0
    print(f"Success Rate: {success_rate:.1f}%")
    
    if success_rate == 100:
        print("\n🎉 ALL ISSUES FIXED!")
        print("GlobalGenie is now working correctly.")
    elif success_rate >= 80:
        print("\n✅ MOST ISSUES FIXED")
        print("GlobalGenie should work for basic usage.")
    else:
        print("\n⚠️ SOME ISSUES REMAIN")
        print("You may need to run the complete installer.")
    
    print("\nNext steps:")
    print("1. Test with: python -c \"import globalgenie; print('Success!')\"")
    print("2. Run verification: python verify_without_dependencies.py")
    print("3. If issues persist, try: python install_globalgenie_simple.py")
    
    return 0 if success_rate >= 80 else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)