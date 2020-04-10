#!/usr/bin/env python

import subprocess

print("Note: this program only works on linux!")
print("Starting Mac Changer")
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
print("Mac changer finished")

