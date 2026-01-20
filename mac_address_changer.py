# MAC Address Changer
# Cambiador de direcciones MAC
# Use: sudo python3 mac_address_changer.py --interface <Enter name of NIC> --mac <Enter new MAC>
# Uso: sudo python3 mac_address_changer.py -i <Ingrese el nombre de la NIC> -m <Ingrese nueva MAC>
# Weapons of Mass Education℠ https://abstru.de
# Armas de Educación Masiva℠ https://abstru.de/es/index-es.html

import subprocess
import optparse
import re

print("-------------------------------------------------")
print("[+] MAC ADDRESS CHANGER")
print("-------------------------------------------------")


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address on")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Specify interface!")
    elif not options.new_mac:
        parser.error("[-] Specify new MAC!")
    return options


def change_mac(interface, new_mac):
    print("[+] " + interface + "    Interface")
    print("-------------------------------------------------")
    print("[+] " + get_current_mac(interface) + "  Current MAC")
    print("[+] " + new_mac + "  New MAC to be set")
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result_processed = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result_processed:
        return mac_address_search_result_processed.group(0)
    else:
        print("[+] Error: Could not read MAC address.")


def verify_changed_mac(interface):
    print("[+] verify_changed_mac valled")
    result = get_current_mac(options.interface)
    if current_mac == result:
        print(" Error, not changed")
    else:
        print("[+] " + current_mac.decode('utf-8') + " Verified\n")
        print("[+] Change successful!")


def print_result():
    if not current_mac == verified_changed_mac:
        print("[+] " + verified_changed_mac + "  Verified new MAC")
        print("-------------------------------------------------")
        print("[+] Weapons of Mass Education℠  https://abstru.de")
        print("-------------------------------------------------")
    if current_mac == verified_changed_mac:
        print("[+] " + verified_changed_mac + "  Error: Failed changing MAC")
        print("-------------------------------------------------")
        print("[+] Weapons of Mass Education℠  https://abstru.de")
        print("-------------------------------------------------")

options = get_args()

current_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

verified_changed_mac = get_current_mac(options.interface)

print_result()