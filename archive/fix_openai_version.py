#!/usr/bin/env python3
"""
Fix OpenAI Version Compatibility Issue
Upgrades OpenAI to a version compatible with GlobalGenie
"""

import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_pip_command(args):
    """Run pip command with proper error handling"""
    cmd = [sys.executable, "-m", "pip"] + args
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

def check_current_version():
    """Check current OpenAI version"""
    try:
        import openai
        version = getattr(openai, '__version__', 'unknown')
        print(f"Current OpenAI version: {version}")
        return version
    except ImportError:
        print("OpenAI not installed")
        return None

def upgrade_openai():
    """Upgrade OpenAI to latest version"""
    print("=== UPGRADING OPENAI ===")
    
    # Try different upgrade strategies
    strategies = [
        ["install", "--upgrade", "openai"],
        ["install", "--upgrade", "--force-reinstall", "openai"],
        ["install", "openai>=1.50.0"],  # Ensure we get a recent version
        ["install", "--no-cache-dir", "--upgrade", "openai"]
    ]
    
    for i, strategy in enumerate(strategies, 1):
        print(f"\nStrategy {i}: pip {' '.join(strategy)}")
        success, output = run_pip_command(strategy)
        
        if success:
            # Check if the problematic import now works
            try:
                from openai.types.chat import ChatCompletionAudio
                print("✓ ChatCompletionAudio import successful!")
                return True
            except ImportError as e:
                print(f"⚠ ChatCompletionAudio still not available: {e}")
                continue
        else:
            print(f"Strategy {i} failed")
    
    return False

def test_globalgenie_integration():
    """Test if GlobalGenie OpenAI integration now works"""
    print("\n=== TESTING GLOBALGENIE INTEGRATION ===")
    
    try:
        # Clear any cached imports
        import sys
        modules_to_clear = [
            'globalgenie.models.openai.chat',
            'globalgenie.models.openai',
            'openai.types.chat'
        ]
        
        for module in modules_to_clear:
            if module in sys.modules:
                del sys.modules[module]
        
        # Test the import that was failing
        from globalgenie.models.openai import OpenAIChat
        print("✓ GlobalGenie OpenAIChat import: SUCCESS")
        
        # Test basic instantiation
        try:
            model = OpenAIChat(id="gpt-4", api_key="test-key")
            print("✓ OpenAIChat instantiation: SUCCESS")
            
            # Test agent creation
            from globalgenie.agent import Agent
            agent = Agent(
                model=model,
                instructions="Test agent"
            )
            print("✓ Agent creation with OpenAI model: SUCCESS")
            
            return True
            
        except Exception as e:
            print(f"⚠ OpenAIChat usage: FAILED - {e}")
            return False
            
    except ImportError as e:
        print(f"✗ GlobalGenie OpenAIChat import: FAILED - {e}")
        return False

def main():
    """Main fix function"""
    print("OpenAI Version Compatibility Fix")
    print("=" * 40)
    
    # Step 1: Check current version
    print("=== CURRENT STATE ===")
    current_version = check_current_version()
    
    if current_version == "1.3.7":
        print("✓ Issue confirmed: OpenAI 1.3.7 is too old for GlobalGenie")
        print("  GlobalGenie requires OpenAI 1.50+ for ChatCompletionAudio")
    
    # Step 2: Upgrade OpenAI
    print(f"\n=== UPGRADING FROM VERSION {current_version} ===")
    upgrade_success = upgrade_openai()
    
    if not upgrade_success:
        print("❌ Failed to upgrade OpenAI to compatible version")
        return 1
    
    # Step 3: Check new version
    print("\n=== CHECKING NEW VERSION ===")
    new_version = check_current_version()
    print(f"Upgraded from {current_version} to {new_version}")
    
    # Step 4: Test GlobalGenie integration
    integration_works = test_globalgenie_integration()
    
    # Step 5: Summary
    print("\n" + "=" * 50)
    print("OPENAI VERSION FIX SUMMARY")
    print("=" * 50)
    print(f"Original version: {current_version}")
    print(f"New version: {new_version}")
    print(f"Upgrade successful: {'✓' if upgrade_success else '✗'}")
    print(f"GlobalGenie integration: {'✓' if integration_works else '✗'}")
    
    if integration_works:
        print("\n🎉 SUCCESS! OpenAI version issue resolved!")
        print("\nGlobalGenie can now use OpenAI models properly.")
        print("\nNext steps:")
        print("1. Run: python verify_without_dependencies.py")
        print("2. Test creating agents with OpenAI models")
        print("3. Try the comprehensive test suite")
        
        # Show example usage
        print("\nExample usage:")
        print("```python")
        print("from globalgenie.agent import Agent")
        print("from globalgenie.models.openai import OpenAIChat")
        print("")
        print("agent = Agent(")
        print('    model=OpenAIChat(id="gpt-4"),')
        print('    instructions="You are a helpful assistant."')
        print(")")
        print("```")
        
        return 0
    else:
        print("\n⚠️ Upgrade completed but integration issues remain")
        print("This might indicate other compatibility issues.")
        print("\nTry:")
        print("1. Restart Python/terminal")
        print("2. Clear Python cache: python -Bc 'import py_compile'")
        print("3. Use a fresh virtual environment")
        
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)