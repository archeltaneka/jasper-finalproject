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
./python.py
```
AttributeError: 'NoneType' object has no attribute 'group'
> Solution
Go to this [discussion] (https://github.com/Boudewijn26/gTTS-token/pull/8/commits/8af6d4b1a672275c506f21af8cfc9ed0c4d4d31a
https://github.com/Boudewijn26/gTTS-token/pull/8/commits/42936a779eae5a411d2be0da56cdb386a4123a0a)


 
