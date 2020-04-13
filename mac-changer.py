#!/usr/bin/env python3

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address on")
    parser.add_option("-m", "--mac", dest="desired_mac", help="Desired new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.desired_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, desired_Mac):
    print("[+] Changing MAC address for " + interface + " to " + desired_Mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", desired_Mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not find mac address!")


options = get_arguments()


print("Note: this program only works on linux!")


# code that can no longer be used, but that I also dont want to delete
# interface = input("Interface > ")
# interface = options.interface
# desired_Mac = input("What is your desired mac? ex:\n00:00:00:00:00:00\n")
# desired_Mac = options.desired_mac

current_mac = get_current_mac(options.interface)
print("Current Mac = "+str(current_mac))
change_mac(options.interface, options.desired_mac)

