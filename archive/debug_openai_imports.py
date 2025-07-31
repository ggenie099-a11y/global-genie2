#!/usr/bin/env python3
"""
Debug OpenAI Import Issues
Check exactly what's available in the installed OpenAI package
"""

def debug_openai_imports():
    """Debug what's available in the OpenAI package"""
    print("=== OPENAI PACKAGE DEBUG ===")
    
    try:
        import openai
        print(f"✓ OpenAI package imported successfully")
        print(f"  Version: {getattr(openai, '__version__', 'unknown')}")
        print(f"  Location: {openai.__file__}")
        print()
        
        # Test basic imports that GlobalGenie needs
        imports_to_test = [
            ("openai", "APIConnectionError"),
            ("openai", "APIStatusError"), 
            ("openai", "RateLimitError"),
            ("openai", "AsyncOpenAI"),
            ("openai", "OpenAI"),
            ("openai.types.chat", "ChatCompletionAudio"),
            ("openai.types.chat.chat_completion", "ChatCompletion"),
            ("openai.types.chat.chat_completion_chunk", "ChatCompletionChunk"),
            ("openai.types.chat.chat_completion_chunk", "ChoiceDelta"),
            ("openai.types.chat.chat_completion_chunk", "ChoiceDeltaToolCall"),
        ]
        
        print("Testing specific imports that GlobalGenie needs:")
        print("-" * 50)
        
        failed_imports = []
        
        for module_name, class_name in imports_to_test:
            try:
                module = __import__(module_name, fromlist=[class_name])
                if hasattr(module, class_name):
                    print(f"✓ {module_name}.{class_name}")
                else:
                    print(f"✗ {module_name}.{class_name} - Not found in module")
                    failed_imports.append(f"{module_name}.{class_name}")
            except ImportError as e:
                print(f"✗ {module_name}.{class_name} - Import error: {e}")
                failed_imports.append(f"{module_name}.{class_name}")
        
        print()
        
        if failed_imports:
            print("FAILED IMPORTS:")
            for failed in failed_imports:
                print(f"  - {failed}")
            print()
            print("This explains why GlobalGenie's OpenAI integration fails!")
            
            # Check OpenAI version compatibility
            version = getattr(openai, '__version__', 'unknown')
            print(f"\nInstalled OpenAI version: {version}")
            print("GlobalGenie might require a specific OpenAI version.")
            
            return False
        else:
            print("✓ All required imports are available!")
            return True
            
    except ImportError as e:
        print(f"✗ Failed to import openai package: {e}")
        return False

def test_manual_openai_chat_import():
    """Test the exact import that's failing in GlobalGenie"""
    print("\n=== TESTING GLOBALGENIE'S EXACT IMPORTS ===")
    
    try:
        # This is the exact import block from GlobalGenie
        from openai import APIConnectionError, APIStatusError, RateLimitError
        from openai import AsyncOpenAI as AsyncOpenAIClient
        from openai import OpenAI as OpenAIClient
        from openai.types.chat import ChatCompletionAudio
        from openai.types.chat.chat_completion import ChatCompletion
        from openai.types.chat.chat_completion_chunk import (
            ChatCompletionChunk,
            ChoiceDelta,
            ChoiceDeltaToolCall,
        )
        
        print("✓ All GlobalGenie OpenAI imports successful!")
        print("  This means the issue might be elsewhere...")
        
        # Test if we can now import GlobalGenie's OpenAI models
        try:
            from globalgenie.models.openai import OpenAIChat
            print("✓ GlobalGenie OpenAIChat import successful!")
            return True
        except ImportError as e:
            print(f"✗ GlobalGenie OpenAIChat import still fails: {e}")
            return False
            
    except ImportError as e:
        print(f"✗ GlobalGenie's exact imports failed: {e}")
        print("  This is the root cause of the issue!")
        return False

def suggest_fixes():
    """Suggest fixes based on findings"""
    print("\n=== SUGGESTED FIXES ===")
    
    # Check current OpenAI version
    try:
        import openai
        version = getattr(openai, '__version__', 'unknown')
        print(f"Current OpenAI version: {version}")
        
        # Suggest version-specific fixes
        if version == 'unknown':
            print("1. Reinstall OpenAI: pip install --force-reinstall openai")
        else:
            print("1. Try upgrading OpenAI: pip install --upgrade openai")
            print("2. Try specific version: pip install openai==1.51.0")
            print("3. Try beta version: pip install openai --pre")
        
        print("4. Clear Python cache and restart")
        print("5. Use virtual environment to avoid conflicts")
        
    except ImportError:
        print("1. Install OpenAI: pip install openai")
        print("2. Check Python environment")

def main():
    """Main debug function"""
    print("OpenAI Import Debug Tool")
    print("=" * 30)
    
    # Step 1: Debug what's available
    imports_ok = debug_openai_imports()
    
    # Step 2: Test exact GlobalGenie imports
    gg_imports_ok = test_manual_openai_chat_import()
    
    # Step 3: Provide suggestions
    suggest_fixes()
    
    # Summary
    print("\n" + "=" * 40)
    print("DEBUG SUMMARY")
    print("=" * 40)
    print(f"OpenAI imports available: {'✓' if imports_ok else '✗'}")
    print(f"GlobalGenie integration works: {'✓' if gg_imports_ok else '✗'}")
    
    if gg_imports_ok:
        print("\n🎉 SUCCESS! The issue has been resolved!")
        print("Try running your verification script again.")
    else:
        print("\n⚠️ Issue identified. Follow the suggested fixes above.")
    
    return 0 if gg_imports_ok else 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)