PRACTICAL – 5 Raspberry Pi GPS Module Interfacing.
STEP 1 :- (Create a virtual environment)
1) Installing the venv module:-
sudo apt install python3-venv
2) Creating a new virtual environment. myenv is user-defined name
python3 -m venv myenv
3) Activate the Virtual Environment
source myenv/bin/activate
4) It should look like :- (myenv) pi@raspberrypi:- $
(If virtual environment is already created just activate the environment)
STEP 2 :- Enter the following commands one by one, pressing Enter after each.
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service

STEP 3 :- Installing minicom
sudo apt-get install minicom

STEP 4 :- Installing pynmea2
pip install pynmea2 --break-system-packages

STEP 5 :-
sudo cat /dev/ttyS0
(This will run in the background. To stop this press ctrl + C)

STEP 6 :-
code:
import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio #if error here use command:- pip install Rpi.GPIO
gpio.setmode(gpio.BCM)
port = &quot;/dev/ttyS0&quot; # the serial port to which the pi is connected.

#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while 1:
try:
data = ser.readline()
print(data)
except:
print(&quot;loading&quot;)
#wait for the serial port to churn out data

if data[0:6] == &#39;$GPRMC&#39;:
msg = pynmea2.parse(data)
print msg
time.sleep(2)

STEP 7:- To deactivate virtual environment
deactivate