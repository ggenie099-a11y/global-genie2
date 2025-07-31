#!/usr/bin/env python3
"""
Final Fix for Remaining GlobalGenie Issues
Addresses version access and OpenAI import problems
"""

import sys
import subprocess
import importlib
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_pip_command(packages):
    """Run pip install command"""
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
            return True, result.stdout
        else:
            logger.error(f"✗ Failed: {result.stderr}")
            return False, result.stderr
            
    except Exception as e:
        logger.error(f"✗ Error: {e}")
        return False, str(e)

def check_package_installed(package_name):
    """Check if a package is properly installed"""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def diagnose_openai_issue():
    """Diagnose why OpenAI import is failing"""
    print("Diagnosing OpenAI import issue...")
    
    # Check if openai package is installed
    try:
        import openai
        print("✓ openai package is importable")
        print(f"  OpenAI version: {getattr(openai, '__version__', 'unknown')}")
        return True
    except ImportError as e:
        print(f"✗ openai package import failed: {e}")
        return False

def diagnose_version_issue():
    """Diagnose why version is not accessible"""
    print("Diagnosing version access issue...")
    
    try:
        import globalgenie
        print("✓ GlobalGenie imported successfully")
        
        # Check various ways to access version
        version_attrs = ['__version__', '_version', 'VERSION', 'version']
        found_version = False
        
        for attr in version_attrs:
            if hasattr(globalgenie, attr):
                version = getattr(globalgenie, attr)
                print(f"✓ Found version via {attr}: {version}")
                found_version = True
                break
        
        if not found_version:
            print("⚠ No version attribute found")
            
            # Check if it's in package metadata
            try:
                import pkg_resources
                version = pkg_resources.get_distribution('globalgenie').version
                print(f"✓ Found version via pkg_resources: {version}")
                found_version = True
            except:
                pass
            
            # Check with importlib.metadata (Python 3.8+)
            try:
                import importlib.metadata
                version = importlib.metadata.version('globalgenie')
                print(f"✓ Found version via importlib.metadata: {version}")
                found_version = True
            except:
                pass
        
        return found_version
        
    except ImportError as e:
        print(f"✗ GlobalGenie import failed: {e}")
        return False

def fix_openai_issue():
    """Fix OpenAI import issue"""
    print("\nFixing OpenAI import issue...")
    
    # First, check if it's already working
    if check_package_installed('openai'):
        print("✓ OpenAI is already properly installed")
        return True
    
    # Try different installation approaches
    strategies = [
        ["--upgrade", "openai"],
        ["--force-reinstall", "openai"],
        ["--no-cache-dir", "openai"],
        ["openai>=1.0.0"]
    ]
    
    for strategy in strategies:
        print(f"Trying: pip install {' '.join(strategy)}")
        success, output = run_pip_command(strategy)
        
        if success and check_package_installed('openai'):
            print("✓ OpenAI installation successful")
            return True
    
    print("✗ All OpenAI installation strategies failed")
    return False

def fix_version_issue():
    """Fix version access issue"""
    print("\nFixing version access issue...")
    
    # Try reinstalling with different approaches
    strategies = [
        ["--upgrade", "--force-reinstall", "globalgenie"],
        ["--no-cache-dir", "--force-reinstall", "globalgenie"],
        ["globalgenie==2.0.0"],  # Try specific version if available
    ]
    
    for strategy in strategies:
        print(f"Trying: pip install {' '.join(strategy)}")
        success, output = run_pip_command(strategy)
        
        if success:
            # Test if version is now accessible
            if diagnose_version_issue():
                print("✓ Version access fixed")
                return True
    
    print("⚠ Version access issue persists (may be a package issue)")
    return False

