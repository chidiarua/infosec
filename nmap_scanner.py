#script for scanning open ports using the nmap package
import nmap

scanner = nmap.PortScanner()

print("this is a simple nmap automation tool")
print("**************************************")

ip_address = input("please, input ip address: ")
print("The IP entered is: ", ip_address)
type(ip_address)

resp = input("""\nselect type of scan: 
                1. SYN ACK Scan
                2. UDP Scan
                3. Comprehensive Scan\n""")
print("you have selected option: ", resp)   

if resp == '1':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['tcp'].keys())
elif resp == '2':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['udp'].keys())
elif resp == '3':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['tcp'].keys())
else:
    print('enter a valid option')