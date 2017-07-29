import urllib.request
import time
import sys

print("""
========================================================================================================
  _________________  .____    .__  ____   ____    .__           _________ .__                   __
 /   _____/\_____  \ |    |   |__| \   \ /   /_ __|  |   ____   \_   ___ \|  |__   ____   ____ |  | __
 \_____  \  /  / \  \|    |   |  |  \   Y   /  |  \  |  /    \  /    \  \/|  |  \_/ __ \_/ ___\|  |/ /
 /        \/   \_/.  \    |___|  |   \     /|  |  /  |_|   |  \ \     \___|   Y  \  ___/\  \___|    <
/_______  /\_____\ \_/_______ \__|    \___/ |____/|____/___|  /  \______  /___|  /\___  >\___  >__|_ \\
        \/        \__>       \/                             \/          \/     \/     \/     \/     \/
========================================================================================================
Description: A script that checks to see if a website is vulnerable to SQL injections.
Keywords: [Python 3, SQL Injection, Vulnerability Check]
July 2017 v3.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------------
""")
# Sets user agent for headers to avoid Bad Request
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = { 'User-Agent' : user_agent }

# Checks for valid URL
def validURL(target):
    print("")
    loading = "Looking up Host: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 \
                or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    request = urllib.request.Request(target, headers = headers)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request)
        print("")
        print("[+] Host Found [+]")
        print("")
        return True
    except urllib.request.HTTPError as e:
        print("")
        print(e)
        print("[!] Host Not Accepting Requests [!]")
        print("")
        input("Press [Enter] to try another URL:")
        print("")
        return False
    except urllib.request.URLError:
        print("")
        # print(e)
        print("[!] Host Not Found [!]")
        print("")
        input("Press [Enter] to try another URL:")
        print("")
        return False

# Check to see if site is vuln to sql injection
def vulnCheck1():
    print("--------------------------------------------------")
    print("[+] Checking Host for Type 1 SQL Vulnerability...")
    time.sleep(2)
    loading = "[!] Appending /index.php?cat_ID=1=1\' or \'1\' to URL: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 \
                or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    try:
        inject = urllib.request.urlopen(target + "/index.php?cat_ID=1=1\' or \'1\'")
        body = inject.read()
        sourceCode = body.decode('utf-8')
        print("")
        time.sleep(1)
        print("[+] Retrieving Error...")
        time.sleep(1)
        print("[!] " + body.decode('utf-8'), end="")
        time.sleep(2)
        if "You have an error in your SQL syntax" in sourceCode:
            print("")
            print("[+] Target Vulnerable to Type 1 SQL Injection [+]")
            print("--------------------------------------------------")
            print("")
            # input("Press [Enter] to try another Target:")
            # print("")
            return True
    except urllib.request.HTTPError:
        print("")
        print("[-] Target not Vulnerable to Type 1 SQL Injection [-]")
        print("--------------------------------------------------")

        print("")
        # input("Press [Enter] to try another Target:")
        # print("")
        return False
    except urllib.request.URLError:
        print("")
        print("[-] Target not Vulnerable to SQL Injection [-]")
        print("--------------------------------------------------")
        print("")
        # input("Press [Enter] to try another Target:")
        # print("")
        return False

# Check to see if site is vuln to sql injection
def vulnCheck2():
    print("--------------------------------------------------")
    print("[+] Checking Host for Type 2 SQL Vulnerability...")
    time.sleep(2)
    loading = "[!] Appending /subcat.php?id=1\' to URL: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 \
                or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    try:
        inject = urllib.request.urlopen(target + "/subcat.php?id=1\'")
        body = inject.read()
        sourceCode = body.decode('utf-8')
        print("")
        time.sleep(1)
        print("[+] Retrieving Error...")
        time.sleep(1)
        print("[!] " + body.decode('utf-8'), end="")
        time.sleep(2)
        if "You have an error in your SQL syntax" in sourceCode:
            print("")
            print("[+] Target Vulnerable to Type 2 SQL Injection [+]")
            print("--------------------------------------------------")
            print("")
            input("Press [Enter] to try another Target:")
            print("")
            return True
    except urllib.request.HTTPError:
        print("")
        print("[-] Target not Vulnerable to Type 2 SQL Injection [-]")
        print("--------------------------------------------------")
        print("")
        input("Press [Enter] to try another Target:")
        print("")
        return False
    except urllib.request.URLError:
        print("")
        print("[-] Target not Vulnerable to SQL Injection [-]")
        print("--------------------------------------------------")
        print("")
        input("Press [Enter] to try another Target:")
        print("")
        return False
#------------------ Program Actual ---------------------
while True:
    target = input("Enter Target Full URL: ")
    try:
        if validURL(target) == True:
            time.sleep(1)
            if vulnCheck1() == True:
                time.sleep(1)
                vulnCheck2()
            else:
                time.sleep(1)
                vulnCheck2()
#catch for invalid url
    except ValueError as e:
        print("")
        print("[!] " + str(e) + " [!]")
        print("[!] Target URL must be full path http://www.site.com [!]")
        print("")
        input("Press [Enter] to try another URL")
        print("")
