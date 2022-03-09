cd venv\Scripts
call activate.bat
cd..
cd..
behave -f html -o report.html
pause