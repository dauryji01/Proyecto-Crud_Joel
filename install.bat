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

REM Crear entorno virtual si no existe
if not exist "env\Scripts\python.exe" (
    echo.
    echo Creando entorno virtual...
    python -m venv env

    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo.
echo Actualizando pip...
env\Scripts\python.exe -m pip install --upgrade pip

echo.
echo Instalando dependencias...

if exist "requirements.txt" (
    env\Scripts\python.exe -m pip install -r requirements.txt
) else (
    echo No se encontro requirements.txt
    echo Instalando Flask...
    env\Scripts\python.exe -m pip install flask
)

flask --app run:app db upgrade

echo.
echo ========================================
echo   Instalacion terminada
echo ========================================
echo.
echo Para activar el entorno manualmente:
echo env\Scripts\activate
echo.
pause