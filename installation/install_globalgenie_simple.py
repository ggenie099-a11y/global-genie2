#!/usr/bin/env python3
"""
Simple GlobalGenie Installation Script for Windows
Handles Windows command-line quirks properly
"""

import os
import sys
import subprocess
import json
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class SimpleGlobalGenieInstaller:
    """Simple, reliable installer for GlobalGenie"""
    
    def __init__(self):
        self.python_executable = sys.executable
        
    def run_pip_install(self, packages: List[str]) -> Tuple[bool, str]:
        """Install packages using pip with proper Windows handling"""
        if not packages:
            return True, "No packages to install"
        
        # Create the command without extra quotes
        cmd_parts = [self.python_executable, "-m", "pip", "install"] + packages
        
        logger.info(f"Installing: {' '.join(packages)}")
        
        try:
            result = subprocess.run(
                cmd_parts,
                capture_output=True,
                text=True,
                timeout=300,
                encoding='utf-8',
                errors='replace'
            )
            
            if result.returncode == 0:
                logger.info("Installation successful")
                return True, result.stdout
            else:
                logger.error(f"Installation failed: {result.stderr}")
                return False, result.stderr
                
        except Exception as e:
            logger.error(f"Installation error: {e}")
            return False, str(e)
    
    def check_python_version(self) -> bool:
        """Check if Python version is compatible"""
        version = sys.version_info
        if version >= (3, 8):
            logger.info(f"Python {version.major}.{version.minor}.{version.micro} - Compatible")
            return True
        else:
            logger.error(f"Python {version.major}.{version.minor}.{version.micro} - Requires 3.8+")
            return False
    
    def install_core_packages(self) -> bool:
        """Install core packages one by one"""
        logger.info("Installing core dependencies...")
        
        # Install packages individually to avoid quoting issues
        core_packages = [
            "setuptools",
            "wheel", 
            "docstring-parser",
            "httpx",
            "pydantic>=2.0.0,<3.0.0",
            "pydantic-settings",
            "python-dotenv",
            "pyyaml",
            "rich",
            "typer",
            "typing-extensions"
        ]
        
        failed_packages = []
        
        for package in core_packages:
            success, output = self.run_pip_install([package])
            if not success:
                failed_packages.append(package)
                logger.error(f"Failed to install {package}")
        
        if failed_packages:
            logger.error(f"Failed packages: {', '.join(failed_packages)}")
            return False
        
        logger.info("All core dependencies installed successfully")
        return True
    
    def install_globalgenie(self) -> bool:
        """Install GlobalGenie package"""
        logger.info("Installing GlobalGenie...")
        
        # Try different installation strategies
        strategies = [
            ["globalgenie"],
            ["--upgrade", "globalgenie"],
            ["--force-reinstall", "globalgenie"],
            ["--no-cache-dir", "globalgenie"]
        ]
        
        for strategy in strategies:
            logger.info(f"Trying: pip install {' '.join(strategy)}")
            success, output = self.run_pip_install(strategy)
            
            if success:
                logger.info("GlobalGenie installed successfully")
                return True
            else:
                logger.warning(f"Strategy failed: {' '.join(strategy)}")
        
        logger.error("All installation strategies failed")
        return False
    
    def install_optional_packages(self) -> dict:
        """Install optional packages for enhanced functionality"""
        logger.info("Installing optional packages...")
        
        optional_packages = {
            "openai": "openai",
            "anthropic": "anthropic", 
            "requests": "requests",
            "beautifulsoup4": "beautifulsoup4"
        }
        
        results = {}
        for name, package in optional_packages.items():
            logger.info(f"Installing {name}...")
            success, output = self.run_pip_install([package])
            results[name] = success
            
            if success:
                logger.info(f"✓ {name} installed")
            else:
                logger.warning(f"⚠ {name} installation failed (optional)")
        
        return results
    
    def verify_installation(self) -> dict:
        """Verify the installation works"""
        logger.info("Verifying installation...")
        
        tests = {}
        
        # Test basic import
        try:
            import globalgenie
            tests["basic_import"] = True
            logger.info("✓ GlobalGenie import successful")
            
            # Test version
            version = getattr(globalgenie, '__version__', 'unknown')
            tests["version_available"] = version != 'unknown'
            logger.info(f"✓ Version: {version}")
            
        except ImportError as e:
            tests["basic_import"] = False
            tests["version_available"] = False
            logger.error(f"✗ Import failed: {e}")
        
        # Test agent import
        try:
            from globalgenie.agent import Agent
            tests["agent_import"] = True
            logger.info("✓ Agent import successful")
        except ImportError as e:
            tests["agent_import"] = False
            logger.error(f"✗ Agent import failed: {e}")
        
        # Test CLI
        try:
            from globalgenie.cli.entrypoint import globalgenie_cli
            tests["cli_import"] = True
            logger.info("✓ CLI import successful")
        except ImportError as e:
            tests["cli_import"] = False
            logger.error(f"✗ CLI import failed: {e}")
        
        return tests
    
    def create_test_file(self) -> bool:
        """Create a simple test file"""
        test_content = '''#!/usr/bin/env python3
"""Test GlobalGenie installation"""

def test_installation():
    try:
        import globalgenie
        print("✓ GlobalGenie imported successfully")
        
        version = getattr(globalgenie, '__version__', 'unknown')
        print(f"✓ Version: {version}")
        
        from globalgenie.agent import Agent
        print("✓ Agent class available")
        
        print("\\n🎉 Installation test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_installation()
    exit(0 if success else 1)
'''
        
        try:
            with open("test_globalgenie.py", "w", encoding='utf-8') as f:
                f.write(test_content)
            logger.info("Created test file: test_globalgenie.py")
            return True
        except Exception as e:
            logger.error(f"Failed to create test file: {e}")
            return False
    
    def run_installation(self) -> dict:
        """Run the complete installation process"""
        print("GlobalGenie Simple Installation")
        print("=" * 40)
        
        results = {
            "python_compatible": False,
            "core_installed": False,
            "globalgenie_installed": False,
            "optional_packages": {},
            "verification": {},
            "test_file_created": False
        }
        
        # Check Python version
        if not self.check_python_version():
            return results
        results["python_compatible"] = True
        
        # Install core dependencies
        print("\nStep 1: Installing core dependencies...")
        if not self.install_core_packages():
            print("❌ Core dependencies installation failed")
            return results
        results["core_installed"] = True
        
        # Install GlobalGenie
        print("\nStep 2: Installing GlobalGenie...")
        if not self.install_globalgenie():
            print("❌ GlobalGenie installation failed")
            return results
        results["globalgenie_installed"] = True
        
        # Install optional packages
        print("\nStep 3: Installing optional packages...")
        results["optional_packages"] = self.install_optional_packages()
        
        # Verify installation
        print("\nStep 4: Verifying installation...")
        results["verification"] = self.verify_installation()
        
        # Create test file
        print("\nStep 5: Creating test file...")
        results["test_file_created"] = self.create_test_file()
        
        return results
    
    def print_summary(self, results: dict):
        """Print installation summary"""
        print("\n" + "=" * 50)
        print("INSTALLATION SUMMARY")
        print("=" * 50)
        
        # Core results
        print(f"Python Compatible: {'✓' if results['python_compatible'] else '✗'}")
        print(f"Core Dependencies: {'✓' if results['core_installed'] else '✗'}")
        print(f"GlobalGenie Package: {'✓' if results['globalgenie_installed'] else '✗'}")
        
        # Optional packages
        if results["optional_packages"]:
            print("\nOptional Packages:")
            for pkg, success in results["optional_packages"].items():
                status = "✓" if success else "✗"
                print(f"  {pkg}: {status}")
        
        # Verification
        if results["verification"]:
            print("\nVerification Tests:")
            for test, success in results["verification"].items():
                status = "✓" if success else "✗"
                print(f"  {test}: {status}")
        
        # Overall status
        verification = results.get("verification", {})
        if verification:
            passed = sum(verification.values())
            total = len(verification)
            success_rate = (passed / total) * 100 if total > 0 else 0
            
            print(f"\nOverall Success Rate: {success_rate:.1f}% ({passed}/{total})")
            
            if success_rate == 100:
                print("\n🎉 INSTALLATION SUCCESSFUL!")
                print("GlobalGenie is ready to use.")
                print("\nNext steps:")
                print("1. Run: python test_globalgenie.py")
                print("2. Check EXAMPLES.md for usage examples")
            elif success_rate >= 75:
                print("\n✅ INSTALLATION MOSTLY SUCCESSFUL")
                print("Some features may not be available.")
            else:
                print("\n⚠️ INSTALLATION ISSUES DETECTED")
                print("Please review the errors above.")


def main():
    """Main installation function"""
    installer = SimpleGlobalGenieInstaller()
    
    try:
        results = installer.run_installation()
        installer.print_summary(results)
        
        # Save results
        with open("installation_results.json", "w", encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\nResults saved to: installation_results.json")
        
        # Return exit code based on success
        verification = results.get("verification", {})
        if verification and sum(verification.values()) == len(verification):
            return 0  # Perfect success
        elif results.get("globalgenie_installed", False):
            return 1  # Partial success
        else:
            return 2  # Failed
            
    except KeyboardInterrupt:
        print("\nInstallation cancelled by user")
        return 130
    except Exception as e:
        logger.error(f"Installation failed: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)