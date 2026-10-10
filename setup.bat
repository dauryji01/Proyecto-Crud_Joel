
@echo off
title Preparar Proyecto CRUD
cd /d "%~dp0"

echo ========================================
echo     SISTEMA DE GESTION DE SUPLEMENTOS
echo ========================================
echo.

echo [1/4] Comprobando Python...
py --version
if errorlevel 1 (
    echo ERROR: Instala Python desde https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/4] Creando entorno virtual...
if not exist "venv\Scripts\python.exe" (
    py -m venv venv
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo.
echo [3/4] Instalando dependencias...
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias.
    pause
    exit /b 1
)

echo.
echo [4/4] Preparando la base de datos...
venv\Scripts\python.exe -m flask --app run.py db upgrade
if errorlevel 1 (
    echo ERROR: No se pudo preparar la base de datos.
    echo Comprueba que la carpeta migrations este incluida.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Proyecto preparado correctamente.
echo Para iniciarlo, ejecuta iniciar.bat
echo ========================================
pause
