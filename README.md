jasper-finalproject-client
=============

*Copyright (c) 2014-2015, Charles Marsh, Shubhro Saha & Jan Holthuis. All rights reserved.*

Jasper is covered by the MIT license, a permissive free software license that lets you do anything you want with the source code, as long as you provide back attribution and ["don't hold \[us\] liable"](http://choosealicense.com). For the full license text see the [LICENSE.md](LICENSE.md) file.

*Note that this licensing only refers to the Jasper client code (i.e.,  the code on GitHub) and not to the disk image itself (i.e., the code on SourceForge).*

## Documentation
### 1. Installation
Go to [Jasper Official Web](http://www.jasperproject.github.io/documentation) for a complete documentation, but instead I refer to [this video](https://www.youtube.com/watch?v=ZOEl527SpFI&t=2059s)
#### I found these errors while installing that might be useful:
```
sudo pip install --upgrade gTTS
```
- ImportError: Cannot import name IncompleteRead
> Solution
```
rm -rf /usr/lib/python2.7/dist-packages/requests*
```
This is caused by IncompleteLibrary function is deprecated on pip higher version

- ImportError: No module named req
> Solution
```
sudo python -m pip install --upgrade pip==9.0.3
```
Change the pip version of your system

```
./jasper.py
```
- AttributeError: 'NoneType' object has no attribute 'group'
> Solution
Go to this [discussion] (https://github.com/Boudewijn26/gTTS-token/pull/8/commits/8af6d4b1a672275c506f21af8cfc9ed0c4d4d31a) and this [solution] (https://github.com/Boudewijn26/gTTS-token/pull/8/commits/42936a779eae5a411d2be0da56cdb386a4123a0a)

After successfully running your jasper, you should be able to initiate basic keyword provided by the API. 

### 2. Configure OpenWeatherMap (OWM)
By default, Jasper has its own weather configuration. However, the response is somewhat short, incomplete and not detail. If you want a more detail response, you need to configure OpenWeatherMap
> Follow this [link] (https://github.com/G10DRAS/JasperModules) to configure your OWM

### 3. Configure GPIO
#### LED
> Components you will need:
- Breadboard
- LED
- Resistor
- Jumper wires (male-female)
Please refer to this [link] (https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins) to setup the circuit
We will set the pins on the GPIO using python. Go to this [page] (https://www.raspberrypi.org/documentation/usage/gpio/python/README.md) and you will find the resources you need.

#### LIRC
> Components you will need:
- IR receiver
- IR transmitter
- General Purpose Transistor NPN

LIRC or LINUX Infrared Remote Control will decode and send infrared signals commonly used remote controls. After finishing this [tutorial] (https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581), you will be able to use your Raspberry PI as a universal remote.

#### If this error occurs:
```
irsend:  command failed: SEND_ONCE Samsung KEY_POWER
irsend: transmission failed
```
> Solution
```
sudo /etc/init.d/lirc restart
sudo /dev/lirc0
```
This will restart your lirc configuration and set the device into default

### 4. Google Calendar
Jasper will be able to use your Google account for saving events and reminders. Refer to this [github repository] (https://github.com/marclave/Jasper-Google-Calendar) to find out how to enable your Google Calendar API.

### 5. Setting up Spotify
Jasper will be able to enter music/spotify mode after [configuration] (http://jasperproject.github.io/documentation/configuration/#spotify-integration)
However, this link seems to be outdated. Use this instead
```
sudo apt-get remove mopidy-spotify
git clone https://github.com/BlackLight/mopidy-spotify.git
cd mopidy-spotify
sudo git checkout fix/incompatible_playlists
sudo python2 setup.py build install
```

### 6. Setting up alarm
Say "Set An Alarm" to Jasper. Jasper will reply by saying, "what time did you want the alarm?". 
There are three commands to choose from "tomorrow", "today", "every monday/tuesday/wednesday/thursday/friday/saturday/sunday" 
followed with "AT (clock do you want to alarmed) AM/PM" and Jasper will set the alarm at the proposed time. 
If the alarm triggers at the proposed time, you need to say "Jasper" first before saying "stop the alarm" to stop the alarm that was triggered.


