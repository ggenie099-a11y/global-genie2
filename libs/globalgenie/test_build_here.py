#!/usr/bin/env python3
"""
Test the build from the package directory
"""

import subprocess
import sys
from pathlib import Path

def test_build():
    print("🔧 Testing GlobalGenie package build...")
    print("=" * 50)
    
    # Test the build from current directory
    try:
        result = subprocess.run([
            sys.executable, "-m", "build", "--sdist", "--wheel"
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ Build successful!")
            
            # Check created files
            dist_dir = Path("dist")
            if dist_dir.exists():
                files = list(dist_dir.glob("*"))
                print(f"📦 Created {len(files)} distribution files:")
                for file in files:
                    print(f"   - {file.name}")
                    print(f"     Size: {file.stat().st_size:,} bytes")
            
            return True
        else:
            print("❌ Build failed!")
            if result.stdout:
                print("STDOUT:", result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Build timed out!")
        return False
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def test_package_info():
    """Test package metadata"""
    print("\n📋 Testing package metadata...")
    
    # Check if pyproject.toml exists
    if Path("pyproject.toml").exists():
        print("✅ pyproject.toml found")
    else:
        print("❌ pyproject.toml not found")
    
    # Check if setup.py exists
    if Path("setup.py").exists():
        print("✅ setup.py found")
    else:
        print("❌ setup.py not found")
    
    # Check if README exists
    if Path("README.md").exists():
        print("✅ README.md found")
    else:
        print("❌ README.md not found")
    
    # Check if LICENSE exists
    if Path("LICENSE").exists():
        print("✅ LICENSE found")
    else:
        print("❌ LICENSE not found")

if __name__ == "__main__":
    test_package_info()
    success = test_build()
    
    if success:
        print("\n🎉 Package build successful!")
        print("\nNext steps:")
        print("1. Check the built files in dist/")
        print("2. Test installation: pip install dist/*.whl")
        print("3. Upload to PyPI: twine upload dist/*")
    else:
        print("\n⚠️  Please fix the build errors before proceeding.")