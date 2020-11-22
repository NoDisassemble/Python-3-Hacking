#!/usr/bin/python3

import urllib.request
import subprocess
import timeit
import time
import sys

print('''
================================================================================
  _      __    __     ___                      ___   ___
 | | /| / /__ / /    / _ \___ _______  ___    |_  | / _ \\
 | |/ |/ / -_) _ \  / , _/ -_) __/ _ \/ _ \  / __/_/ // /
 |__/|__/\__/_.__/ /_/|_|\__/\__/\___/_//_/ /____(_)___/


May 2018 v2.1
by
NoDisassemble.me
================================================================================
''')


def TargetAlive():
    # Sets user agent for headers to avoid 400 Bad Request and 403 Forbidden Errors
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    print("----------- [ Validating ] -----------")
    print("[!] Checking if Target is up... [!]")
    request = urllib.request.Request('http://' + target, headers=headers)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request)
        print("[+] Target is up! [+]")
        print("[+] Continuing with WebRecon 2.0 [+]")
        print("")
        return True
    except:
        print("[-] Target is down! [-]")
        print("")
        ContinueAnyway = input("Would you like to continue anyway? Y or N ")
        print("")
        if ContinueAnyway in ["Y", "y", "Yes", "YES", "yes"]:
            return True
        else:
            print("[!] Aborting WebRecon 2.0 [!]")
            print("")
            time.sleep(3)
            return False


def Whatweb():
    print("------------ [ Whatweb ] -------------")
    startTime = timeit.default_timer()
    print("[!] Scan in progress... [!]")
    time.sleep(3)
    f = open("whatweb.txt", "w")
    subprocess.call(['whatweb', '--color=never', '%s' % target], stdout=f)
    print("[+] Scan complete! [+]")
    print("[+] Output saved to file. [+]")
    elapsed = int(timeit.default_timer() - startTime) // 60  # Count in minutes
    print("[!] Whatweb ran for " + str(elapsed) + " minutes. [!]")
    print("")


def Nmap():
    print("-------------- [ Nmap ] --------------")
    startTime = timeit.default_timer()
    print("[!] Scan in progress... [!]")
    time.sleep(3)
    f = open("nmap.txt", "w")
    subprocess.call(['nmap', '-A', '-v', '-f', '%s' % target], stdout=f)
    print("[+] Scan complete! [+]")
    print("[+] Output saved to file. [+]")
    elapsed = int(timeit.default_timer() - startTime) // 60  # Count in minutes
    print("[!] Nmap ran for " + str(elapsed) + " minutes. [!]")
    print("")


def Nikto():
    print("------------- [ Nikto ] --------------")
    startTime = timeit.default_timer()
    print("[!] Scan in progress... [!]")
    time.sleep(3)
    f = open("nikto.txt", "w")
    subprocess.call(['nikto', '-a','no', '-h', '%s' % target], stdout=f)
    print("[+] Scan complete! [+]")
    print("[+] Output saved to file. [+]")
    elapsed = int(timeit.default_timer() - startTime) // 60  # Count in minutes
    print("[!] Nikto ran for " + str(elapsed) + " minutes. [!]")
    print("")


def Dirb():
    print("-------------- [ Dirb ] --------------")
    startTime = timeit.default_timer()
    print("[!] Scan in progress... [!]")
    time.sleep(3)
    f = open("dirb.txt", "w")
    dirbTarget = "http://" + target
    subprocess.call(['dirb', dirbTarget, '-S', '-w'], stdout=f)
    print("[+] Scan complete! [+]")
    print("[+] Output saved to file. [+]")
    elapsed = int(timeit.default_timer() - startTime) // 60  # Count in minutes
    print("[!] Dirb ran for " + str(elapsed) + " minutes. [!]")
    print("")


def summary():
    print("------------ [ Summary ] -------------")
    elapsed = int(timeit.default_timer() - startTime) // 60  # Count in minutes
    print("[!] Scan Complete [!]")
    print("[+] Target: " + target + " [+]")
    print("[!] WebRecon 2.0 ran for " + str(elapsed) + " minutes. [!]")
    print("")


# WebRecon core function calls
def WebRecon():
    if TargetAlive() is True:
        Whatweb()
        Nmap()
        Nikto()
        Dirb()
        print("")
        summary()
        ScanAgain = input("Would you like to Scan another Target? Y or N ")
        if ScanAgain in ["Y", "y", "Yes", "YES", "yes"]:
            pass
        else:
            print("")
            print("[!] Exiting WebRecon 2.0...")
            print("")
            time.sleep(2)
            sys.exit()
    else:
        ScanAgain = input("Would you like to Scan another Target? Y or N ")
        if ScanAgain in ["Y", "y", "Yes", "YES", "yes"]:
            pass
        else:
            print("")
            print("[!] Exiting WebRecon 2.0...")
            print("")
            time.sleep(2)
            sys.exit()


# Program actual
if __name__ == '__main__':
    while True:
        # Start total program timer
        startTime = timeit.default_timer()
        # Target host input
        print("")
        target = input(str("Target url: "))
        print("")
        # If target is alive then run WebRecon 2.0
        WebRecon()
