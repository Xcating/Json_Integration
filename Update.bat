@echo off
:begin
echo Open update address or open Github warehouse (a/b)
set /p abc=
if "%abc%"=="a" goto a
if "%abc%"=="b" goto b
echo Only can send a / b
pause
goto begin
:a
start https://github.com/Xcating/Json_Integration/archive/refs/heads/dev.zip
pause
:b
start https://github.com/Xcating/Json_Integration/tree/dev
pause