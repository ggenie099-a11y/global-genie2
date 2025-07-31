#!/usr/bin/env python3
"""
Final Git Cleanup
Remove unwanted files and prepare for clean commit
"""

import os
import glob
import subprocess

def remove_unwanted_files():
    """Remove unwanted files that shouldn't be in git"""
    print("=== REMOVING UNWANTED FILES ===")
    
    # Files with single quotes (likely from command errors)
    quote_files = glob.glob("*'")
    
    # Other unwanted files
    unwanted_files = [
        "cleanup_and_organize.py",
        "cleanup_summary.json",
        "pypi_deployment_guide.py"
    ]
    
    removed_files = []
    
    # Remove quote files
    for file in quote_files:
        try:
            os.remove(file)
            removed_files.append(file)
            print(f"✓ Removed: {file}")
        except Exception as e:
            print(f"✗ Failed to remove {file}: {e}")
    
    # Remove other unwanted files
    for file in unwanted_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                removed_files.append(file)
                print(f"✓ Removed: {file}")
            except Exception as e:
                print(f"✗ Failed to remove {file}: {e}")
    
    return removed_files

def check_git_status():
    """Check git status"""
    print("\n=== CHECKING GIT STATUS ===")
    
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            status_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            if status_lines:
                print("Files to be committed:")
                for line in status_lines:
                    if line.strip():
                        print(f"  {line}")
            else:
                print("No changes to commit")
            
            return status_lines
        else:
            print(f"Git status failed: {result.stderr}")
            return []
            
    except Exception as e:
        print(f"Error checking git status: {e}")
        return []

def stage_files():
    """Stage the organized files for commit"""
    print("\n=== STAGING FILES ===")
    
    # Stage the organized directories
    directories_to_stage = [
        "testing/",
        "installation/", 
        "docs/",
        "archive/",
        "README.md",
        ".gitignore"
    ]
    
    staged_items = []
    
    for item in directories_to_stage:
        if os.path.exists(item):
            try:
                result = subprocess.run(
                    ["git", "add", item],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    staged_items.append(item)
                    print(f"✓ Staged: {item}")
                else:
                    print(f"✗ Failed to stage {item}: {result.stderr}")
                    
            except Exception as e:
                print(f"✗ Error staging {item}: {e}")
    
    return staged_items

def create_commit_message():
    """Create a comprehensive commit message"""
    commit_message = """Organize GlobalGenie testing suite and cleanup files

- Reorganized testing files into structured directories:
  * testing/ - Core testing scripts
  * installation/ - Installation utilities  
  * docs/ - Documentation and guides
  * archive/ - Debug scripts (archived)

- Added comprehensive testing suite covering:
  * Fresh Python environment installations
  * Cross-platform compatibility (Windows, macOS, Linux)
  * Python version compatibility (3.8+)
  * Virtual environment compatibility
  * Package manager variations
  * Import statement testing
  * CLI command verification

- Created installation utilities:
  * Simple installer for easy setup
  * Quick fix script for common issues
  * Windows batch installer

- Added documentation:
  * Testing strategy and methodology
  * Quick start guide
  * Windows-specific setup commands

- Cleaned up temporary and obsolete files
- Added proper .gitignore for Python projects

Testing suite is production-ready and covers all installation scenarios."""

    return commit_message

def main():
    """Main cleanup and git preparation"""
    print("Final Git Cleanup and Commit Preparation")
    print("=" * 50)
    
    # Step 1: Remove unwanted files
    removed_files = remove_unwanted_files()
    
    # Step 2: Check git status
    status_lines = check_git_status()
    
    # Step 3: Stage organized files
    staged_items = stage_files()
    
    # Step 4: Show commit message
    commit_message = create_commit_message()
    
    print("\n" + "=" * 60)
    print("CLEANUP COMPLETE - READY FOR COMMIT")
    print("=" * 60)
    print(f"Files removed: {len(removed_files)}")
    print(f"Items staged: {len(staged_items)}")
    print()
    print("Suggested commit command:")
    print('git commit -m "Organize GlobalGenie testing suite and cleanup files"')
    print()
    print("Or use the detailed commit message:")
    print("git commit -F -")
    print("Then paste the following message:")
    print()
    print(commit_message)
    print()
    print("After committing, push with:")
    print("git push origin main")

if __name__ == "__main__":
    main()