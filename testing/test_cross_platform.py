#!/usr/bin/env python3
"""
Cross-Platform Installation Test for GlobalGenie
Tests installation across Windows, macOS, and Linux environments
"""

import os
import sys
import platform
import subprocess
import tempfile
import json
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CrossPlatformTester:
    """Test GlobalGenie installation across different platforms"""
    
    def __init__(self):
        self.platform_info = self._get_platform_info()
        self.test_results = {}
    
    def _get_platform_info(self) -> Dict[str, str]:
        """Get detailed platform information"""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "architecture": platform.architecture(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "python_compiler": platform.python_compiler(),
        }
    
    def _run_command(self, command: str, shell: bool = None) -> Tuple[bool, str, str]:
        """Run command with platform-appropriate settings"""
        if shell is None:
            shell = platform.system() == "Windows"
        
        try:
            result = subprocess.run(
                command if shell else command.split(),
                shell=shell,
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def test_platform_specific_installation(self) -> Dict[str, bool]:
        """Test platform-specific installation methods"""
        results = {}
        
        system = platform.system()
        
        if system == "Windows":
            results.update(self._test_windows_installation())
        elif system == "Darwin":  # macOS
            results.update(self._test_macos_installation())
        elif system == "Linux":
            results.update(self._test_linux_installation())
        else:
            logger.warning(f"Unsupported platform: {system}")
            results["platform_supported"] = False
        
        return results
    
    def _test_windows_installation(self) -> Dict[str, bool]:
        """Test Windows-specific installation scenarios"""
        results = {"platform": "Windows"}
        
        # Test with different Python installations
        python_commands = ["python", "py", "python3"]
        
        for cmd in python_commands:
            success, stdout, stderr = self._run_command(f"{cmd} --version")
            if success:
                results[f"{cmd}_available"] = True
                
                # Test pip installation
                pip_success, _, _ = self._run_command(f"{cmd} -m pip install --user globalgenie --dry-run")
                results[f"{cmd}_pip_compatible"] = pip_success
            else:
                results[f"{cmd}_available"] = False
                results[f"{cmd}_pip_compatible"] = False
        
        # Test Windows-specific paths
        results["windows_paths"] = self._test_windows_paths()
        
        # Test PowerShell compatibility
        ps_success, _, _ = self._run_command("powershell -Command \"python --version\"")
        results["powershell_compatible"] = ps_success
        
        # Test Command Prompt compatibility
        cmd_success, _, _ = self._run_command("cmd /c python --version")
        results["cmd_compatible"] = cmd_success
        
        return results
    
    def _test_macos_installation(self) -> Dict[str, bool]:
        """Test macOS-specific installation scenarios"""
        results = {"platform": "macOS"}
        
        # Test system Python vs Homebrew Python
        python_locations = [
            "/usr/bin/python3",
            "/opt/homebrew/bin/python3",
            "/usr/local/bin/python3"
        ]
        
        for python_path in python_locations:
            if os.path.exists(python_path):
                results[f"python_{python_path.replace('/', '_')}_available"] = True
                
                # Test installation with this Python
                pip_success, _, _ = self._run_command(f"{python_path} -m pip install --user globalgenie --dry-run")
                results[f"python_{python_path.replace('/', '_')}_pip_compatible"] = pip_success
            else:
                results[f"python_{python_path.replace('/', '_')}_available"] = False
        
        # Test Homebrew compatibility
        brew_success, _, _ = self._run_command("brew --version")
        results["homebrew_available"] = brew_success
        
        # Test macOS-specific permissions
        results["macos_permissions"] = self._test_macos_permissions()
        
        return results
    
    def _test_linux_installation(self) -> Dict[str, bool]:
        """Test Linux-specific installation scenarios"""
        results = {"platform": "Linux"}
        
        # Detect Linux distribution
        try:
            with open("/etc/os-release", "r") as f:
                os_release = f.read()
                if "Ubuntu" in os_release:
                    results["distribution"] = "Ubuntu"
                elif "CentOS" in os_release or "Red Hat" in os_release:
                    results["distribution"] = "RHEL/CentOS"
                elif "Debian" in os_release:
                    results["distribution"] = "Debian"
                else:
                    results["distribution"] = "Other"
        except:
            results["distribution"] = "Unknown"
        
        # Test package managers
        package_managers = ["apt", "yum", "dnf", "pacman", "zypper"]
        for pm in package_managers:
            success, _, _ = self._run_command(f"{pm} --version")
            results[f"{pm}_available"] = success
        
        # Test Python installations
        python_commands = ["python3", "python", "python3.8", "python3.9", "python3.10", "python3.11"]
        for cmd in python_commands:
            success, stdout, _ = self._run_command(f"{cmd} --version")
            if success:
                results[f"{cmd}_available"] = True
                version = stdout.strip().split()[-1] if stdout else "unknown"
                results[f"{cmd}_version"] = version
            else:
                results[f"{cmd}_available"] = False
        
        # Test sudo requirements
        results["sudo_required"] = self._test_sudo_requirements()
        
        return results
    
    def _test_windows_paths(self) -> bool:
        """Test Windows path handling"""
        try:
            # Test path with spaces
            temp_dir = tempfile.mkdtemp(prefix="Global Genie Test ")
            success = os.path.exists(temp_dir)
            if success:
                os.rmdir(temp_dir)
            return success
        except:
            return False
    
    def _test_macos_permissions(self) -> bool:
        """Test macOS permission requirements"""
        try:
            # Test user directory access
            home_dir = os.path.expanduser("~")
            test_file = os.path.join(home_dir, ".globalgenie_test")
            
            with open(test_file, "w") as f:
                f.write("test")
            
            success = os.path.exists(test_file)
            if success:
                os.remove(test_file)
            
            return success
        except:
            return False
    
    def _test_sudo_requirements(self) -> bool:
        """Test if sudo is required for installation"""
        # Test user pip install (should not require sudo)
        success, _, _ = self._run_command("python3 -m pip install --user --dry-run setuptools")
        return not success  # If user install fails, sudo might be required
    
    def test_architecture_compatibility(self) -> Dict[str, bool]:
        """Test compatibility with different architectures"""
        results = {}
        
        arch = platform.machine().lower()
        results["architecture"] = arch
        
        # Common architectures
        supported_archs = ["x86_64", "amd64", "arm64", "aarch64", "i386", "i686"]
        results["architecture_supported"] = arch in supported_archs
        
        # Test Python wheel compatibility
        success, stdout, _ = self._run_command("python -m pip debug --verbose")
        if success and "platform" in stdout.lower():
            results["wheel_platform_detected"] = True
        else:
            results["wheel_platform_detected"] = False
        
        return results
    
    def test_environment_variables(self) -> Dict[str, bool]:
        """Test environment variable handling across platforms"""
        results = {}
        
        # Test PATH variable
        path_var = os.environ.get("PATH", "")
        results["path_variable_exists"] = bool(path_var)
        
        # Test Python path detection
        python_paths = []
        for path in path_var.split(os.pathsep):
            if "python" in path.lower():
                python_paths.append(path)
        
        results["python_in_path"] = len(python_paths) > 0
        
        # Test pip path detection
        pip_paths = []
        for path in path_var.split(os.pathsep):
            if "pip" in path.lower() or "scripts" in path.lower():
                pip_paths.append(path)
        
        results["pip_in_path"] = len(pip_paths) > 0
        
        # Test home directory
        home_dir = os.path.expanduser("~")
        results["home_directory_accessible"] = os.path.exists(home_dir)
        
        return results
    
    def test_unicode_support(self) -> Dict[str, bool]:
        """Test Unicode and international character support"""
        results = {}
        
        try:
            # Test Unicode in paths
            unicode_dir = tempfile.mkdtemp(prefix="测试_")
            results["unicode_paths"] = os.path.exists(unicode_dir)
            if results["unicode_paths"]:
                os.rmdir(unicode_dir)
        except:
            results["unicode_paths"] = False
        
        # Test Unicode in environment
        try:
            test_var = "GLOBALGENIE_测试"
            os.environ[test_var] = "测试值"
            results["unicode_env_vars"] = os.environ.get(test_var) == "测试值"
            if test_var in os.environ:
                del os.environ[test_var]
        except:
            results["unicode_env_vars"] = False
        
        # Test Unicode in Python
        try:
            success, stdout, _ = self._run_command('python -c "print(\'测试 GlobalGenie 🚀\')"')
            results["unicode_python"] = success and "测试" in stdout
        except:
            results["unicode_python"] = False
        
        return results
    
    def run_all_tests(self) -> Dict[str, any]:
        """Run all cross-platform tests"""
        logger.info("Running cross-platform installation tests...")
        
        results = {
            "platform_info": self.platform_info,
            "tests": {}
        }
        
        # Run test categories
        results["tests"]["platform_specific"] = self.test_platform_specific_installation()
        results["tests"]["architecture"] = self.test_architecture_compatibility()
        results["tests"]["environment"] = self.test_environment_variables()
        results["tests"]["unicode"] = self.test_unicode_support()
        
        return results
    
    def generate_report(self, results: Dict[str, any]) -> str:
        """Generate cross-platform test report"""
        report = []
        report.append("=" * 80)
        report.append("GLOBALGENIE CROSS-PLATFORM TEST REPORT")
        report.append("=" * 80)
        
        # Platform info
        report.append("PLATFORM INFORMATION:")
        report.append("-" * 40)
        for key, value in results["platform_info"].items():
            report.append(f"  {key}: {value}")
        report.append("")
        
        # Test results
        for category, tests in results["tests"].items():
            report.append(f"{category.upper().replace('_', ' ')} TESTS:")
            report.append("-" * 40)
            
            for test_name, result in tests.items():
                if isinstance(result, bool):
                    status = "✓ PASS" if result else "✗ FAIL"
                    report.append(f"  {test_name}: {status}")
                else:
                    report.append(f"  {test_name}: {result}")
            report.append("")
        
        return "\n".join(report)


def main():
    """Main execution function"""
    print("GlobalGenie Cross-Platform Installation Test")
    print("=" * 50)
    
    tester = CrossPlatformTester()
    results = tester.run_all_tests()
    
    # Generate report
    report = tester.generate_report(results)
    print(report)
    
    # Save results
    with open("cross_platform_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    with open("cross_platform_test_report.txt", "w") as f:
        f.write(report)
    
    print("Results saved to cross_platform_test_results.json")
    print("Report saved to cross_platform_test_report.txt")


if __name__ == "__main__":
    main()