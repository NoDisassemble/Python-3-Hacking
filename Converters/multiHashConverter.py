import hashlib
import sys
import time

print('''
===============================================================================================================================
   _____        .__   __  .__    ___ ___               .__      _________                                   __
  /     \  __ __|  |_/  |_|__|  /   |   \_____    _____|  |__   \_   ___ \  ____   _______  __ ____________/  |_  ___________
 /  \ /  \|  |  \  |\   __\  | /    ~    \__  \  /  ___/  |  \  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \\
/    Y    \  |  /  |_|  | |  | \    Y    // __ \_\___ \|   Y  \ \     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/
\____|__  /____/|____/__| |__|  \___|_  /(____  /____  >___|  /  \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|
        \/                            \/      \/     \/     \/          \/            \/          \/                 \/

-------------------------------------------------------------------------------------------------------------------------------
Description: A script that converts user input to many different types of Hashes. MD5, SHA1, SHA224, SHA256, SHA384 and SHA512.
Keywords: [Python 3, MD5, SHA1, SHA224, SHA256, SHA384, SHA512, Hash Converter]
Dec 2016 v2.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------------------------------------
''')

while True:

    md5Len = "32"
    sha1Len = "40"
    sha224Len = "56"
    sha256Len = "64"
    sha384Len = "96"
    sha512Len = "128"

    mystring = input("Enter String to hash: ")
    print("")
    hash = input("Choose your Algorithm: MD5, SHA1, SHA224, SHA256, SHA384, SHA512: ")
# MD5 Hashing
    if hash in ["md5", "MD5"]:
        hash_object = hashlib.md5(mystring.encode())
        print("")
        # Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + md5Len + " chars:")
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
# SHA1 Hashing
    if hash in ["sha1", "SHA1"]:
        hash_object = hashlib.sha1(mystring.encode())
        print("")
        #Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + sha1Len + " chars:")
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
# SHA224 Hashing
    if hash in ["sha224", "SHA224"]:
        hash_object = hashlib.sha224(mystring.encode())
        print("")
        # Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + sha224Len + " chars:")
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
# SHA256 Hashing
    if hash in ["sha256", "SHA256"]:
        hash_object = hashlib.sha256(mystring.encode())
        print("")
        # Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + sha256Len + " chars:")
        time.sleep(.5)
        x = "-"
        for i in range(1, int(sha256Len) + 1):
            print(x, end="")
        print("")
        # Generates SHA256 Hash
        print(hash_object.hexdigest())
        x = "-"
        for i in range(1, int(sha256Len) + 1):
            print(x, end="")
        print("")
        print("")
        input("Press Enter to convert another string:")
        print("")
        continue
# SHA384 Hashing
    if hash in ["sha384", "SHA384"]:
        hash_object = hashlib.sha384(mystring.encode())
        print("")
        # Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + sha384Len + " chars:")
        time.sleep(.5)
        x = "-"
        for i in range(1, int(sha384Len) + 1):
            print(x, end="")
        print("")
        # Generates SHA384 Hash
        print(hash_object.hexdigest())
        x = "-"
        for i in range(1, int(sha384Len) + 1):
            print(x, end="")
        print("")
        print("")
        input("Press Enter to convert another string:")
        print("")
        continue
# SHA512 Hashing
    if hash in ["sha512", "SHA512"]:
        hash_object = hashlib.sha512(mystring.encode())
        print("")
        # Loading bar
        loading = "[+] Generating " + hash.upper() + " Hash: [-------------------]"
        for i in range(101):
            time.sleep(0.03)
            sys.stdout.write("\r" + loading + " %d%%" % i)
            if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                loading = loading.replace("-", "=", 1)
            sys.stdout.flush()
        print("")
        print("\n[+] " + hash.upper() + " Hashing Completed with " + sha512Len + " chars:")
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
    # Catchall for wrong selection
    else:
        print("")
        print("[!] Invalid selection:")
        print("")
        input("Press Enter to try again:")
        print("")
