#!/bin/bash

/usr/bin/amixer set Master 15% unmute;
/usr/bin/amixer set PCM 100% unmute;
/usr/bin/amixer set Headphone 100% unmute;
/usr/bin/amixer set Speaker 100% unmute;
for (( kk=1; kk<12; kk+=1 )); do
  /usr/bin/amixer set Master 5%+;
  sleep 20;
done
