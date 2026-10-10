@echo off
title Instalacion del entorno Python

echo ========================================
echo   Configurando entorno Python
echo ========================================
echo.

REM Comprobar Python
python --version
if errorlevel 1 (
    echo.
    echo ERROR: Python no esta instalado o no esta en PATH.
    pause
    exit /b 1
)

"env\Scripts\python.exe" run.py
pause