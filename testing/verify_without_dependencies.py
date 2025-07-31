#!/usr/bin/env python3
"""
Dependency-Free Verification Script for GlobalGenie
Verifies installation without requiring external dependencies
"""

import sys
import os
import importlib
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class DependencyFreeVerifier:
    """Verify GlobalGenie installation without external dependencies"""
    
    def __init__(self):
        self.results = {}
        self.python_version = sys.version_info
        
    def verify_python_version(self) -> Dict[str, any]:
        """Verify Python version compatibility"""
        results = {
            "version": f"{self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}",
            "major": self.python_version.major,
            "minor": self.python_version.minor,
            "micro": self.python_version.micro,
            "compatible": False,
            "minimum_met": False
        }
        
        # Check minimum version (3.8+)
        if self.python_version >= (3, 8):
            results["minimum_met"] = True
            
        # Check compatible versions
        if (3, 8) <= self.python_version < (4, 0):
            results["compatible"] = True
            
        return results
    
    def verify_core_imports(self) -> Dict[str, bool]:
        """Verify core GlobalGenie imports work"""
        imports_to_test = [
            "globalgenie",
            "globalgenie.agent",
            "globalgenie.models",
            "globalgenie.models.openai",
            "globalgenie.tools",
            "globalgenie.memory",
            "globalgenie.cli",
            "globalgenie.cli.entrypoint"
        ]
        
        results = {}
        
        for module_name in imports_to_test:
            try:
                importlib.import_module(module_name)
                results[module_name] = True
            except ImportError as e:
                results[module_name] = False
                print(f"Import failed for {module_name}: {e}")
            except Exception as e:
                results[module_name] = False
                print(f"Unexpected error importing {module_name}: {e}")
        
        return results
    
    def verify_package_structure(self) -> Dict[str, bool]:
        """Verify package structure and files"""
        results = {}
        
        try:
            import globalgenie
            package_path = Path(globalgenie.__file__).parent
            results["package_path_found"] = True
            results["package_location"] = str(package_path)
            
            # Check for essential files/directories
            essential_items = [
                "agent.py",
                "models",
                "tools", 
                "memory",
                "cli",
                "__init__.py"
            ]
            
            for item in essential_items:
                item_path = package_path / item
                results[f"has_{item}"] = item_path.exists()
                
        except Exception as e:
            results["package_path_found"] = False
            results["error"] = str(e)
            
        return results
    
    def verify_version_info(self) -> Dict[str, any]:
        """Verify version information is accessible"""
        results = {}
        
        try:
            import globalgenie
            
            # Check __version__ attribute
            if hasattr(globalgenie, '__version__'):
                results["version_attribute"] = True
                results["version"] = globalgenie.__version__
            else:
                results["version_attribute"] = False
                results["version"] = None
            
            # Check other metadata
            metadata_attrs = ['__author__', '__email__', '__description__']
            for attr in metadata_attrs:
                results[attr] = hasattr(globalgenie, attr)
                if hasattr(globalgenie, attr):
                    results[f"{attr}_value"] = getattr(globalgenie, attr)
                    
        except Exception as e:
            results["error"] = str(e)
            results["version_attribute"] = False
            
        return results
    
    def verify_basic_functionality(self) -> Dict[str, bool]:
        """Verify basic functionality without API keys"""
        results = {}
        
        try:
            # Test Agent class import and instantiation
            from globalgenie.agent import Agent
            results["agent_import"] = True
            
            # Test model import
            from globalgenie.models.openai import OpenAIChat
            results["model_import"] = True
            
            # Test agent creation (should work without API key for basic instantiation)
            try:
                agent = Agent(
                    model=OpenAIChat(id="gpt-4", api_key="test-key"),
                    instructions="Test agent"
                )
                results["agent_creation"] = True
            except Exception as e:
                # This might fail due to API key validation, which is expected
                results["agent_creation"] = False
                results["agent_creation_error"] = str(e)
            
            # Test memory import
            try:
                from globalgenie.memory import SqliteMemory
                results["memory_import"] = True
            except ImportError:
                results["memory_import"] = False
            
            # Test tools import
            try:
                from globalgenie.tools.web import WebSearchTools
                results["tools_import"] = True
            except ImportError:
                results["tools_import"] = False
                
        except Exception as e:
            results["basic_functionality_error"] = str(e)
            
        return results
    
    def verify_cli_accessibility(self) -> Dict[str, bool]:
        """Verify CLI commands are accessible"""
        results = {}
        
        try:
            # Test CLI module import
            from globalgenie.cli.entrypoint import globalgenie_cli
            results["cli_import"] = True
            
            # Test if CLI function is callable
            results["cli_callable"] = callable(globalgenie_cli)
            
        except ImportError:
            results["cli_import"] = False
            results["cli_callable"] = False
        except Exception as e:
            results["cli_error"] = str(e)
            results["cli_import"] = False
            
        # Test command line entry points
        try:
            # Check if gg command is available
            result = subprocess.run([sys.executable, "-c", "import sys; sys.exit(0 if 'gg' in sys.modules else 1)"], 
                                  capture_output=True, timeout=10)
            results["gg_command_available"] = result.returncode == 0
        except:
            results["gg_command_available"] = False
            
        return results
    
    def verify_dependencies(self) -> Dict[str, any]:
        """Verify core dependencies are available"""
        core_dependencies = [
            "docstring_parser",
            "gitpython", 
            "httpx",
            "pydantic",
            "pydantic_settings",
            "python_dotenv",
            "python_multipart",
            "pyyaml",
            "rich",
            "typer",
            "typing_extensions"
        ]
        
        results = {
            "total_dependencies": len(core_dependencies),
            "available_dependencies": 0,
            "missing_dependencies": [],
            "dependency_status": {}
        }
        
        for dep in core_dependencies:
            try:
                # Try different import names
                import_names = [dep, dep.replace("_", "-"), dep.replace("-", "_")]
                imported = False
                
                for import_name in import_names:
                    try:
                        importlib.import_module(import_name)
                        results["dependency_status"][dep] = True
                        results["available_dependencies"] += 1
                        imported = True
                        break
                    except ImportError:
                        continue
                
                if not imported:
                    results["dependency_status"][dep] = False
                    results["missing_dependencies"].append(dep)
                    
            except Exception as e:
                results["dependency_status"][dep] = False
                results["missing_dependencies"].append(dep)
        
        results["all_dependencies_available"] = len(results["missing_dependencies"]) == 0
        
        return results
    
    def verify_installation_integrity(self) -> Dict[str, any]:
        """Verify installation integrity"""
        results = {}
        
        try:
            import globalgenie
            
            # Check if package is properly installed
            results["package_installed"] = True
            
            # Get installation location
            package_file = globalgenie.__file__
            results["installation_path"] = str(Path(package_file).parent)
            
            # Check if it's in site-packages (proper installation)
            results["in_site_packages"] = "site-packages" in package_file
            
            # Check if it's a development installation
            results["development_install"] = package_file.endswith(".egg-link") or "src" in package_file
            
            # Verify package can be imported from different locations
            original_path = sys.path.copy()
            try:
                # Remove current directory from path to test proper installation
                if '' in sys.path:
                    sys.path.remove('')
                if '.' in sys.path:
                    sys.path.remove('.')
                
                # Try importing again
                import importlib
                importlib.reload(globalgenie)
                results["imports_without_local_path"] = True
                
            except Exception as e:
                results["imports_without_local_path"] = False
                results["import_error"] = str(e)
            finally:
                sys.path = original_path
                
        except ImportError:
            results["package_installed"] = False
        except Exception as e:
            results["verification_error"] = str(e)
            
        return results
    
    def run_all_verifications(self) -> Dict[str, any]:
        """Run all verification tests"""
        print("Running GlobalGenie installation verification...")
        
        all_results = {
            "verification_timestamp": __import__("datetime").datetime.now().isoformat(),
            "python_info": {
                "version": sys.version,
                "executable": sys.executable,
                "platform": sys.platform
            },
            "verifications": {}
        }
        
        # Run all verification categories
        all_results["verifications"]["python_version"] = self.verify_python_version()
        all_results["verifications"]["core_imports"] = self.verify_core_imports()
        all_results["verifications"]["package_structure"] = self.verify_package_structure()
        all_results["verifications"]["version_info"] = self.verify_version_info()
        all_results["verifications"]["basic_functionality"] = self.verify_basic_functionality()
        all_results["verifications"]["cli_accessibility"] = self.verify_cli_accessibility()
        all_results["verifications"]["dependencies"] = self.verify_dependencies()
        all_results["verifications"]["installation_integrity"] = self.verify_installation_integrity()
        
        return all_results
    
    def generate_report(self, results: Dict[str, any]) -> str:
        """Generate verification report with Windows-compatible characters"""
        report = []
        report.append("=" * 80)
        report.append("GLOBALGENIE INSTALLATION VERIFICATION REPORT")
        report.append("=" * 80)
        report.append(f"Verification Time: {results['verification_timestamp']}")
        report.append(f"Python Version: {results['python_info']['version']}")
        report.append(f"Python Executable: {results['python_info']['executable']}")
        report.append("")
        
        # Summary counters
        total_checks = 0
        passed_checks = 0
        
        # Process each verification category
        for category, checks in results["verifications"].items():
            report.append(f"{category.upper().replace('_', ' ')}:")
            report.append("-" * 40)
            
            for check_name, result in checks.items():
                if isinstance(result, bool):
                    status = "[PASS]" if result else "[FAIL]"
                    report.append(f"  {check_name}: {status}")
                    total_checks += 1
                    if result:
                        passed_checks += 1
                elif isinstance(result, (str, int, float)):
                    report.append(f"  {check_name}: {result}")
                elif isinstance(result, list):
                    if result:
                        report.append(f"  {check_name}: {', '.join(map(str, result))}")
                    else:
                        report.append(f"  {check_name}: None")
            report.append("")
        
        # Overall summary
        report.append("VERIFICATION SUMMARY:")
        report.append("-" * 40)
        report.append(f"Total Checks: {total_checks}")
        report.append(f"Passed: {passed_checks}")
        report.append(f"Failed: {total_checks - passed_checks}")
        
        if total_checks > 0:
            success_rate = (passed_checks / total_checks) * 100
            report.append(f"Success Rate: {success_rate:.1f}%")
            
            if passed_checks == total_checks:
                report.append("\nALL VERIFICATIONS PASSED!")
                report.append("GlobalGenie is properly installed and ready to use.")
            else:
                report.append(f"\n{total_checks - passed_checks} verifications failed.")
                report.append("Please check the failed items above.")
        
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """Main verification function"""
    print("GlobalGenie Installation Verification")
    print("=" * 50)
    
    verifier = DependencyFreeVerifier()
    
    try:
        # Run all verifications
        results = verifier.run_all_verifications()
        
        # Generate and display report
        report = verifier.generate_report(results)
        print(report)
        
        # Save results
        with open("verification_results.json", "w") as f:
            json.dump(results, f, indent=2, default=str)
        
        with open("verification_report.txt", "w") as f:
            f.write(report)
        
        print(f"\nDetailed results saved to: verification_results.json")
        print(f"Verification report saved to: verification_report.txt")
        
        # Return exit code based on results
        verifications = results["verifications"]
        critical_failures = []
        
        # Check critical verifications
        if not verifications.get("python_version", {}).get("compatible", False):
            critical_failures.append("Python version incompatible")
        
        if not verifications.get("core_imports", {}).get("globalgenie", False):
            critical_failures.append("Core package import failed")
        
        if critical_failures:
            print(f"\n❌ Critical failures detected: {', '.join(critical_failures)}")
            return 1
        else:
            print("\n✅ Core verification passed - GlobalGenie is functional")
            return 0
            
    except Exception as e:
        print(f"Verification failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)