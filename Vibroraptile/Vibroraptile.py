import vlc
import os
import time

import subprocess

pdpatch = "/home/pi/Documents/Pd/Vibroraptile/pipeline.pd"
pdpath = '/usr/lib/puredata/tcl/pd-gui.tcl'

subprocess.Popen([pdpath, pdpatch])
#subprocess.Popen([pdpath,pdpatch])
time.sleep(5)
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('Video/final_lowres.mp4')
player.set_media(Media)
player.play()
