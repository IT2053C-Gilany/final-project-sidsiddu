@echo off
REM IT2053C Environment Setup Script for Windows
REM This script sets up the conda environment without auto-activation

IF "%1"=="" (
    echo Error: You must provide your 6+2 username as the first argument.
    echo Usage: setup.bat ^<your_6+2_username^>
    exit /b 1
)
SET USERNAME=%1

echo Setting up IT2053C environment for %USERNAME%...

REM Check if conda is available
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: conda is not installed or not in PATH
    pause
    exit /b 1
)

REM Create or update the environment
conda env list | findstr "IT2053C" >nul
if %errorlevel% equ 0 (
    echo Updating existing IT2053C environment...
    conda env update -f environment.yml
) else (
    echo Creating new IT2053C environment...
    conda env create -f environment.yml
)

REM Set the STUDENT_USERNAME environment variable
conda env config vars set STUDENT_USERNAME=%USERNAME% -n IT2053C

echo.
echo ✅ Environment setup complete!
echo.
echo To use the environment:
echo   conda activate IT2053C
echo.
echo To deactivate:
echo   conda deactivate
echo.
echo To view environment variables:
echo   conda env config vars list
echo.
echo To access STUDENT_USERNAME in Python:
echo   import os
echo   username = os.environ.get('STUDENT_USERNAME')
echo.
pause 