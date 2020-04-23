#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # use for debug

    answered_list, unanswerd_list = scapy.srp(arp_request_broadcast, timeout =1)
    print(answered_list.summary())


scan("127.0.0.1/24")
# this is a placeholder, not an actual IP - NOTE: changed to loopback
# TODO - remove placeholder
