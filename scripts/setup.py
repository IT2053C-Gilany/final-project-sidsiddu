#!/usr/bin/env python3
"""
IT2053C Environment Setup Script
Cross-platform script that works on Windows, macOS, and Linux
"""

import sys
import subprocess
import platform
import argparse

def run_command(command, shell=True):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=shell, capture_output=True, text=True, check=False)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_conda():
    """Check if conda is available"""
    success, stdout, stderr = run_command("conda --version")
    if not success:
        print("❌ Error: conda is not installed or not in PATH")
        print("Please install Anaconda or Miniconda first.")
        return False
    print(f"✅ Found conda: {stdout.strip()}")
    return True

def check_environment_exists():
    """Check if IT2053C environment already exists"""
    success, stdout, stderr = run_command("conda env list")
    if success:
        return "IT2053C" in stdout
    return False

def setup_environment(username):
    """Set up the conda environment"""
    print("Setting up IT2053C environment...")
    
    if not check_conda():
        return False
    
    env_exists = check_environment_exists()
    
    if env_exists:
        print("📦 Updating existing IT2053C environment...")
        success, stdout, stderr = run_command("conda env update -f environment.yml")
    else:
        print("🆕 Creating new IT2053C environment...")
        success, stdout, stderr = run_command("conda env create -f environment.yml")
    
    if success:
        print("✅ Environment setup complete!")
        
        # Set the STUDENT_USERNAME environment variable
        print(f"🔧 Setting STUDENT_USERNAME to: {username}")
        set_var_success, set_var_stdout, set_var_stderr = run_command(f"conda env config vars set STUDENT_USERNAME={username} -n IT2053C")
        
        if set_var_success:
            print("✅ STUDENT_USERNAME environment variable set successfully!")
        else:
            print("⚠️  Warning: Could not set STUDENT_USERNAME environment variable:")
            print(set_var_stderr)
        
        return True
    else:
        print("❌ Error setting up environment:")
        print(stderr)
        return False

def print_usage_instructions():
    """Print usage instructions"""
    print("\n" + "="*50)
    print("📋 USAGE INSTRUCTIONS")
    print("="*50)
    print()
    print("To activate the environment:")
    print("  conda activate IT2053C")
    print()
    print("To deactivate:")
    print("  conda deactivate")
    print()
    print("To update the environment later:")
    print("  conda env update -f environment.yml")
    print()

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="IT2053C Environment Setup")
    parser.add_argument("--username", type=str, help="Provide your 6+2 username to the script")
    args = parser.parse_args()

    if args.username and len(args.username) >= 3:
        print(f"👋 Hello, {args.username}!")
    else:
        print("❌ You must provide your 6+2 username to the script.")
        print("Usage:\tpython setup.py --username <your_username>\n\tOR\n\tpython setup.py --username=<your_username>")
        sys.exit(1)

    print("🚀 IT2053C Environment Setup")
    print("="*30)
    print(f"Platform: {platform.system()} {platform.release()}")
    print()
    
    if setup_environment(args.username):
        print_usage_instructions()
    else:
        print("\n❌ Setup failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 