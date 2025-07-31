#!/usr/bin/env python3
"""
Fix OpenAI Detection Issue in GlobalGenie
Addresses the specific problem where openai package is installed but not detected
"""

import sys
import subprocess
import importlib
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def check_openai_installation():
    """Thoroughly check OpenAI installation"""
    print("=== OPENAI INSTALLATION DIAGNOSIS ===")
    
    # Test 1: Direct import
    try:
        import openai
        print("✓ Direct openai import: SUCCESS")
        print(f"  OpenAI version: {getattr(openai, '__version__', 'unknown')}")
        print(f"  OpenAI location: {openai.__file__}")
        return True
    except ImportError as e:
        print(f"✗ Direct openai import: FAILED - {e}")
        return False

def check_pip_list():
    """Check what pip thinks is installed"""
    print("\n=== PIP PACKAGE LIST ===")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            openai_found = False
            
            for line in lines:
                if 'openai' in line.lower():
                    print(f"✓ Found in pip list: {line.strip()}")
                    openai_found = True
            
            if not openai_found:
                print("✗ OpenAI not found in pip list")
            
            return openai_found
        else:
            print(f"✗ Failed to get pip list: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error checking pip list: {e}")
        return False

def reinstall_openai():
    """Reinstall OpenAI with different strategies"""
    print("\n=== REINSTALLING OPENAI ===")
    
    strategies = [
        ["uninstall", "openai", "-y"],  # First uninstall
        ["install", "openai"],          # Then reinstall
        ["install", "--upgrade", "openai"],
        ["install", "--force-reinstall", "openai"],
        ["install", "--no-cache-dir", "openai"]
    ]
    
    for i, strategy in enumerate(strategies):
        print(f"Step {i+1}: pip {' '.join(strategy)}")
        
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip"] + strategy,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=120
            )
            
            if result.returncode == 0:
                print("  ✓ Success")
                
                # After reinstall, test import
                if "install" in strategy:
                    try:
                        # Clear import cache
                        if 'openai' in sys.modules:
                            del sys.modules['openai']
                        
                        import openai
                        print(f"  ✓ Import test successful - version {getattr(openai, '__version__', 'unknown')}")
                        return True
                    except ImportError as e:
                        print(f"  ⚠ Import test failed: {e}")
            else:
                print(f"  ✗ Failed: {result.stderr}")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    return False

def test_globalgenie_openai():
    """Test GlobalGenie's OpenAI integration specifically"""
    print("\n=== TESTING GLOBALGENIE OPENAI INTEGRATION ===")
    
    try:
        # Clear any cached imports
        modules_to_clear = [
            'globalgenie.models.openai',
            'globalgenie.models',
            'openai'
        ]
        
        for module in modules_to_clear:
            if module in sys.modules:
                del sys.modules[module]
        
        # Test the specific import that's failing
        from globalgenie.models.openai import OpenAIChat
        print("✓ GlobalGenie OpenAI models import: SUCCESS")
        
        # Test basic instantiation
        try:
            model = OpenAIChat(id="gpt-4", api_key="test-key")
            print("✓ OpenAIChat instantiation: SUCCESS")
            return True
        except Exception as e:
            print(f"⚠ OpenAIChat instantiation: FAILED - {e}")
            return False
            
    except ImportError as e:
        print(f"✗ GlobalGenie OpenAI models import: FAILED - {e}")
        
        # Try to understand why it's failing
        try:
            import openai
            print("  ✓ Direct openai import works")
            print("  ⚠ Issue seems to be in GlobalGenie's openai integration")
        except ImportError:
            print("  ✗ Direct openai import also fails")
        
        return False

def check_python_path():
    """Check Python path and site-packages"""
    print("\n=== PYTHON PATH DIAGNOSIS ===")
    
    import site
    
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print("\nSite packages directories:")
    for path in site.getsitepackages():
        print(f"  {path}")
    
    print(f"\nUser site packages: {site.getusersitepackages()}")
    
    # Check if openai is in any of these locations
    import os
    for site_dir in site.getsitepackages() + [site.getusersitepackages()]:
        openai_path = os.path.join(site_dir, 'openai')
        if os.path.exists(openai_path):
            print(f"✓ Found openai package at: {openai_path}")
        else:
            print(f"✗ No openai package at: {openai_path}")

def main():
    """Main diagnostic and fix function"""
    print("GlobalGenie OpenAI Detection Fix")
    print("=" * 40)
    
    # Step 1: Diagnose current state
    openai_direct = check_openai_installation()
    openai_in_pip = check_pip_list()
    
    # Step 2: Check Python environment
    check_python_path()
    
    # Step 3: If OpenAI seems to be installed but not working, try reinstall
    if not openai_direct:
        print("\nOpenAI not directly importable - attempting reinstall...")
        openai_reinstalled = reinstall_openai()
    else:
        print("\nOpenAI is directly importable - checking GlobalGenie integration...")
        openai_reinstalled = True
    
    # Step 4: Test GlobalGenie integration
    gg_openai_works = test_globalgenie_openai()
    
    # Step 5: Summary and recommendations
    print("\n" + "=" * 50)
    print("OPENAI FIX SUMMARY")
    print("=" * 50)
    
    print(f"Direct OpenAI import: {'✓' if openai_direct else '✗'}")
    print(f"OpenAI in pip list: {'✓' if openai_in_pip else '✗'}")
    print(f"GlobalGenie OpenAI integration: {'✓' if gg_openai_works else '✗'}")
    
    if gg_openai_works:
        print("\n🎉 SUCCESS! OpenAI integration is now working!")
        print("\nYou can now:")
        print("1. Create agents with OpenAI models")
        print("2. Use OpenAIChat in your code")
        print("3. Run the full verification test")
        
        # Test basic agent creation
        print("\n=== TESTING AGENT CREATION ===")
        try:
            from globalgenie.agent import Agent
            from globalgenie.models.openai import OpenAIChat
            
            agent = Agent(
                model=OpenAIChat(id="gpt-4", api_key="test-key"),
                instructions="Test agent"
            )
            print("✓ Agent creation with OpenAI model: SUCCESS")
        except Exception as e:
            print(f"⚠ Agent creation: FAILED - {e}")
        
        return 0
    else:
        print("\n⚠️ ISSUES REMAIN")
        print("\nPossible solutions:")
        print("1. Try running: python install_globalgenie_simple.py")
        print("2. Create a fresh virtual environment")
        print("3. Check for conflicting Python installations")
        
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)