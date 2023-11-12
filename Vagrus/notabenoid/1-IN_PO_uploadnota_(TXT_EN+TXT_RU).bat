@echo off
setlocal enabledelayedexpansion
for /R file_nota %%a in (*_EN.txt) do (
set x="%%a" 
Enterider_Notabenoid.exe -encode_po "%%a" -tra_file_txt !x:_EN.txt=_RU.txt!)
pause
