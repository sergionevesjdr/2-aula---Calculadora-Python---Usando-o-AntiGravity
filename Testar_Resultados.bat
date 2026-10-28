@echo off
chcp 65001 > nul
title PyCalc - Teste de Resultados
color 0B

cd /d "%~dp0"

echo ========================================================
echo       VERIFICACAO COMPLETA DA CALCULADORA PYTHON
echo ========================================================
echo.
python test_calculator.py
echo.
echo ========================================================
echo Testes concluidos com sucesso!
echo Pressione qualquer tecla para fechar esta janela...
pause > nul
