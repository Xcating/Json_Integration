@echo off
:begin
echo �򿪸��µ�ַ���Ǵ�Github�ֿ�(a/b)
set /p abc=
if "%abc%"=="a" goto a
if "%abc%"=="b" goto b
echo �������˸�ɶ���Ⱑ����Сд��a��b
pause
goto begin
:a
start https://github.com/Xcating/Json_Integration/archive/refs/heads/main.zip
pause
:b
start https://github.com/Xcating/Json_Integration
pause