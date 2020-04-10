#!/usr/bin/env python

import subprocess

print("Note: this program only works on linux!")
# print("Defining variables")
interface = "wlan0"
desired_Mac = "00:11:22:33:44:55"
print("[+] Changing MAC address for "+interface+" to "+desired_Mac)
# print("Starting Mac Changer")
subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+desired_Mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
print("Mac changer finished")

