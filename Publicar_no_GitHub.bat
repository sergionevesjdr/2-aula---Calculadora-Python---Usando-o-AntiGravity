@echo off
title Publicar no GitHub - PyCalc
color 0B

cd /d "%~dp0"

echo ======================================================
echo       ASSISTENTE DE PUBLICACAO NO GITHUB
echo ======================================================
echo.

set /p GNAME="Digite seu Nome ou Usuario do GitHub: "
set /p GEMAIL="Digite seu E-mail do GitHub: "

git config --global user.name "%GNAME%"
git config --global user.email "%GEMAIL%"

echo.
echo [1/3] Preparando arquivos e criando commit...
git init
git add .
git commit -m "feat: Calculadora em Python com testes e documentacao"
git branch -M main

echo.
echo ======================================================
echo [2/3] Conectar com o repositorio do GitHub
echo ======================================================
echo Acesse https://github.com/new e crie seu repositorio.
echo Copie a URL do repositorio criado.
echo (Exemplo: https://github.com/usuario/calculadora-python.git)
echo.
set /p REPO_URL="Cole a URL do seu repositorio aqui: "

set REPO_URL=%REPO_URL:"=%
set REPO_URL=%REPO_URL: =%

git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

echo.
echo [3/3] Enviando arquivos para o GitHub...
echo (Se abrir uma janela pedindo autorizacao, clique em Sign in with browser)
echo.

git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================
    echo   PARABENS! Projeto publicado com sucesso no GitHub!
    echo   URL: %REPO_URL%
    echo ======================================================
) else (
    echo.
    echo Sincronizando com o GitHub...
    git pull origin main --rebase --allow-unrelated-histories >nul 2>&1
    git push -u origin main
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ======================================================
        echo   PARABENS! Projeto publicado com sucesso no GitHub!
        echo   URL: %REPO_URL%
        echo ======================================================
    ) else (
        echo.
        echo [!] Ocorreu um problema no envio.
        echo Verifique se a URL esta correta e se o repositorio existe.
    )
)

echo.
pause
