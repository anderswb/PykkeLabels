set HOME=C:\Users\Anders\
C:\Python34\python.exe setup.py bdist_egg upload --identity="Anders Brandt" --sign --quiet
C:\Python34\python.exe setup.py bdist_wininst --target-version=3.4 register upload --identity="Anders Brandt" --sign --quiet
C:\Python34\python.exe setup.py sdist upload --identity="Anders Brandt" --sign
pause