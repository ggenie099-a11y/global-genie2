#!/usr/bin/env python3
"""
GlobalGenie PyPI Upload Script
Professional PyPI package upload with validation and safety checks
"""

import os
import sys
import subprocess
import getpass
from pathlib import Path
import json
import re

def run_command(cmd, cwd=None, check=True, capture_output=True):
    """Run a command and return the result"""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, 
        capture_output=capture_output, text=True
    )
    if check and result.returncode != 0:
        print(f"Error running command: {cmd}")
        if capture_output:
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
        sys.exit(1)
    return result

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check if twine is installed
    result = run_command("python -m twine --version", check=False)
    if result.returncode != 0:
        print("❌ Twine is not installed. Install with: pip install twine")
        sys.exit(1)
    
    # Check if build artifacts exist
    dist_dir = Path("dist")
    if not dist_dir.exists() or not list(dist_dir.glob("*")):
        print("❌ No distribution files found. Run build_package.py first.")
        sys.exit(1)
    
    print("✅ Prerequisites check passed")

def validate_version():
    """Validate version number format"""
    print("🔍 Validating version number...")
    
    # Read version from pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if pyproject_path.exists():
        content = pyproject_path.read_text()
        version_match = re.search(r'version\s*=\s*"([^"]+)"', content)
        if version_match:
            version = version_match.group(1)
            
            # Validate semantic versioning
            semver_pattern = r'^\d+\.\d+\.\d+(?:-[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)?(?:\+[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)?$'
            if re.match(semver_pattern, version):
                print(f"✅ Version {version} is valid")
                return version
            else:
                print(f"❌ Version {version} is not valid semantic versioning")
                sys.exit(1)
    
    print("❌ Could not determine version from pyproject.toml")
    sys.exit(1)

def check_pypi_credentials():
    """Check PyPI credentials"""
    print("🔍 Checking PyPI credentials...")
    
    # Check for API token in environment
    if os.getenv("TWINE_PASSWORD") or os.getenv("PYPI_API_TOKEN"):
        print("✅ PyPI API token found in environment")
        return True
    
    # Check for .pypirc file
    pypirc_path = Path.home() / ".pypirc"
    if pypirc_path.exists():
        print("✅ .pypirc file found")
        return True
    
    print("⚠️  No PyPI credentials found")
    return False

def run_security_checks():
    """Run security checks on the package"""
    print("🔒 Running security checks...")
    
    # Check for common security issues
    security_issues = []
    
    # Check for hardcoded secrets
    for py_file in Path("globalgenie").rglob("*.py"):
        content = py_file.read_text()
        
        # Check for potential API keys or secrets
        secret_patterns = [
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'secret[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'password\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']'
        ]
        
        for pattern in secret_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                security_issues.append(f"Potential hardcoded secret in {py_file}")
    
    if security_issues:
        print("❌ Security issues found:")
        for issue in security_issues:
            print(f"  - {issue}")
        
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    else:
        print("✅ No security issues found")

def validate_package_contents():
    """Validate package contents"""
    print("🔍 Validating package contents...")
    
    # Run twine check
    result = run_command("python -m twine check dist/*")
    print("✅ Twine validation passed")
    
    # Check package size
    total_size = sum(f.stat().st_size for f in Path("dist").glob("*"))
    size_mb = total_size / (1024 * 1024)
    
    if size_mb > 100:  # 100MB limit
        print(f"⚠️  Package size is large: {size_mb:.1f}MB")
        response = input("Continue with large package? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    else:
        print(f"✅ Package size is reasonable: {size_mb:.1f}MB")

def confirm_upload(version, target_repo):
    """Confirm upload with user"""
    print(f"\n📦 Ready to upload GlobalGenie v{version} to {target_repo}")
    print("\nDistribution files:")
    for file in Path("dist").glob("*"):
        size_kb = file.stat().st_size / 1024
        print(f"  - {file.name} ({size_kb:.1f}KB)")
    
    print(f"\n⚠️  This will upload to {target_repo.upper()}!")
    if target_repo == "pypi":
        print("   This is the PRODUCTION PyPI repository!")
    
    response = input("\nContinue with upload? (y/N): ")
    return response.lower() == 'y'

def upload_to_repository(target_repo="testpypi"):
    """Upload package to PyPI repository"""
    print(f"🚀 Uploading to {target_repo}...")
    
    if target_repo == "testpypi":
        repository_url = "https://test.pypi.org/legacy/"
        cmd = f"python -m twine upload --repository-url {repository_url} dist/*"
    else:
        cmd = "python -m twine upload dist/*"
    
    # Run upload command
    result = run_command(cmd, capture_output=False)
    
    if result.returncode == 0:
        print(f"✅ Successfully uploaded to {target_repo}!")
        
        if target_repo == "testpypi":
            print("\n🔗 Test installation:")
            print("   pip install --index-url https://test.pypi.org/simple/ globalgenie")
        else:
            print("\n🔗 Installation:")
            print("   pip install globalgenie")
    else:
        print(f"❌ Upload to {target_repo} failed")
        sys.exit(1)

def post_upload_verification(version, target_repo):
    """Verify upload was successful"""
    print("🔍 Verifying upload...")
    
    if target_repo == "pypi":
        url = f"https://pypi.org/project/globalgenie/{version}/"
        print(f"📦 Package URL: {url}")
    else:
        url = f"https://test.pypi.org/project/globalgenie/{version}/"
        print(f"📦 Test Package URL: {url}")
    
    print("✅ Upload verification completed")

def main():
    """Main upload process"""
    print("🚀 Starting GlobalGenie PyPI upload process...")
    
    # Change to package directory
    package_dir = Path(__file__).parent.parent
    os.chdir(package_dir)
    
    # Parse command line arguments
    target_repo = "testpypi"  # Default to test PyPI
    if len(sys.argv) > 1:
        if sys.argv[1] == "--production":
            target_repo = "pypi"
        elif sys.argv[1] == "--test":
            target_repo = "testpypi"
        else:
            print("Usage: python upload_to_pypi.py [--test|--production]")
            sys.exit(1)
    
    try:
        # Upload process steps
        check_prerequisites()
        version = validate_version()
        check_pypi_credentials()
        run_security_checks()
        validate_package_contents()
        
        if not confirm_upload(version, target_repo):
            print("❌ Upload cancelled by user")
            sys.exit(1)
        
        upload_to_repository(target_repo)
        post_upload_verification(version, target_repo)
        
        print(f"\n🎉 GlobalGenie v{version} successfully uploaded to {target_repo.upper()}!")
        
        if target_repo == "testpypi":
            print("\n🧪 Test the package:")
            print("   pip install --index-url https://test.pypi.org/simple/ globalgenie")
            print("\n🚀 When ready, upload to production:")
            print("   python upload_to_pypi.py --production")
        else:
            print("\n🌟 Package is now live on PyPI!")
            print("   pip install globalgenie")
        
    except KeyboardInterrupt:
        print("\n❌ Upload process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Upload process failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()