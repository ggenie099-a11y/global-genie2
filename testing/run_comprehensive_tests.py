#!/usr/bin/env python3
"""
Comprehensive Test Runner for GlobalGenie Installation and Integration
Orchestrates all test suites and generates consolidated reports
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging
from datetime import datetime

# Configure logging with proper encoding for Windows
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('comprehensive_test.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ComprehensiveTestRunner:
    """Orchestrate all GlobalGenie installation and integration tests"""
    
    def __init__(self):
        self.test_scripts = {
            "installation": "test_installation_comprehensive.py",
            "cross_platform": "test_cross_platform.py", 
            "verification": "verify_without_dependencies.py"
        }
        self.results = {}
        self.start_time = None
        self.end_time = None
        
    def _run_test_script(self, script_name: str, script_path: str) -> Tuple[bool, Dict, str]:
        """Run a test script and return results"""
        logger.info(f"Running {script_name} tests...")
        
        try:
            # Run the test script
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                timeout=1800  # 30 minutes timeout
            )
            
            success = result.returncode == 0
            output = result.stdout
            error = result.stderr
            
            # Try to load JSON results if available
            json_results = {}
            result_files = {
                "installation": "installation_test_results.json",
                "cross_platform": "cross_platform_test_results.json",
                "verification": "verification_results.json"
            }
            
            if script_name in result_files:
                result_file = result_files[script_name]
                if os.path.exists(result_file):
                    try:
                        with open(result_file, 'r') as f:
                            json_results = json.load(f)
                    except Exception as e:
                        logger.warning(f"Could not load JSON results from {result_file}: {e}")
            
            return success, json_results, output
            
        except subprocess.TimeoutExpired:
            logger.error(f"{script_name} test timed out")
            return False, {}, "Test timed out after 30 minutes"
        except Exception as e:
            logger.error(f"Error running {script_name} test: {e}")
            return False, {}, str(e)
    
    def run_all_tests(self) -> Dict[str, any]:
        """Run all test suites"""
        logger.info("Starting comprehensive GlobalGenie testing...")
        self.start_time = datetime.now()
        
        overall_results = {
            "test_session": {
                "start_time": self.start_time.isoformat(),
                "test_environment": {
                    "python_version": sys.version,
                    "python_executable": sys.executable,
                    "platform": sys.platform,
                    "working_directory": os.getcwd()
                }
            },
            "test_suites": {},
            "summary": {}
        }
        
        # Run each test suite
        for test_name, script_path in self.test_scripts.items():
            if not os.path.exists(script_path):
                logger.error(f"Test script not found: {script_path}")
                overall_results["test_suites"][test_name] = {
                    "status": "SKIPPED",
                    "reason": "Script not found",
                    "results": {}
                }
                continue
            
            logger.info(f"Executing {test_name} test suite...")
            success, json_results, output = self._run_test_script(test_name, script_path)
            
            overall_results["test_suites"][test_name] = {
                "status": "PASSED" if success else "FAILED",
                "results": json_results,
                "output_preview": output[:500] + "..." if len(output) > 500 else output
            }
            
            if success:
                logger.info(f"✓ {test_name} tests completed successfully")
            else:
                logger.error(f"✗ {test_name} tests failed")
        
        self.end_time = datetime.now()
        overall_results["test_session"]["end_time"] = self.end_time.isoformat()
        overall_results["test_session"]["duration"] = str(self.end_time - self.start_time)
        
        # Generate summary
        overall_results["summary"] = self._generate_summary(overall_results["test_suites"])
        
        return overall_results
    
    def _generate_summary(self, test_suites: Dict[str, any]) -> Dict[str, any]:
        """Generate overall test summary"""
        summary = {
            "total_suites": len(test_suites),
            "passed_suites": 0,
            "failed_suites": 0,
            "skipped_suites": 0,
            "detailed_results": {}
        }
        
        for suite_name, suite_data in test_suites.items():
            status = suite_data["status"]
            
            if status == "PASSED":
                summary["passed_suites"] += 1
            elif status == "FAILED":
                summary["failed_suites"] += 1
            elif status == "SKIPPED":
                summary["skipped_suites"] += 1
            
            # Extract key metrics from each suite
            if "results" in suite_data and suite_data["results"]:
                summary["detailed_results"][suite_name] = self._extract_key_metrics(
                    suite_name, suite_data["results"]
                )
        
        # Calculate overall success rate
        if summary["total_suites"] > 0:
            summary["success_rate"] = (summary["passed_suites"] / summary["total_suites"]) * 100
        else:
            summary["success_rate"] = 0
        
        return summary
    
    def _extract_key_metrics(self, suite_name: str, results: Dict[str, any]) -> Dict[str, any]:
        """Extract key metrics from test suite results"""
        metrics = {}
        
        if suite_name == "installation":
            # Extract installation test metrics
            if "tests" in results:
                total_tests = 0
                passed_tests = 0
                
                for category, tests in results["tests"].items():
                    if isinstance(tests, dict):
                        for test_name, result in tests.items():
                            if isinstance(result, bool):
                                total_tests += 1
                                if result:
                                    passed_tests += 1
                            elif isinstance(result, dict):
                                for sub_test, sub_result in result.items():
                                    if isinstance(sub_result, bool):
                                        total_tests += 1
                                        if sub_result:
                                            passed_tests += 1
                
                metrics["total_tests"] = total_tests
                metrics["passed_tests"] = passed_tests
                metrics["success_rate"] = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        elif suite_name == "cross_platform":
            # Extract cross-platform metrics
            if "tests" in results:
                platform_info = results.get("platform_info", {})
                metrics["platform"] = platform_info.get("system", "Unknown")
                metrics["architecture"] = platform_info.get("machine", "Unknown")
                
                # Count platform-specific tests
                platform_tests = results["tests"].get("platform_specific", {})
                metrics["platform_tests_passed"] = sum(1 for v in platform_tests.values() if v is True)
                metrics["platform_tests_total"] = len([v for v in platform_tests.values() if isinstance(v, bool)])
        
        elif suite_name == "verification":
            # Extract verification metrics
            if "verifications" in results:
                total_verifications = 0
                passed_verifications = 0
                
                for category, checks in results["verifications"].items():
                    if isinstance(checks, dict):
                        for check_name, result in checks.items():
                            if isinstance(result, bool):
                                total_verifications += 1
                                if result:
                                    passed_verifications += 1
                
                metrics["total_verifications"] = total_verifications
                metrics["passed_verifications"] = passed_verifications
                metrics["verification_rate"] = (passed_verifications / total_verifications * 100) if total_verifications > 0 else 0
        
        return metrics
    
    def generate_consolidated_report(self, results: Dict[str, any]) -> str:
        """Generate a consolidated test report"""
        report = []
        report.append("=" * 100)
        report.append("GLOBALGENIE COMPREHENSIVE TEST REPORT")
        report.append("=" * 100)
        
        # Test session info
        session = results["test_session"]
        report.append(f"Test Start Time: {session['start_time']}")
        report.append(f"Test End Time: {session['end_time']}")
        report.append(f"Total Duration: {session['duration']}")
        report.append(f"Python Version: {session['test_environment']['python_version'].split()[0]}")
        report.append(f"Platform: {session['test_environment']['platform']}")
        report.append("")
        
        # Overall summary
        summary = results["summary"]
        report.append("OVERALL SUMMARY:")
        report.append("-" * 50)
        report.append(f"Total Test Suites: {summary['total_suites']}")
        report.append(f"Passed: {summary['passed_suites']}")
        report.append(f"Failed: {summary['failed_suites']}")
        report.append(f"Skipped: {summary['skipped_suites']}")
        report.append(f"Success Rate: {summary['success_rate']:.1f}%")
        report.append("")
        
        # Individual test suite results
        for suite_name, suite_data in results["test_suites"].items():
            status_icon = "✓" if suite_data["status"] == "PASSED" else "✗" if suite_data["status"] == "FAILED" else "⚠"
            report.append(f"{status_icon} {suite_name.upper().replace('_', ' ')} TEST SUITE: {suite_data['status']}")
            report.append("-" * 50)
            
            # Add detailed metrics if available
            if suite_name in summary["detailed_results"]:
                metrics = summary["detailed_results"][suite_name]
                for metric_name, metric_value in metrics.items():
                    report.append(f"  {metric_name.replace('_', ' ').title()}: {metric_value}")
            
            # Add output preview
            if suite_data.get("output_preview"):
                report.append("  Output Preview:")
                for line in suite_data["output_preview"].split('\n')[:5]:
                    if line.strip():
                        report.append(f"    {line}")
            
            report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS:")
        report.append("-" * 50)
        
        if summary["success_rate"] == 100:
            report.append("🎉 Excellent! All tests passed successfully.")
            report.append("   GlobalGenie is ready for production use.")
        elif summary["success_rate"] >= 80:
            report.append("✅ Good! Most tests passed.")
            report.append("   Review failed tests and address any critical issues.")
        elif summary["success_rate"] >= 60:
            report.append("⚠️  Moderate success rate.")
            report.append("   Several issues detected. Review and fix before deployment.")
        else:
            report.append("❌ Low success rate detected.")
            report.append("   Significant issues found. Thorough review required.")
        
        # Next steps
        report.append("")
        report.append("NEXT STEPS:")
        report.append("-" * 50)
        report.append("1. Review individual test reports for detailed findings")
        report.append("2. Address any failed tests based on priority")
        report.append("3. Re-run tests after fixes to verify improvements")
        report.append("4. Consider environment-specific optimizations")
        
        report.append("=" * 100)
        
        return "\n".join(report)
    
    def save_results(self, results: Dict[str, any], report: str):
        """Save test results and reports to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON results
        results_file = f"comprehensive_test_results_{timestamp}.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        # Save text report
        report_file = f"comprehensive_test_report_{timestamp}.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        # Save latest versions (without timestamp)
        with open("comprehensive_test_results_latest.json", 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        with open("comprehensive_test_report_latest.txt", 'w') as f:
            f.write(report)
        
        logger.info(f"Results saved to: {results_file}")
        logger.info(f"Report saved to: {report_file}")
        logger.info(f"Latest results: comprehensive_test_results_latest.json")
        logger.info(f"Latest report: comprehensive_test_report_latest.txt")
    
    def cleanup_temp_files(self):
        """Clean up temporary test files"""
        temp_files = [
            "installation_test_results.json",
            "installation_test_report.txt", 
            "installation_test.log",
            "cross_platform_test_results.json",
            "cross_platform_test_report.txt",
            "verification_results.json",
            "verification_report.txt"
        ]
        
        for file in temp_files:
            if os.path.exists(file):
                try:
                    os.remove(file)
                    logger.info(f"Cleaned up: {file}")
                except Exception as e:
                    logger.warning(f"Could not clean up {file}: {e}")


def main():
    """Main test execution function"""
    print("GlobalGenie Comprehensive Test Suite")
    print("=" * 60)
    print("This will run all installation and integration tests.")
    print("Expected duration: 10-30 minutes depending on system.")
    print("")
    
    # Confirm execution
    try:
        response = input("Continue with comprehensive testing? (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Testing cancelled.")
            return 0
    except KeyboardInterrupt:
        print("\nTesting cancelled.")
        return 0
    
    runner = ComprehensiveTestRunner()
    
    try:
        # Run all tests
        results = runner.run_all_tests()
        
        # Generate consolidated report
        report = runner.generate_consolidated_report(results)
        print("\n" + report)
        
        # Save results
        runner.save_results(results, report)
        
        # Cleanup temporary files
        runner.cleanup_temp_files()
        
        # Return appropriate exit code
        success_rate = results["summary"]["success_rate"]
        if success_rate == 100:
            return 0  # Perfect success
        elif success_rate >= 80:
            return 1  # Mostly successful with some issues
        else:
            return 2  # Significant issues detected
            
    except KeyboardInterrupt:
        print("\nTesting interrupted by user")
        runner.cleanup_temp_files()
        return 130
    except Exception as e:
        logger.error(f"Test execution failed: {e}")
        runner.cleanup_temp_files()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)