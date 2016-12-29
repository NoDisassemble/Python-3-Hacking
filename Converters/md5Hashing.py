import hashlib
import sys
import time

print('''
==============================================================================================
   _____  ________   .________ _________                                   __
  /     \ \______ \  |   ____/ \_   ___ \  ____   _______  __ ____________/  |_  ___________
 /  \ /  \ |    |  \ |____  \  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
/    Y    \|    `   \/       \ \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
\____|__  /_______  /______  /  \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/        \/       \/          \/            \/          \/                 \/

----------------------------------------------------------------------------------------------
Description: A simple program that converts your input to MD5 Hash.
Keywords: [Python 3, MD5 Hash, MD5 Hash Converter, MD5 Converter]
Dec 2016 v2.0
by
NoDisassemble.me
----------------------------------------------------------------------------------------------
''')

while True:

    md5Len = "32"

    mystring = input("Enter String for MD5 Hashing: ")
# MD5 Hashing
    hash_object = hashlib.md5(mystring.encode())
    print("")
    loading = "[+] Generating MD5 Hash: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("\n[+] MD5 Hashing Completed with " + md5Len + " chars:")
    time.sleep(.5)
    x = "-"
    for i in range(1, int(md5Len) + 1):
        print(x, end="")
    print("")
    # Generates MD5 Hash
    print(hash_object.hexdigest())
    x = "-"
    for i in range(1, int(md5Len) + 1):
        print(x, end="")
    print("")
    print("")
    input("Press Enter to convert another string:")
    print("")
    continue
