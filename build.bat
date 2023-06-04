@echo off
echo This file must be run in Python Terminal.
echo Before building you must complete the following points:
echo # create venv with name 'venv':
echo py -m venv venv
echo # activate venv:
echo venv/scripts/activate
echo # install requirements:
echo pip install -r requirements
echo # change DEV variable in passbox.py to False
echo DEV = False
echo # run this file to build exe:
echo ./build

set /p answer=Did you? y/n:
if "%answer%"=="y" (
    pyinstaller -w -F -i passbox.ico --add-data "./venv/Lib/site-packages/customtkinter;customtkinter/" --add-data "passbox.ico;." passbox.py
)

pause

@REM -w --windowed --- Do not provide a console window for standard i/o.
@REM -F --onefile / -D --onedir
@REM -i filename.ico
@REM --add-data "SRC;DEST" --- This option can be used multiple times.

