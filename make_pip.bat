rem activate k36
if exist build\*.* del build\*.* /q /s
if exist dist\*.* del dist\*.* /q /s
if exist pysga.egg-info\*.* del pysga.egg-info\*.* /q /s

rmdir build
rmdir dist
rmdir pysga.egg-info

python setup.py sdist bdist_wheel

if "%1"=="v" goto VERIFY
python -m twine upload dist/*
goto end

:VERIFY
python -m twine check dist/*

:end
pause
