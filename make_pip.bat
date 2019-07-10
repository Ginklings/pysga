
if exist build\*.* del build\*.* /q /s
if exist dist\*.* del dist\*.* /q /s
if exist pysga.egg-info\*.* del pysga.egg-info\*.* /q /s

rmdir build
rmdir dist
rmdir pysga.egg-info

python setup.py sdist bdist_wheel
python -m twine upload dist/*

pause
