#!/bin/bash
a=$(xprop -id `xdotool getactivewindow` | grep WM_CLASS | cut -d '"' -f4)
#notify-send -t 100 "$a"

case $a in
  Firefox )
  i3-msg "move container to workspace 4" 
    ;;
  Gvim )
  i3-msg "move container to workspace 3" 
    ;;
  Gnome-terminal )
  i3-msg "move container to workspace 3" 
    ;;
  Gnome-system-monitor )
  i3-msg "move container to workspace 1" 
    ;;
  Nautilus )
  i3-msg "move container to workspace 9" 
    ;;
  Pidgin )
  i3-msg "move container to workspace 5" 
    ;;
esac
