import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="the new MAC address")
    return parser.parse_args()

def change_mac(interface, new_mac) :
    print("[+] Changing MAC address for " + interface)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    subprocess.call("ifconfig", shell=True)


(options, arguments) = get_arguments()

interface = options.interface
new_mac = options.new_mac

change_mac(interface, new_mac)
