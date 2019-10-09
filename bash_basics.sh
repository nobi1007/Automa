#!/bin/bash

s1="hi"
s2="hi"

if [ "$s1" == "$s2" ]
then
	echo match
else
	echo no match
fi
read


#v76=`curl -o chromedriverv_76.zip https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip`

#v77=`curl -o chromedriverv_76.zip https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_win32.zip`

#v78=`curl -o chromedriverv_76.zip https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_win32.zip`

run C:\Program Files (x86)\Google\Chrome\Application\chromedriver_v76.exe
#wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value
#echo "$Version"
read
