import hashlib
import sys
import time

print('''
  _________ ___ ___    _____   ________ ________    _____   _________                                   __
 /   _____//   |   \  /  _  \  \_____  \\\\_____  \  /  |  |  \_   ___ \  ____   _______  __ ____________/  |_  ___________
 \_____  \/    ~    \/  /_\  \  /  ____/ /  ____/ /   |  |_ /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
 /        \    Y    /    |    \/       \/       \/    ^   / \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
/_______  /\___|_  /\____|__  /\_______ \_______ \____   |   \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/       \/         \/         \/       \/    |__|          \/            \/          \/                 \/

---------------------------------------------------------------------------------------------------------------------------
A simple program that converts user input to SHA224 Hash.
Dec 2016 v2.0
by
NoDisassemble.me
---------------------------------------------------------------------------------------------------------------------------
''')

while True:

    sha224Len = "56"

    mystring = input("Enter String for SHA224 Hashing: ")
# SHA224 Hashing
    hash_object = hashlib.sha224(mystring.encode())
    print("")
    loading = "[+] Generating SHA224 Hash: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("\n[+] SHA224 Hashing Completed with " + sha224Len + " chars:")
    time.sleep(.5)
    x = "-"
    for i in range(1, int(sha224Len) + 1):
        print(x, end="")
    print("")
    # Generates SHA224 Hash
    print(hash_object.hexdigest())
    x = "-"
    for i in range(1, int(sha224Len) + 1):
        print(x, end="")
    print("")
    print("")
    input("Press Enter to convert another string:")
    print("")
    continue