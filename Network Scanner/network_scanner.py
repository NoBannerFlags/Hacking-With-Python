#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

scan("127.0.0.1/24")
# this is a placeholder, not an actual IP - NOTE: changed to loopback
# TODO - remove placeholder
