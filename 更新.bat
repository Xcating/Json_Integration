@echo off
:begin
echo 打开更新地址还是打开Github仓库(a/b)
set /p abc=
if "%abc%"=="a" goto a
if "%abc%"=="b" goto b
echo 你输入了个啥玩意啊，就小写的a和b
pause
goto begin
:a
start https://github.com/Xcating/Json_Integration/archive/refs/heads/main.zip
pause
:b
start https://github.com/Xcating/Json_Integration
pause