import hashlib
import sys
import time

print('''
  _________ ___ ___    _____   .____________________   _________                                   __
 /   _____//   |   \  /  _  \  |   ____/_   \_____  \  \_   ___ \  ____   _______  __ ____________/  |_  ___________
 \_____  \/    ~    \/  /_\  \ |____  \ |   |/  ____/  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
 /        \    Y    /    |    \/       \|   /       \  \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
/_______  /\___|_  /\____|__  /______  /|___\_______ \  \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/       \/         \/       \/             \/         \/            \/          \/                 \/

----------------------------------------------------------------------------------------------------------------------
A simple program that converts user input to SHA512 Hash.
Keywords [SHA512 Hash, SHA512 Hash Converter, SHA512 Converter]
Dec 2016 v2.0
by
NoDisassemble.me
----------------------------------------------------------------------------------------------------------------------
''')

while True:

    sha512Len = "128"

    mystring = input("Enter String for SHA512 Hashing: ")
# SHA512 Hashing
    hash_object = hashlib.sha512(mystring.encode())
    print("")
    loading = "[+] Generating SHA512 Hash: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("\n[+] SHA512 Hashing Completed with " + sha512Len + " chars:")
    time.sleep(.5)
    x = "-"
    for i in range(1, int(sha512Len) + 1):
        print(x, end="")
    print("")
    # Generates SHA512 Hash
    print(hash_object.hexdigest())
    x = "-"
    for i in range(1, int(sha512Len) + 1):
        print(x, end="")
    print("")
    print("")
    input("Press Enter to convert another string:")
    print("")
    continue
