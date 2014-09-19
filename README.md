# i3-wm-config by benkaiser

This is my configuration for the i3 window manager.  

I have used both `awesome` and `i3` and felt `i3` is a bit more customizable. Try both of them before choosing if you hate working with mouse and dig tiling of windows.

I am still figuring out to get all the parts of the original repo working. Right now, the status bar is the default provided by i3.
`i3pystatus` is not being used. 
`workspace_controller.py` is not being used as workspace navigation is slow.
Using the default commands for the navigation keybindings


# Dependencies

- i3 - the i3 window manager
- py3status - for changing the status bar
- dmenu - for menu operations
- python3 - for my workspace controller script

# Keyboard Shortcuts

Mod Key: Windows(Super) key (Mod4)

## i3 keys
Mod + Shift + b = Reload i3 configuration file  
Mod + Shift + r = Restart i3 (reload )  
Mod + Shift + e = Exit i3  

## Applications
Mod + Enter = Terminal  
Mod + d = Run dmenu (with mods to open application in the current space)  

## Window Operations
Mod + Shift + c = Kill current window  
Mod + f = Make current window fullscreen  


Mod + Shift + 1 = Move window to workspace 1 in block  
Mod + Shift + 2 = Move window to workspace 2 in block  
Mod + Shift + 3 = Move window to workspace 3 in block  
Mod + Shift + 4 = Move window to workspace 4 in block  
Mod + Shift + 5 = Move window to workspace 5 in block  
Mod + Shift + 6 = Move window to workspace 6 in block  
Mod + Shift + 7 = Move window to workspace 7 in block  
Mod + Shift + 8 = Move window to workspace 8 in block  
Mod + Shift + 9 = Move window to workspace 9 in block  
Mod + Shift + 0 = Move window to workspace 0 in block  

##Enter resize mode
Mod + r = Resize window  

## Navigation. Changed to replicate vim bindings
Mod + h = Focus window to the left  
Mod + j = Focus window down  
Mod + k = Focus window up  
Mod + l = Focus window to the right  


## Layouts
Mod + Shift+Control+h = Split horizontal layout  
Mod + v = Split vertical layout  
Mod + s = Stacking layout  
Mod + w = Tabbed layout  
Mod + e = Default layout  
Mod + space = Toggle between floating/tiling layers  

## System Manipulation
Volume Decrease Key (varies on keyboard) / XF86AudioLowerVolume = Lower volume by 2%  
Volume Increase Key (varies on keyboard) / XF86AudioRaiseVolume = Raise volume by 2%  
Volume Mute Key (varies on keyboard) / XF86AudioMute = Mute volume  

#Rhythmbox bindings
Shift+Control+space Play/Pause
Shift+Control+j Play Next Song
Shift+Control+k Play Previous Song

## Added vim style bindings
Mod + Left = Switch to workspace -1 (e.g. 1 to 0)  
Mod +Control+ h = Switch to workspace -1 (e.g. 1 to 0)  
Mod + Right = Switch to workspace +1 (e.g 1 to 2)  
Mod + Control+l = Switch to workspace +1 (e.g 1 to 2)  
Mod + Up = Switch to workspace +10 (e.g 1 to 11)  
Mod + Control+k = Switch to workspace +10 (e.g 1 to 11)  
Mod + Down = Switch to workspace -10 (e.g 1 to -9)  
Mod + Control+j = Switch to workspace -10 (e.g 1 to -9)  

##Move to previous workspace
Mod+b

The blocks refer to blocks of 10, so if you were on workspace 15 and pressed `Mod + 2` you would move to 12. The same applies to `Mod + Shift + 2` except it moves the window to the selected workspace.  

## Other Modifications
Custom color scheme centering around my favourite color #44bbff.  
My own application startup list, just sift through what you want  
