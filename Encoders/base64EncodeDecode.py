import sys
import time
import base64

print('''
======================================================================================================================================================
__________                        ________   _____   ___________                       .___           /\ ________                          .___
\______   \_____    ______ ____  /  _____/  /  |  |  \_   _____/ ____   ____  ____   __| _/____      / / \______ \   ____   ____  ____   __| _/____
 |    |  _/\__  \  /  ___// __ \/   __  \  /   |  |_  |    __)_ /    \_/ ___\/  _ \ / __ |/ __ \    / /   |    |  \_/ __ \_/ ___\/  _ \ / __ |/ __ \\
 |    |   \ / __ \_\___ \\\  ___/\  |__\  \/    ^   /  |        \   |  \  \__(  <_> ) /_/ \  ___/   / /    |    `   \  ___/\  \__(  <_> ) /_/ \  ___/
 |______  /(____  /____  >\___  >\_____  /\____   |  /_______  /___|  /\___  >____/\____ |\___  > / /    /_______  /\___  >\___  >____/\____ |\___  >
        \/      \/     \/     \/       \/      |__|          \/     \/     \/           \/    \/  \/             \/     \/     \/           \/    \/

======================================================================================================================================================

Description: Python 3 script that Encodes/Decodes user input to base64 and back.
Keywords: [Python 3, Base64 Encoder, Base64 Decoder]
Jan 2017 v2.0
by
NoDisassemble.me
------------------------------------------------------------------------------------------------------------------------------------------------------
''')


def base64encode():
    dataEncode = input("Enter data to be encoded: ")
    encode = base64.b64encode(dataEncode.encode())
    print("")
    loading = "[+] Base64 Encoding: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 \
                or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 \
                or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("")
    print("[!] Encoding = " + str(encode) + "")


def base64decode():
    dataDecode = input("Enter data to be decoded: ")
    decode = base64.b64decode(dataDecode)
    print("")
    loading = "[+] Base64 Decoding: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 \
                or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 \
                or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("")
    print("[!] Decoding = " + str(decode) + "")


def invalid_opt():
    # Catch for invalid response
    print("[!] Invalid choice")


while True:
    # Options for Base64 Encode & Decode
    options = {"A": ["Base64 Encode", base64encode], "B": ["Base64 Decode", base64decode], }
    for option in options:
        print(option + ") " + options.get(option)[0])
    # User input for choice
    choice = input("Which Encoding would you like to perform? [A or B] ")
    print("")
    val = options.get(choice.upper())
    if val is not None:
        action = val[1]
    else:
        action = invalid_opt
    action()
    print("")
    input("Press Enter to Encode/Decode again.")
    print("")
