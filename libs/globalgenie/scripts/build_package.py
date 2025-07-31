#!/usr/bin/env python3
"""
GlobalGenie Package Build Script
Professional PyPI package building and validation
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import tempfile
import json

def run_command(cmd, cwd=None, check=True):
    """Run a command and return the result"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running command: {cmd}")
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        sys.exit(1)
    return result

def clean_build_artifacts():
    """Clean previous build artifacts"""
    print("🧹 Cleaning build artifacts...")
    
    artifacts = [
        "build",
        "dist", 
        "*.egg-info",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache"
    ]
    
    for artifact in artifacts:
        for path in Path(".").glob(artifact):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"  Removed directory: {path}")
            elif path.is_file():
                path.unlink()
                print(f"  Removed file: {path}")

def validate_package_structure():
    """Validate package structure before building"""
    print("🔍 Validating package structure...")
    
    required_files = [
        "pyproject.toml",
        "setup.py", 
        "README.md",
        "LICENSE",
        "MANIFEST.in",
        "globalgenie/__init__.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        sys.exit(1)
    
    print("✅ Package structure validation passed")

def run_tests():
    """Run tests before building"""
    print("🧪 Running tests...")
    
    # Check if tests directory exists
    if Path("tests").exists():
        result = run_command("python -m pytest tests/ -v", check=False)
        if result.returncode != 0:
            print("⚠️  Some tests failed, but continuing with build...")
        else:
            print("✅ All tests passed")
    else:
        print("ℹ️  No tests directory found, skipping tests")

def run_linting():
    """Run code quality checks"""
    print("🔍 Running code quality checks...")
    
    # Run ruff if available
    result = run_command("python -m ruff check globalgenie/", check=False)
    if result.returncode == 0:
        print("✅ Ruff linting passed")
    else:
        print("⚠️  Ruff linting issues found, but continuing...")
    
    # Run mypy if available
    result = run_command("python -m mypy globalgenie/", check=False)
    if result.returncode == 0:
        print("✅ MyPy type checking passed")
    else:
        print("⚠️  MyPy type checking issues found, but continuing...")

def build_package():
    """Build the package"""
    print("📦 Building package...")
    
    # Build source distribution
    run_command("python -m build --sdist")
    print("✅ Source distribution built")
    
    # Build wheel distribution
    run_command("python -m build --wheel")
    print("✅ Wheel distribution built")

def validate_built_package():
    """Validate the built package"""
    print("🔍 Validating built package...")
    
    # Check if dist directory exists and has files
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("❌ No dist directory found")
        sys.exit(1)
    
    dist_files = list(dist_dir.glob("*"))
    if not dist_files:
        print("❌ No distribution files found")
        sys.exit(1)
    
    print(f"📦 Built packages:")
    for file in dist_files:
        print(f"  - {file.name} ({file.stat().st_size} bytes)")
    
    # Run twine check if available
    result = run_command("python -m twine check dist/*", check=False)
    if result.returncode == 0:
        print("✅ Twine validation passed")
    else:
        print("⚠️  Twine validation issues found")

def test_installation():
    """Test package installation in a virtual environment"""
    print("🧪 Testing package installation...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        venv_dir = Path(temp_dir) / "test_env"
        
        # Create virtual environment
        run_command(f"python -m venv {venv_dir}")
        
        # Determine activation script
        if sys.platform == "win32":
            activate_script = venv_dir / "Scripts" / "activate.bat"
            pip_cmd = f"{venv_dir}/Scripts/pip"
        else:
            activate_script = venv_dir / "bin" / "activate"
            pip_cmd = f"{venv_dir}/bin/pip"
        
        # Install the package
        wheel_file = next(Path("dist").glob("*.whl"))
        run_command(f"{pip_cmd} install {wheel_file}")
        
        # Test import
        if sys.platform == "win32":
            python_cmd = f"{venv_dir}/Scripts/python"
        else:
            python_cmd = f"{venv_dir}/bin/python"
            
        result = run_command(f'{python_cmd} -c "import globalgenie; print(globalgenie.__version__)"')
        print(f"✅ Package installation test passed: {result.stdout.strip()}")

def generate_package_info():
    """Generate package information"""
    print("📋 Generating package information...")
    
    # Get package info
    result = run_command("python setup.py --name --version --description", check=False)
    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        if len(lines) >= 3:
            name, version, description = lines[0], lines[1], lines[2]
            
            info = {
                "name": name,
                "version": version,
                "description": description,
                "files": [f.name for f in Path("dist").glob("*")],
                "build_timestamp": subprocess.run(
                    ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], 
                    capture_output=True, text=True
                ).stdout.strip()
            }
            
            with open("dist/package-info.json", "w") as f:
                json.dump(info, f, indent=2)
            
            print(f"📦 Package: {name} v{version}")
            print(f"📝 Description: {description}")

def main():
    """Main build process"""
    print("🚀 Starting GlobalGenie package build process...")
    
    # Change to package directory
    package_dir = Path(__file__).parent.parent
    os.chdir(package_dir)
    
    try:
        # Build process steps
        clean_build_artifacts()
        validate_package_structure()
        run_linting()
        run_tests()
        build_package()
        validate_built_package()
        test_installation()
        generate_package_info()
        
        print("\n🎉 Package build completed successfully!")
        print("\n📦 Distribution files:")
        for file in Path("dist").glob("*"):
            print(f"  - {file}")
        
        print("\n🚀 Ready for PyPI upload!")
        print("   Run: python -m twine upload dist/*")
        
    except KeyboardInterrupt:
        print("\n❌ Build process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Build process failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()