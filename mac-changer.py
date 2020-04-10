#!/usr/bin/env python3

import subprocess

print("Note: this program only works on linux!")
# interface = "wlan0"
interface = input("Interface > ")
# desired_Mac = "00:11:22:33:44:55"
desired_Mac = input("What is your desired mac? ex:\n00:00:00:00:00:00\n")
print("[+] Changing MAC address for "+interface+" to "+desired_Mac)
# print("Starting Mac Changer")
subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+desired_Mac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
print("Mac changer finished")

