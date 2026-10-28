@echo off
chcp 65001 > nul
title PyCalc - Calculadora Python
color 0A

:: Garante que o terminal execute dentro da pasta do script
cd /d "%~dp0"

echo ========================================================
echo       Iniciando a Calculadora Python (PyCalc)...
echo ========================================================
echo.

python gui.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Ocorreu um problema ao iniciar a janela gráfica.
    echo Tentando abrir o modo interativo no terminal...
    echo.
    python cli.py
    pause
)
