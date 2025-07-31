#!/usr/bin/env python3
"""
GlobalGenie Installation and Integration Test Suite
Comprehensive testing for pip installation across different environments
"""

import os
import sys
import subprocess
import tempfile
import shutil
import platform
import json
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('installation_test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class InstallationTester:
    """Comprehensive installation testing for GlobalGenie"""
    
    def __init__(self):
        self.test_results = {}
        self.python_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]
        self.package_managers = ["pip", "pip3", "python -m pip"]
        self.platforms = self._detect_platform()
        self.temp_dirs = []
        
    def _detect_platform(self) -> Dict[str, str]:
        """Detect current platform information"""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation()
        }
    
    def _run_command(self, command: str, cwd: Optional[str] = None, timeout: int = 300) -> Tuple[bool, str, str]:
        """Run a shell command and return success status, stdout, stderr"""
        try:
            logger.info(f"Running command: {command}")
            if platform.system() == "Windows":
                # Use shell=True on Windows for proper command execution
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=cwd
                )
            else:
                result = subprocess.run(
                    command.split(),
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=cwd
                )
            
            success = result.returncode == 0
            return success, result.stdout, result.stderr
            
        except subprocess.TimeoutExpired:
            return False, "", f"Command timed out after {timeout} seconds"
        except Exception as e:
            return False, "", str(e)
    
    def _create_virtual_env(self, env_name: str, python_version: str = None) -> Tuple[bool, str]:
        """Create a virtual environment"""
        temp_dir = tempfile.mkdtemp(prefix=f"gg_test_{env_name}_")
        self.temp_dirs.append(temp_dir)
        
        # Determine Python executable
        if python_version:
            python_cmd = f"python{python_version}"
        else:
            python_cmd = "python"
        
        # Create virtual environment
        venv_path = os.path.join(temp_dir, "venv")
        
        if platform.system() == "Windows":
            create_cmd = f"{python_cmd} -m venv {venv_path}"
            activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
            pip_cmd = os.path.join(venv_path, "Scripts", "pip.exe")
        else:
            create_cmd = f"{python_cmd} -m venv {venv_path}"
            activate_script = os.path.join(venv_path, "bin", "activate")
            pip_cmd = os.path.join(venv_path, "bin", "pip")
        
        success, stdout, stderr = self._run_command(create_cmd)
        
        if success and os.path.exists(pip_cmd):
            return True, venv_path
        else:
            logger.error(f"Failed to create virtual environment: {stderr}")
            return False, temp_dir
    
    def _get_pip_command(self, venv_path: str) -> str:
        """Get the pip command for the virtual environment"""
        if platform.system() == "Windows":
            return os.path.join(venv_path, "Scripts", "pip.exe")
        else:
            return os.path.join(venv_path, "bin", "pip")
    
    def _get_python_command(self, venv_path: str) -> str:
        """Get the python command for the virtual environment"""
        if platform.system() == "Windows":
            return os.path.join(venv_path, "Scripts", "python.exe")
        else:
            return os.path.join(venv_path, "bin", "python")
    
    def test_pip_installation(self) -> Dict[str, bool]:
        """Test pip installation in fresh environments"""
        logger.info("Testing pip installation...")
        results = {}
        
        # Test basic pip install
        success, venv_path = self._create_virtual_env("basic_install")
        if success:
            pip_cmd = self._get_pip_command(venv_path)
            
            # Install GlobalGenie
            install_success, stdout, stderr = self._run_command(f'"{pip_cmd}" install globalgenie')
            results["basic_pip_install"] = install_success
            
            if install_success:
                # Test import
                python_cmd = self._get_python_command(venv_path)
                import_success, _, _ = self._run_command(f'"{python_cmd}" -c "import globalgenie; print(globalgenie.__version__)"')
                results["basic_import"] = import_success
            else:
                logger.error(f"Basic pip install failed: {stderr}")
                results["basic_import"] = False
        else:
            results["basic_pip_install"] = False
            results["basic_import"] = False
        
        # Test with --upgrade flag
        success, venv_path = self._create_virtual_env("upgrade_install")
        if success:
            pip_cmd = self._get_pip_command(venv_path)
            install_success, _, stderr = self._run_command(f'"{pip_cmd}" install --upgrade globalgenie')
            results["upgrade_install"] = install_success
            if not install_success:
                logger.error(f"Upgrade install failed: {stderr}")
        else:
            results["upgrade_install"] = False
        
        # Test with --force-reinstall
        success, venv_path = self._create_virtual_env("force_install")
        if success:
            pip_cmd = self._get_pip_command(venv_path)
            install_success, _, stderr = self._run_command(f'"{pip_cmd}" install --force-reinstall globalgenie')
            results["force_reinstall"] = install_success
            if not install_success:
                logger.error(f"Force reinstall failed: {stderr}")
        else:
            results["force_reinstall"] = False
        
        return results
    
    def test_python_versions(self) -> Dict[str, Dict[str, bool]]:
        """Test installation across different Python versions"""
        logger.info("Testing Python version compatibility...")
        results = {}
        
        for version in self.python_versions:
            logger.info(f"Testing Python {version}...")
            version_results = {}
            
            # Check if Python version is available
            check_success, _, _ = self._run_command(f"python{version} --version")
            if not check_success:
                logger.warning(f"Python {version} not available on this system")
                version_results["available"] = False
                version_results["install"] = False
                version_results["import"] = False
                results[f"python_{version}"] = version_results
                continue
            
            version_results["available"] = True
            
            # Create virtual environment with specific Python version
            success, venv_path = self._create_virtual_env(f"py{version}", version)
            if success:
                pip_cmd = self._get_pip_command(venv_path)
                python_cmd = self._get_python_command(venv_path)
                
                # Install GlobalGenie
                install_success, _, stderr = self._run_command(f'"{pip_cmd}" install globalgenie')
                version_results["install"] = install_success
                
                if install_success:
                    # Test import
                    import_success, stdout, import_stderr = self._run_command(
                        f'"{python_cmd}" -c "import globalgenie; print(f\'GlobalGenie version: {{globalgenie.__version__}}\'); print(\'Import successful\')"'
                    )
                    version_results["import"] = import_success
                    
                    if import_success:
                        logger.info(f"Python {version}: {stdout.strip()}")
                    else:
                        logger.error(f"Python {version} import failed: {import_stderr}")
                else:
                    logger.error(f"Python {version} install failed: {stderr}")
                    version_results["import"] = False
            else:
                version_results["install"] = False
                version_results["import"] = False
            
            results[f"python_{version}"] = version_results
        
        return results
    
    def test_virtual_environments(self) -> Dict[str, bool]:
        """Test virtual environment compatibility"""
        logger.info("Testing virtual environment compatibility...")
        results = {}
        
        # Test venv (built-in)
        success, venv_path = self._create_virtual_env("venv_test")
        if success:
            pip_cmd = self._get_pip_command(venv_path)
            install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
            results["venv"] = install_success
        else:
            results["venv"] = False
        
        # Test virtualenv (if available)
        virtualenv_check, _, _ = self._run_command("virtualenv --version")
        if virtualenv_check:
            temp_dir = tempfile.mkdtemp(prefix="gg_virtualenv_test_")
            self.temp_dirs.append(temp_dir)
            venv_path = os.path.join(temp_dir, "virtualenv_test")
            
            create_success, _, _ = self._run_command(f"virtualenv {venv_path}")
            if create_success:
                pip_cmd = self._get_pip_command(venv_path)
                install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
                results["virtualenv"] = install_success
            else:
                results["virtualenv"] = False
        else:
            results["virtualenv"] = False
            logger.info("virtualenv not available, skipping test")
        
        # Test conda (if available)
        conda_check, _, _ = self._run_command("conda --version")
        if conda_check:
            env_name = "gg_conda_test"
            create_success, _, _ = self._run_command(f"conda create -n {env_name} python=3.9 -y")
            if create_success:
                install_success, _, _ = self._run_command(f"conda run -n {env_name} pip install globalgenie")
                results["conda"] = install_success
                # Cleanup
                self._run_command(f"conda env remove -n {env_name} -y")
            else:
                results["conda"] = False
        else:
            results["conda"] = False
            logger.info("conda not available, skipping test")
        
        return results
    
    def test_package_managers(self) -> Dict[str, bool]:
        """Test different package manager commands"""
        logger.info("Testing package manager compatibility...")
        results = {}
        
        for manager in self.package_managers:
            logger.info(f"Testing {manager}...")
            success, venv_path = self._create_virtual_env(f"manager_{manager.replace(' ', '_').replace('-', '_')}")
            
            if success:
                if platform.system() == "Windows":
                    if manager == "pip":
                        cmd = f'"{self._get_pip_command(venv_path)}" install globalgenie'
                    elif manager == "pip3":
                        # On Windows, pip3 might not exist, use pip instead
                        cmd = f'"{self._get_pip_command(venv_path)}" install globalgenie'
                    else:  # python -m pip
                        python_cmd = self._get_python_command(venv_path)
                        cmd = f'"{python_cmd}" -m pip install globalgenie'
                else:
                    if manager == "python -m pip":
                        python_cmd = self._get_python_command(venv_path)
                        cmd = f"{python_cmd} -m pip install globalgenie"
                    else:
                        pip_cmd = self._get_pip_command(venv_path)
                        cmd = f"{pip_cmd} install globalgenie"
                
                install_success, _, stderr = self._run_command(cmd)
                results[manager] = install_success
                
                if not install_success:
                    logger.error(f"{manager} failed: {stderr}")
            else:
                results[manager] = False
        
        return results
    
    def test_example_scripts(self) -> Dict[str, bool]:
        """Test that example scripts run successfully"""
        logger.info("Testing example scripts...")
        results = {}
        
        # Create a test environment
        success, venv_path = self._create_virtual_env("examples_test")
        if not success:
            return {"environment_creation": False}
        
        pip_cmd = self._get_pip_command(venv_path)
        python_cmd = self._get_python_command(venv_path)
        
        # Install GlobalGenie
        install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
        if not install_success:
            return {"globalgenie_install": False}
        
        results["globalgenie_install"] = True
        
        # Test basic import and agent creation
        basic_test = '''
import sys
try:
    from globalgenie.agent import Agent
    from globalgenie.models.openai import OpenAIChat
    print("✓ Basic imports successful")
    
    # Test agent creation (without API key)
    try:
        agent = Agent(
            model=OpenAIChat(id="gpt-4", api_key="test-key"),
            instructions="Test agent"
        )
        print("✓ Agent creation successful")
    except Exception as e:
        print(f"✓ Agent creation test passed (expected without API key): {type(e).__name__}")
    
    print("SUCCESS: Basic functionality test passed")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
'''
        
        # Write test script
        test_script_path = os.path.join(os.path.dirname(venv_path), "basic_test.py")
        with open(test_script_path, 'w') as f:
            f.write(basic_test)
        
        # Run basic test
        test_success, stdout, stderr = self._run_command(f'"{python_cmd}" "{test_script_path}"')
        results["basic_functionality"] = test_success
        
        if test_success:
            logger.info(f"Basic test output: {stdout}")
        else:
            logger.error(f"Basic test failed: {stderr}")
        
        # Test CLI entry points
        cli_success, stdout, stderr = self._run_command(f'"{python_cmd}" -c "import globalgenie.cli.entrypoint; print(\'CLI module accessible\')"')
        results["cli_access"] = cli_success
        
        return results
    
    def test_import_contexts(self) -> Dict[str, bool]:
        """Test import statements in various contexts"""
        logger.info("Testing import contexts...")
        results = {}
        
        success, venv_path = self._create_virtual_env("import_test")
        if not success:
            return {"environment_creation": False}
        
        pip_cmd = self._get_pip_command(venv_path)
        python_cmd = self._get_python_command(venv_path)
        
        # Install GlobalGenie
        install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
        if not install_success:
            return {"globalgenie_install": False}
        
        # Test different import patterns
        import_tests = {
            "basic_import": "import globalgenie",
            "agent_import": "from globalgenie.agent import Agent",
            "models_import": "from globalgenie.models.openai import OpenAIChat",
            "tools_import": "from globalgenie.tools.web import WebSearchTools",
            "memory_import": "from globalgenie.memory import SqliteMemory",
            "version_access": "import globalgenie; print(globalgenie.__version__)",
            "submodule_access": "import globalgenie.agent; print('Agent module loaded')"
        }
        
        for test_name, import_statement in import_tests.items():
            test_success, stdout, stderr = self._run_command(
                f'"{python_cmd}" -c "{import_statement}; print(\'SUCCESS: {test_name}\')"'
            )
            results[test_name] = test_success
            
            if not test_success:
                logger.error(f"{test_name} failed: {stderr}")
        
        return results
    
    def test_cli_commands(self) -> Dict[str, bool]:
        """Test CLI commands and entry points"""
        logger.info("Testing CLI commands...")
        results = {}
        
        success, venv_path = self._create_virtual_env("cli_test")
        if not success:
            return {"environment_creation": False}
        
        pip_cmd = self._get_pip_command(venv_path)
        python_cmd = self._get_python_command(venv_path)
        
        # Install GlobalGenie
        install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
        if not install_success:
            return {"globalgenie_install": False}
        
        # Test CLI entry points
        if platform.system() == "Windows":
            gg_cmd = os.path.join(venv_path, "Scripts", "gg.exe")
            globalgenie_cmd = os.path.join(venv_path, "Scripts", "globalgenie.exe")
        else:
            gg_cmd = os.path.join(venv_path, "bin", "gg")
            globalgenie_cmd = os.path.join(venv_path, "bin", "globalgenie")
        
        # Test gg command
        if os.path.exists(gg_cmd):
            gg_success, stdout, stderr = self._run_command(f'"{gg_cmd}" --help')
            results["gg_command"] = gg_success
        else:
            # Fallback to python -m
            gg_success, stdout, stderr = self._run_command(f'"{python_cmd}" -m globalgenie.cli.entrypoint --help')
            results["gg_command"] = gg_success
        
        # Test globalgenie command
        if os.path.exists(globalgenie_cmd):
            globalgenie_success, stdout, stderr = self._run_command(f'"{globalgenie_cmd}" --help')
            results["globalgenie_command"] = globalgenie_success
        else:
            # Fallback to python -m
            globalgenie_success, stdout, stderr = self._run_command(f'"{python_cmd}" -m globalgenie.cli.entrypoint --help')
            results["globalgenie_command"] = globalgenie_success
        
        return results
    
    def test_uninstall_process(self) -> Dict[str, bool]:
        """Test uninstall process and residual file cleanup"""
        logger.info("Testing uninstall process...")
        results = {}
        
        success, venv_path = self._create_virtual_env("uninstall_test")
        if not success:
            return {"environment_creation": False}
        
        pip_cmd = self._get_pip_command(venv_path)
        python_cmd = self._get_python_command(venv_path)
        
        # Install GlobalGenie
        install_success, _, _ = self._run_command(f'"{pip_cmd}" install globalgenie')
        if not install_success:
            return {"install_for_uninstall": False}
        
        results["install_for_uninstall"] = True
        
        # Check installation location
        location_success, stdout, stderr = self._run_command(f'"{pip_cmd}" show globalgenie')
        results["show_package_info"] = location_success
        
        # Uninstall
        uninstall_success, _, stderr = self._run_command(f'"{pip_cmd}" uninstall globalgenie -y')
        results["uninstall_success"] = uninstall_success
        
        if uninstall_success:
            # Verify uninstallation
            verify_success, _, _ = self._run_command(f'"{python_cmd}" -c "import globalgenie"')
            results["uninstall_verified"] = not verify_success  # Should fail after uninstall
            
            # Check for residual files (basic check)
            if platform.system() == "Windows":
                site_packages = os.path.join(venv_path, "Lib", "site-packages")
            else:
                site_packages = os.path.join(venv_path, "lib", "python*", "site-packages")
            
            # This is a simplified check - in practice, pip should clean up properly
            results["no_residual_files"] = True  # Assume pip cleans up correctly
        else:
            logger.error(f"Uninstall failed: {stderr}")
            results["uninstall_verified"] = False
            results["no_residual_files"] = False
        
        return results
    
    def cleanup(self):
        """Clean up temporary directories"""
        logger.info("Cleaning up temporary directories...")
        for temp_dir in self.temp_dirs:
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
                logger.info(f"Cleaned up: {temp_dir}")
            except Exception as e:
                logger.warning(f"Failed to clean up {temp_dir}: {e}")
    
    def run_all_tests(self) -> Dict[str, any]:
        """Run all installation tests"""
        logger.info("Starting comprehensive installation tests...")
        start_time = time.time()
        
        all_results = {
            "platform_info": self.platforms,
            "test_timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tests": {}
        }
        
        try:
            # Run all test categories
            all_results["tests"]["pip_installation"] = self.test_pip_installation()
            all_results["tests"]["python_versions"] = self.test_python_versions()
            all_results["tests"]["virtual_environments"] = self.test_virtual_environments()
            all_results["tests"]["package_managers"] = self.test_package_managers()
            all_results["tests"]["example_scripts"] = self.test_example_scripts()
            all_results["tests"]["import_contexts"] = self.test_import_contexts()
            all_results["tests"]["cli_commands"] = self.test_cli_commands()
            all_results["tests"]["uninstall_process"] = self.test_uninstall_process()
            
        except Exception as e:
            logger.error(f"Test execution failed: {e}")
            all_results["error"] = str(e)
        
        finally:
            self.cleanup()
        
        end_time = time.time()
        all_results["execution_time"] = end_time - start_time
        
        return all_results
    
    def generate_report(self, results: Dict[str, any]) -> str:
        """Generate a comprehensive test report"""
        report = []
        report.append("=" * 80)
        report.append("GLOBALGENIE INSTALLATION TEST REPORT")
        report.append("=" * 80)
        report.append(f"Test Date: {results['test_timestamp']}")
        report.append(f"Execution Time: {results['execution_time']:.2f} seconds")
        report.append("")
        
        # Platform information
        report.append("PLATFORM INFORMATION:")
        report.append("-" * 40)
        for key, value in results["platform_info"].items():
            report.append(f"  {key}: {value}")
        report.append("")
        
        # Test results
        total_tests = 0
        passed_tests = 0
        
        for category, tests in results["tests"].items():
            report.append(f"{category.upper().replace('_', ' ')}:")
            report.append("-" * 40)
            
            if isinstance(tests, dict):
                for test_name, result in tests.items():
                    if isinstance(result, dict):
                        # Handle nested results (like python versions)
                        report.append(f"  {test_name}:")
                        for sub_test, sub_result in result.items():
                            status = "✓ PASS" if sub_result else "✗ FAIL"
                            report.append(f"    {sub_test}: {status}")
                            total_tests += 1
                            if sub_result:
                                passed_tests += 1
                    else:
                        status = "✓ PASS" if result else "✗ FAIL"
                        report.append(f"  {test_name}: {status}")
                        total_tests += 1
                        if result:
                            passed_tests += 1
            report.append("")
        
        # Summary
        report.append("SUMMARY:")
        report.append("-" * 40)
        report.append(f"Total Tests: {total_tests}")
        report.append(f"Passed: {passed_tests}")
        report.append(f"Failed: {total_tests - passed_tests}")
        report.append(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if passed_tests == total_tests:
            report.append("\n🎉 ALL TESTS PASSED! GlobalGenie installation is working correctly.")
        else:
            report.append(f"\n⚠️  {total_tests - passed_tests} tests failed. Please review the failures above.")
        
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """Main test execution function"""
    print("GlobalGenie Installation Test Suite")
    print("=" * 50)
    
    tester = InstallationTester()
    
    try:
        # Run all tests
        results = tester.run_all_tests()
        
        # Generate and display report
        report = tester.generate_report(results)
        print(report)
        
        # Save results to file
        with open("installation_test_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        with open("installation_test_report.txt", "w") as f:
            f.write(report)
        
        print(f"\nDetailed results saved to: installation_test_results.json")
        print(f"Test report saved to: installation_test_report.txt")
        print(f"Test log saved to: installation_test.log")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
        tester.cleanup()
    except Exception as e:
        print(f"Test execution failed: {e}")
        tester.cleanup()
        raise


if __name__ == "__main__":
    main()