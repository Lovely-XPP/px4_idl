@echo off
cd %~dp0

:: ������ļ�
powershell -Command "Remove-Item -Path %dir%px4_cpps -Recurse -Force"
:: �����ļ���
mkdir px4_cpps

echo ################################# ��idl��Ϣת��Ϊc++�ļ�...

setlocal enabledelayedexpansion  

set dir=%~dp0

:: Check java binary.
set java_exec=java

java -version > NUL 2>&1

if not %ERRORLEVEL%==0 (
   if not "%JAVA_HOME%"=="" (
      set java_exec="%JAVA_HOME%\bin\java"
   ) else (
      echo Java binary cannot be found. Please, make sure its location is in the PATH environment variable or set JAVA_HOME environment variable.
      exit /B 65
   )
)

cd %dir%px4_idls
%java_exec% -jar "%dir%/Tools/fastddsgen.jar" -replace -typeros2 -d %dir%px4_cpps *.idl

echo ################################# ��Ϣת�����.

echo ------------------------------------------------
echo ################################# �������ļ�...

:: .cxx -> .cpp
python.exe -u %dir%Tools/handle_cppmessages.py

echo ################################# �������ļ����.
echo ------------------------------------------------
pause