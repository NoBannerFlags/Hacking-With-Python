#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest= "interface", help="Interface to change mac address on")
parser.add_option("-m", "--mac", dest= "desired_mac", help="Desired new mac address")

(options, arguments) = parser.parse_args()

print("Note: this program only works on linux!")

# interface = input("Interface > ")
interface = options.interface

# desired_Mac = input("What is your desired mac? ex:\n00:00:00:00:00:00\n")
desired_Mac = options.desired_mac

print("[+] Changing MAC address for "+interface+" to "+desired_Mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", desired_Mac])
subprocess.call(["ifconfig", interface, "up"])
