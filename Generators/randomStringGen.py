import string
import random
import sys
import time

print('''
=======================================================================================================================
__________                    .___                 _________ __         .__                   ________
\______   \_____    ____    __| _/____   _____    /   _____//  |________|__| ____    ____    /  _____/  ____   ____
 |       _/\__  \  /    \  / __ |/  _ \ /     \   \_____  \\\   __\_  __ \  |/    \  / ___\  /   \  ____/ __ \ /    \\
 |    |   \ / __ \|   |  \/ /_/ (  <_> )  Y Y  \  /        \|  |  |  | \/  |   |  \/ /_/  > \    \_\  \  ___/|   |  \\
 |____|_  /(____  /___|  /\____ |\____/|__|_|  / /_______  /|__|  |__|  |__|___|  /\___  /   \______  /\___  >___|  /
        \/      \/     \/      \/            \/          \/                     \//_____/           \/     \/     \/

-----------------------------------------------------------------------------------------------------------------------
Description: Program that generates a random string from given input. Option to include symbols and punctuation or not.
Keywords: [Python 3, Random String Generator, Random Character Generator, Password Generator]
Dec 2016 v1.0
by
NoDisassemble.me
-----------------------------------------------------------------------------------------------------------------------
''')

while True:
    # User input for string length
    try:
        pwdLen = int(input("Please enter the length of string: "))
    except ValueError:
        print("")
        # Catch if a non int is submitted
        print("[!]Invalid Entry")
        input("Press Enter to try again:")
        print("")
    else:
        include = input("Include symbols and punctuation? Yes or No: ")
        # Yes will yield alpha, digi, punct and special chars in string generation
        if include in ["Yes", "yes", "Y", "y"]:
            # Just alphanumeric characters
            chars = string.ascii_letters + string.digits
            # Alphanumeric + special characters
            chars = string.ascii_letters + string.digits + string.punctuation
            # Loading bar
            loading = "[+] Generating Random String: [-------------------]"
            print("")
            for i in range(101):
                time.sleep(0.03)
                sys.stdout.write("\r" + loading + " %d%%" % i)
                if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                    loading = loading.replace("-", "=", 1)
                sys.stdout.flush()
            print("")
            print("")
            print("[+] String Generated with " + str(pwdLen) + " chars:")
            time.sleep(.5)
            # Prints dash for length of output
            x = "-"
            for i in range(1, pwdLen+1):
                print(x, end="")
            print("")
            # Generates string with all options
            print("".join((random.choice(chars)) for x in range(int(pwdLen))))
            # Prints dash for length of output
            x = "-"
            for i in range(1, pwdLen+1):
                print(x, end="")
            print("")
            print("")
            input("Press Enter to generate another string:")
            print("")
            continue
        # No will yield only alphanumeric chars
        if include in ["No", "no", "N", "n"]:
            # Just alphanumeric characters
            chars = string.ascii_letters + string.digits
            # Loading bar
            loading = "[+] Generating Random String: [-------------------]"
            print("")
            for i in range(101):
                time.sleep(0.03)
                sys.stdout.write("\r" + loading + " %d%%" % i)
                if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                    loading = loading.replace("-", "=", 1)
                sys.stdout.flush()
            print("")
            print("")
            print("[+] String Generated with " + str(pwdLen) + " chars:")
            time.sleep(.5)
            # Prints dash for length of output
            x = "-"
            for i in range(1, pwdLen + 1):
                print(x, end="")
            print("")
            # Generates only alpha string
            print("".join((random.choice(chars)) for x in range(int(pwdLen))))
            # Prints dash for length of output
            x = "-"
            for i in range(1, pwdLen + 1):
                print(x, end="")
            print("")
            print("")
            input("Press Enter to generate another string:")
            print("")
            continue
        # Catch all for invalid yes or no entry
        else:
            print("")
            print("[!] Invalid entry: ")
            input("Press Enter to try again:")
            print("")
