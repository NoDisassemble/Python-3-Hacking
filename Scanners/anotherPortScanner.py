import socket
import sys
import time

print('''
__________              __      _________
\______   \____________/  |_   /   _____/ ____ _____    ____   ____   ___________
 |     ___/  _ \_  __ \   __\  \_____  \_/ ___\\\__  \  /    \ /    \_/ __ \_  __ \\
 |    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
 |____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /___|  /\___  >__|
                                      \/     \/     \/     \/     \/     \/

---------------------------------------------------------------------------------------
A simple port scanner with range input that displays ports being scanned in real time.
2016 v2.0
by
NoDisassemble.me
---------------------------------------------------------------------------------------
''')

class PyPortScan:

    def __init__(self):
        pass
    def ScanConnection(self, target_host, target_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_host, target_port))
            x = "-"
            for i in range(1, 25):
                print(x, end="")
            print("")
            print(" [+] Tcp-Port %i open" % (target_port))
            x = "-"
            for i in range(1, 25):
                print(x, end="")
            print("")
            s.close()
        except:
            print("  [-] Tcp-Port %i closed" % (target_port))

    def ScanPort(self, target_host, target_ports):
        try:
            target_ip = socket.gethostbyname(target_host)
        except:
            print('[!] Cannot Resolve "%s": Unknown Host' % (target_host))
            print("")
            return

        try:
            target_name = socket.gethostbyaddr(target_ip)
            print("\n[+] Scan Results for: %s" % (target_name[0]))
        except:
            print("")
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("\n[+] Scan Results for: %s" % (target_ip))
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")

        socket.setdefaulttimeout(1)

        for port in target_ports:
            print("Scanning Port: %s" % (port))
            self.ScanConnection(target_host, int(port))

while True:

    def main():
        URL = input("Enter Target IP: ")
        try:
            number=int(input("How many ports to scan? Example 500: "))
            print("")
            loading = "[+] Establishing Connections: Ports 0 ~ " + str(number) + " [-------------------]"
            for i in range(101):
                time.sleep(0.05)
                sys.stdout.write("\r" + loading + " %d%%" % i)
                if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                    loading = loading.replace("-", "=", 1)
                sys.stdout.flush()
            print("")
            time.sleep(1)
            print("[!] This may take some time...")
            print("")
        # Main Program
            pps = PyPortScan()
            p_list = []
            for i in range(0, int(number) +1):
                p_list.append(int(i))
            pps.ScanPort(URL, p_list)
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")
            print("[!] Port Scan Complete: ")
            x = "-"
            for i in range(1, 35):
                print(x, end="")
            print("")
            print("")
            input("Press Enter to run another scan:")
            print("")
        except ValueError:
            print("")
            print("[!] Invalid response:")
            input("Press enter to try again:")
            print("")



    if __name__ == '__main__':
        main()

