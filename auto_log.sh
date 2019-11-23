#!/bin/bash
today=$(date +%y%m%d)
#the cause to use the command ls is in that to bulit a new #file,not in that the command ls.
ls /usr/bin -al > $today.log

