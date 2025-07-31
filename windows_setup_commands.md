# Windows PowerShell Commands for New Repository Setup

## Correct Windows PowerShell Commands:

### Step 1: Clean up the project first
```powershell
python cleanup_project.py
```

### Step 2: Remove old git history (Windows PowerShell)
```powershell
# Remove .git directory (Windows PowerShell command)
Remove-Item -Recurse -Force .git

# Initialize new git repository
git init
```

### Step 3: Add all your project files
```powershell
git add .
```

### Step 4: Make initial commit
```powershell
git commit -m "Initial commit: GlobalGenie comprehensive testing framework with 100% success rate"
```

### Step 5: Set up main branch and remote
```powershell
git branch -M main
git remote add origin https://github.com/ggenie099-a11y/global-genie.git
```

### Step 6: Push to GitHub
```powershell
git push -u origin main
```

## Complete Windows PowerShell Sequence:
```powershell
# 1. Clean up project
python cleanup_project.py

# 2. Remove old git and start fresh (Windows PowerShell)
Remove-Item -Recurse -Force .git
git init

# 3. Add all files
git add .

# 4. Initial commit
git commit -m "Initial commit: GlobalGenie comprehensive testing framework with 100% success rate"

# 5. Setup main branch and remote
git branch -M main
git remote add origin https://github.com/ggenie099-a11y/global-genie.git

# 6. Push to GitHub
git push -u origin main
```

## Alternative if Remove-Item doesn't work:
```powershell
# Alternative method to remove .git folder
rmdir /s .git

# Then continue with:
git init
git add .
git commit -m "Initial commit: GlobalGenie comprehensive testing framework with 100% success rate"
git branch -M main
git remote add origin https://github.com/ggenie099-a11y/global-genie.git
git push -u origin main
```

## Key Differences for Windows:
- ❌ `rm -rf .git` (Linux/Mac)
- ✅ `Remove-Item -Recurse -Force .git` (Windows PowerShell)
- ✅ `rmdir /s .git` (Windows CMD alternative)

Use the Windows PowerShell commands above! 🚀