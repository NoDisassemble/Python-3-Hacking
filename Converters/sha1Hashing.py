import hashlib
import sys
import time

print('''
  _________ ___ ___    _____  ____  _________                                   __
 /   _____//   |   \  /  _  \/_   | \_   ___ \  ____   _______  __ ____________/  |_  ___________
 \_____  \/    ~    \/  /_\  \|   | /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
 /        \    Y    /    |    \   | \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
/_______  /\___|_  /\____|__  /___|  \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/       \/         \/              \/            \/          \/                 \/

---------------------------------------------------------------------------------------------------
A simple program that converts user input to SHA1 Hash.
Keywords [SHA1 Hash, SHA1 Hash Converter, SHA1 Converter]
Dec 2016 v2.0
by
NoDisassemble.me
---------------------------------------------------------------------------------------------------
''')

while True:

    sha1Len = "40"

    mystring = input("Enter String for SHA1 Hashing: ")
# SHA1 Hashing
    hash_object = hashlib.sha1(mystring.encode())
    print("")
    loading = "[+] Generating SHA1 Hash: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("\n[+] SHA1 Hashing Completed with " + sha1Len + " chars:")
    time.sleep(.5)
    x = "-"
    for i in range(1, int(sha1Len) + 1):
        print(x, end="")
    print("")
    # Generates SHA1 Hash
    print(hash_object.hexdigest())
    x = "-"
    for i in range(1, int(sha1Len) + 1):
        print(x, end="")
    print("")
    print("")
    input("Press Enter to convert another string:")
    print("")
    continue
