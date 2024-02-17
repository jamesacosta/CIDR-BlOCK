import nmap

scanner = nmap.PortScanner()

ip = input("Insert a direction ip")
print("this is the ip you typed")
scanner.scan(ip)

print(scanner.all_hosts())

