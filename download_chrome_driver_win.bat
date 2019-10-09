@ECHO OFF

REM open the registry editor using "regedit"

FOR /F "skip=2 tokens=2,*" %%A IN ( 'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v "version"') DO set "version=%%B"

REM ECHO %version%

set version_initials=%version:~0,2%

REM echo %version_initials%

set v1=76
set v2=77
set v3=78

echo.
echo Current Chrome version is %version% . 
echo Downloading required version . . .
echo.
if "%version_initials%" == "%v1%" (
    curl -o chromedriver_v76.zip --insecure https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip --ssl-no-revoke
) else (	
	if "%version_initials%" == "%v2%" ( 
		curl -o chromedriver_v77.zip --insecure https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_win32.zip --ssl-no-revoke
	) else ( 
		curl -o chromedriver_v78.zip --insecure https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_win32.zip --ssl-no-revoke
	)
)
echo.
echo Chromedriver_v%version_initials% successfully installed !
echo.
echo Starting extraction . . . 
echo.
set mypath=%cd%
powershell Expand-Archive -Force %mypath%\chromedriver_v%version_initials%.zip %mypath%
echo.
echo Installing dependencies . . .
pip install cx-freeze
pip install selenium
pip install PyQt4-4.11.4-cp36-cp36m-win32.whl
echo.
echo Installing -- WhatsBulk --
echo.
python setup.py build
echo.
pause