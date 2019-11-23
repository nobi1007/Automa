## Running the demo

1. Clone the repository and cd to whatsenv:
```
git clone link_to_repo && cd Automa/WhatApp/whatsenv
```
2. Download the required packages:
```
pip3 install -r requirements.txt
```
3. Open the wa_main.py file in your editor and change the path of chromedriver according to your pc (in line 68).

4. Run the wa_main.py file
```
sudo python3 wa_main.py
```

##### Additional


5. For PYQt4 installation(system wide):
```
sudo apt-get install python3-PyQt4
```
6. For getting PYQt4 into the virtualenv after installation (from step 5): 
   1. Just go to /usr/lib/python3/dist-packages/ and the copy the folder of PyQt4 and all the sip related files from that directory. 
   2. Then go to your virtualenv folder (here, viren) and then go to /lib/python3.6/site-packages and paste all the copied items in here, and you are good to go now :) .

#### NOTE: _here, we didn't install the PyQt4 and sip explicity, but they have been added in the site-packages folder already_.


-----------



## Creating a virtualenv 

1. Install virtualenv from using pip3:
```
pip3 install virtualenv
```
2. Check the installation:
```
virtualenv --version
```
3. Create a virtual environment in your suitable directory with any name (here "viren")
```
virtualenv viren
```
4. Launch the virtual environment "viren":
```
source viren/bin/activate
```
5. For deactivating the virtualenv
```
deactivate
```
