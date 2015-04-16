#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is a simple wrapper which prefixes each i3status line with custom
# information. It is a python reimplementation of:
# http://code.stapelberg.de/git/i3status/tree/contrib/wrapper.pl
#
# To use it, ensure your ~/.i3status.conf contains this line:
#     output_format = "i3bar"
# in the 'general' section.
# Then, in your ~/.i3/config, use:
#     status_command i3status | ~/i3status/contrib/wrapper.py
# In the 'bar' section.
#
# In its current version it will display the cpu frequency governor, but you
# are free to change it to display whatever you like, see the comment in the
# source code below.
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.
from subprocess import Popen, PIPE
import sys
import re
import json
import time

I3STATUS_CMD = 'i3status'

NOW_PLAYING_CMD = "mpc current -f '%title%'"

CAPSLOCK_CMD="xset q | grep 'Caps Lock' | awk '"+'{split($0,a," "); print a[4]}'+"'"

def get_governor():
    """ Get the current governor for cpu0, assuming all CPUs use the same. """
    with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor') as fp:
        return fp.readlines()[0].strip()

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line(process):
  ''' Interrupted respecting reader for stdin. '''
  try:
    line = process.stdout.readline().strip()
    if not line:
      sys.exit(3)
    return line
    # exit on ctrl-c
  except KeyboardInterrupt:
    sys.exit()
lock_dic={}
lock_dic['off']='#0C7922'
lock_dic['on']='#DC322F'


if __name__ == '__main__':
    p = Popen(I3STATUS_CMD, stdout=PIPE, shell=True)
    p2=Popen(CAPSLOCK_CMD,stdout=PIPE,shell=True)
    p3=Popen(NOW_PLAYING_CMD,stdout=PIPE,shell=True)
    caps_status=p2.communicate()[0][0:-1]
    # waiting 1 second to get the first lines
    time.sleep(1)
    if p.poll() is None:
    # Skip the first line which contains the version header.
      print_line(read_line(p))
      # The second line contains the start of the infinite array.
      print_line(read_line(p))
    while p.poll() is None:
                        #print(caps_status)
        #p2.kill()
        line, prefix = read_line(p), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        #j.insert(0, {'full_text' : '%s' % get_governor(), 'name' : 'gov'})
        #j.insert(0,{'full_text':'CAPS '+caps_status,'name':'Caps_Lock', 'color':lock_dic[caps_status]})
        p2=Popen(CAPSLOCK_CMD,stdout=PIPE,shell=True)
        p3=Popen(NOW_PLAYING_CMD,stdout=PIPE,shell=True)
        now_playing=p3.communicate()
        #print("fooooooooooooo")
        #print(now_playing)
        caps_status=p2.communicate()[0][0:-1]
        j.insert(0,{'full_text':"Caps Lock "+caps_status ,'name':'Caps_Lock', 'color':lock_dic[caps_status]})
        j.insert(0,{'full_text':"NP: "+now_playing[0][:-1] ,'name':'now_playing', 'color':'#E6BB1D'})
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
