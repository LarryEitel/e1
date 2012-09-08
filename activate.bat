@echo off
set PROJECTS_ROOT=C:\Users\Larry\__prjs\_ex\_prjs\e1
set PROJECT_NAME=ea
set PYTHON_ROOT=C:\Python27
set PYTHONHOME=%PYTHON_ROOT%
set PROJECT_ROOT=%PROJECTS_ROOT%\%PROJECT_NAME%
set DJANGO_SETTINGS_MODULE=%PROJECT_NAME%.settings

set PATH=%PATH%;%PROJECT_ROOT%\scripts\windows

set PYTHONPATH=%PROJECTS_ROOT%;%PROJECT_ROOT%;%PROJECT_ROOT%\parts;%PROJECT_ROOT%\apps;%PROJECT_ROOT%\ve\Lib;%PROJECT_ROOT%\ve\Lib\site-packages;%PYTHON_ROOT%;%PYTHON_ROOT%\Lib;%PYTHON_ROOT%\Lib\site-packages

REM %PROJECT_ROOT%\ve\Scripts\activate.bat
ve\Scripts\activate.bat

@echo on

set DEV=True
cd ea

@cmd.exe
