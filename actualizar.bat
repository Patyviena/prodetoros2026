@echo off
title Prode Toros 2026 - Actualizador
echo.
echo  ============================================
echo   PRODE TOROS 2026 - Actualizando panel...
echo  ============================================
echo.

cd /d "%~dp0"
python update_prode.py

echo.
if %errorlevel% == 0 (
    echo  Panel listo en:
    echo  https://patyviena.github.io/prodetoros2026/
) else (
    echo  Algo salio mal. Revisa la conexion a internet.
)
echo.
pause
