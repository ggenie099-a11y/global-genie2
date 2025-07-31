#!/usr/bin/env python3
"""
Investigate OpenAI API and ChatCompletionAudio availability
Check if this feature actually exists in current OpenAI versions
"""

import sys
import subprocess

def check_installed_version():
    """Check what version is actually installed"""
    try:
        import openai
        version = getattr(openai, '__version__', 'unknown')
        print(f"Installed OpenAI version: {version}")
        print(f"OpenAI location: {openai.__file__}")
        return version
    except ImportError:
        print("OpenAI not installed")
        return None

def check_available_types():
    """Check what's actually available in openai.types.chat"""
    try:
        import openai.types.chat as chat_types
        print(f"\nAvailable in openai.types.chat:")
        print(f"Module location: {chat_types.__file__}")
        
        # List all available attributes
        available_attrs = [attr for attr in dir(chat_types) if not attr.startswith('_')]
        print(f"Available attributes: {len(available_attrs)}")
        
        for attr in sorted(available_attrs):
            print(f"  - {attr}")
        
        # Check specifically for ChatCompletionAudio
        has_audio = hasattr(chat_types, 'ChatCompletionAudio')
        print(f"\nChatCompletionAudio available: {has_audio}")
        
        return available_attrs
        
    except ImportError as e:
        print(f"Failed to import openai.types.chat: {e}")
        return []

def check_openai_changelog():
    """Check when ChatCompletionAudio was introduced"""
    print("\n=== CHATCOMPLETIONAUDIO RESEARCH ===")
    print("Checking if ChatCompletionAudio is a real OpenAI API feature...")
    
    # Let's see what audio-related features exist
    try:
        import openai.types.chat as chat_types
        audio_related = [attr for attr in dir(chat_types) if 'audio' in attr.lower()]
        print(f"Audio-related attributes: {audio_related}")
        
        # Check for completion-related types
        completion_related = [attr for attr in dir(chat_types) if 'completion' in attr.lower()]
        print(f"Completion-related attributes: {completion_related}")
        
    except ImportError:
        print("Cannot check audio-related features")

def check_latest_pypi_version():
    """Check what's the latest version on PyPI"""
    print("\n=== CHECKING PYPI ===")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "index", "versions", "openai"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("PyPI version info:")
            print(result.stdout)
        else:
            # Try alternative method
            result = subprocess.run(
                [sys.executable, "-m", "pip", "search", "openai"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                print("PyPI search results:")
                print(result.stdout)
            else:
                print("Could not check PyPI versions")
                
    except Exception as e:
        print(f"Error checking PyPI: {e}")

def test_alternative_imports():
    """Test if there are alternative ways to get audio functionality"""
    print("\n=== TESTING ALTERNATIVE IMPORTS ===")
    
    alternatives = [
        "openai.types.chat.completion_create_params",
        "openai.types.chat_completion_audio",
        "openai.types.audio",
        "openai.audio",
        "openai.types.completion_audio"
    ]
    
    for alt in alternatives:
        try:
            parts = alt.split('.')
            module_path = '.'.join(parts[:-1])
            class_name = parts[-1]
            
            module = __import__(module_path, fromlist=[class_name])
            if hasattr(module, class_name):
                print(f"✓ Found: {alt}")
            else:
                print(f"✗ Not found: {alt}")
        except ImportError:
            print(f"✗ Cannot import: {alt}")

def check_globalgenie_compatibility():
    """Check if we can make GlobalGenie work without ChatCompletionAudio"""
    print("\n=== GLOBALGENIE COMPATIBILITY CHECK ===")
    
    # Let's see if ChatCompletionAudio is actually used in GlobalGenie
    try:
        # Read the GlobalGenie source to see how ChatCompletionAudio is used
        import os
        gg_path = "libs/globalgenie/globalgenie/models/openai/chat.py"
        
        if os.path.exists(gg_path):
            with open(gg_path, 'r') as f:
                content = f.read()
                
            # Count usage of ChatCompletionAudio
            audio_usage = content.count('ChatCompletionAudio')
            print(f"ChatCompletionAudio mentioned {audio_usage} times in GlobalGenie")
            
            # Check if it's actually used or just imported
            if 'ChatCompletionAudio' in content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if 'ChatCompletionAudio' in line and not line.strip().startswith('#'):
                        print(f"Line {i+1}: {line.strip()}")
            
            return audio_usage
        else:
            print("Cannot find GlobalGenie source file")
            return 0
            
    except Exception as e:
        print(f"Error checking GlobalGenie source: {e}")
        return 0

def suggest_workaround():
    """Suggest potential workarounds"""
    print("\n=== SUGGESTED WORKAROUNDS ===")
    
    print("1. Check if ChatCompletionAudio is actually needed:")
    print("   - It might be an optional import")
    print("   - GlobalGenie might work without audio features")
    
    print("\n2. Try different OpenAI versions:")
    print("   - pip install openai==1.40.0")
    print("   - pip install openai==1.35.0") 
    print("   - pip install openai==1.30.0")
    
    print("\n3. Check GlobalGenie version compatibility:")
    print("   - This GlobalGenie version might be too new for current OpenAI")
    print("   - Or OpenAI removed ChatCompletionAudio in recent versions")
    
    print("\n4. Modify GlobalGenie source (advanced):")
    print("   - Comment out ChatCompletionAudio import")
    print("   - Make it an optional import with try/except")

def main():
    """Main investigation function"""
    print("OpenAI API Investigation")
    print("=" * 30)
    
    # Check current state
    version = check_installed_version()
    available_types = check_available_types()
    
    # Research the issue
    check_openai_changelog()
    check_latest_pypi_version()
    test_alternative_imports()
    
    # Check GlobalGenie usage
    audio_usage = check_globalgenie_compatibility()
    
    # Provide recommendations
    suggest_workaround()
    
    # Summary
    print("\n" + "=" * 50)
    print("INVESTIGATION SUMMARY")
    print("=" * 50)
    print(f"OpenAI version: {version}")
    print(f"Available chat types: {len(available_types)}")
    print(f"ChatCompletionAudio available: {'ChatCompletionAudio' in available_types}")
    print(f"GlobalGenie audio usage: {audio_usage} references")
    
    if 'ChatCompletionAudio' not in available_types:
        print("\n🔍 FINDING: ChatCompletionAudio is not available in current OpenAI")
        print("This suggests either:")
        print("  - Feature was removed from OpenAI API")
        print("  - Feature doesn't exist yet")
        print("  - GlobalGenie expects a different OpenAI version")
        print("  - This is an optional feature that can be worked around")

if __name__ == "__main__":
    main()