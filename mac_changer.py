#!/usr/bin/env python
import subprocess

interface = input("please enter the name of the interface: ")
newMac = input("Please enter the new MAC address: ")
print("[+] Changing MAC address for " + interface)
subprocess.call("ifconfig " + interface + " down", shell = True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell = True)
subprocess.call("ifconfig " + interface + " up", shell = True)
subprocess.call("ifconfig", shell = True)
