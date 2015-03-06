#!/usr/bin/env python
from random import randint
from subprocess import Popen, PIPE,call
p = Popen("ls ~/pro/xkcd/xkcd_comics_full_png/*.png", stdout=PIPE, shell=True)
result=p.communicate()[0].split('\n')[0:-1]
n=len(result)
comic=result[randint(0,n)]
call(["i3lock","-i",comic,"-t"])


