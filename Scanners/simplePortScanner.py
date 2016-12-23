import socket
import threading
from queue import Queue
import time
import sys

print('''
__________              __      _________
\______   \____________/  |_   /   _____/ ____ _____    ____   ____   ___________
 |     ___/  _ \_  __ \   __\  \_____  \_/ ___\\\__  \  /    \ /    \_/ __ \_  __ \\
 |    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
 |____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /___|  /\___  >__|
                                      \/     \/     \/     \/     \/     \/

------------------------------------------------------------------------------------
Simple port scanner with range input and threading.
Keywords [Simple Port Scanner, Threading Port Scanner]
2016 v1.3
by
NoDisassemble.me
------------------------------------------------------------------------------------
''')

while True:

    print_lock = threading.Lock()

    target = input("Enter target IP: ")
    try:
        number = int(input("How many ports to scan? Example 500: "))
        print("")
        loading = "[+] Scanning Ports on " + target + ": [-------------------]"
        for i in range(101):
            time.sleep(0.05)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("[!] This may take some time...")
        time.sleep(2)
        print("")

        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((target, port))
                with print_lock:
                    x = "-"
                    for i in range(1, 25):
                        print(x, end="")
                    print("")
                    print("[+] port", port, "is open")
                    x = "-"
                    for i in range(1, 25):
                        print(x, end="")
                    print("")
            except:
                pass


        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()


        q = Queue()

        for x in range(30):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(1, int(number) + 1):
            q.put(worker)
        q.join()
        print("")
        print("[!] Scan Completed")
        print("")
        input("Press Enter to try another IP: ")
        print("")
    except ValueError:
        print("")
        print("[!] Invalid response:")
        input("Press enter to try again:")
        print("")