def comprehensive_test():
    """Run comprehensive test after fixes"""
    print("\nRunning comprehensive test...")
    
    tests = {}
    
    # Test 1: Basic import
    try:
        import globalgenie
        tests["basic_import"] = True
        print("✓ GlobalGenie import: SUCCESS")
    except ImportError as e:
        tests["basic_import"] = False
        print(f"✗ GlobalGenie import: FAILED - {e}")
    
    # Test 2: Version access
    try:
        import globalgenie
        
        # Try multiple methods to get version
        version = None
        methods = [
            lambda: getattr(globalgenie, '__version__', None),
            lambda: getattr(globalgenie, 'version', None),
            lambda: getattr(globalgenie, 'VERSION', None),
        ]
        
        for method in methods:
            try:
                version = method()
                if version:
                    break
            except:
                continue
        
        # Try package metadata
        if not version:
            try:
                import importlib.metadata
                version = importlib.metadata.version('globalgenie')
            except:
                pass
        
        if version:
            tests["version_access"] = True
            print(f"✓ Version access: SUCCESS - {version}")
        else:
            tests["version_access"] = False
            print("⚠ Version access: FAILED - No version found")
            
    except Exception as e:
        tests["version_access"] = False
        print(f"✗ Version access: FAILED - {e}")
    
    # Test 3: Agent import
    try:
        from globalgenie.agent import Agent
        tests["agent_import"] = True
        print("✓ Agent import: SUCCESS")
    except ImportError as e:
        tests["agent_import"] = False
        print(f"✗ Agent import: FAILED - {e}")
    
    # Test 4: OpenAI models import
    try:
        from globalgenie.models.openai import OpenAIChat
        tests["openai_models"] = True
        print("✓ OpenAI models import: SUCCESS")
    except ImportError as e:
        tests["openai_models"] = False
        print(f"⚠ OpenAI models import: FAILED - {e}")
    
    # Test 5: CLI import
    try:
        from globalgenie.cli.entrypoint import globalgenie_cli
        tests["cli_import"] = True
        print("✓ CLI import: SUCCESS")
    except ImportError as e:
        tests["cli_import"] = False
        print(f"✗ CLI import: FAILED - {e}")
    
    # Test 6: Basic agent creation (without API key)
    try:
        from globalgenie.agent import Agent
        from globalgenie.models.openai import OpenAIChat
        
        # This should work even without API key for basic instantiation
        agent = Agent(
            model=OpenAIChat(id="gpt-4", api_key="test-key"),
            instructions="Test agent"
        )
        tests["agent_creation"] = True
        print("✓ Agent creation: SUCCESS")
    except Exception as e:
        tests["agent_creation"] = False
        print(f"⚠ Agent creation: FAILED - {e}")
    
    return tests

def main():
    """Main fix function"""
    print("GlobalGenie Final Fix")
    print("=" * 30)
    print("Addressing remaining issues...")
    print()
    
    # Diagnose current state
    print("=== DIAGNOSIS ===")
    openai_ok = diagnose_openai_issue()
    version_ok = diagnose_version_issue()
    print()
    
    # Apply fixes
    print("=== APPLYING FIXES ===")
    
    if not openai_ok:
        fix_openai_issue()
    
    if not version_ok:
        fix_version_issue()
    
    print()
    
    # Final comprehensive test
    print("=== FINAL TESTING ===")
    results = comprehensive_test()
    
    # Summary
    print("\n" + "=" * 40)
    print("FINAL FIX SUMMARY")
    print("=" * 40)
    
    passed = sum(results.values())
    total = len(results)
    success_rate = (passed / total) * 100 if total > 0 else 0
    
    print(f"Tests Passed: {passed}/{total}")
    print(f"Success Rate: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("\n🎉 EXCELLENT! GlobalGenie is fully functional!")
    elif success_rate >= 75:
        print("\n✅ GOOD! GlobalGenie is mostly working.")
    elif success_rate >= 50:
        print("\n⚠️ PARTIAL SUCCESS. Some features may not work.")
    else:
        print("\n❌ SIGNIFICANT ISSUES REMAIN.")
    
    print("\nNext steps:")
    print("1. Run: python verify_without_dependencies.py")
    print("2. Test basic usage:")
    print('   python -c "import globalgenie; print(\'Success!\')"')
    
    if results.get("openai_models", False):
        print("3. Try creating an agent with OpenAI models")
    
    return 0 if success_rate >= 75 else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)