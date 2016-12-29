import time
from selenium import webdriver

print('''
==========================================================================================================================
__________                         __________        _____                      .__
\______   \_____     ____   ____   \______   \ _____/ ____\______   ____   _____|  |__
 |     ___/\__  \   / ___\_/ __ \   |       _// __ \   __\\\_  __ \_/ __ \ /  ___/  |  \\
 |    |     / __ \_/ /_/  >  ___/   |    |   \  ___/|  |   |  | \/\  ___/ \___ \|   Y  \\
 |____|    (____  /\___  / \___  >  |____|_  /\___  >__|   |__|    \___  >____  >___|  /
                \//_____/      \/          \/     \/                   \/     \/     \/

-------------------------------------------------------------------------------------------------------------------------
Description: A program that will open your web browser to a given URL and refresh that page however many times you input.
Keywords: [Python 3, Web Page Refresh, Web Page Open, Website Page Refresh, Website Page Open]
Dec 2016 v2.0
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------------------------------
''')

while True:
    # Input for Target URL
    targetURL = input("Please enter the full URL to Refresh: ")
    # Input for number of times to refresh page
    cycleNum = input("How many times to refresh page? ")
    # Error check for invalid response
    if cycleNum.isdigit():
        pass
    else:
        print("")
        print("[!] Invalid response. Value must be a number.")
        input("[!] Press Enter to try again:")
        print("")
        continue
    # Input for time to wait between page refresh
    refTime = input("Number of seconds to wait for each page refresh: ")
    # Error check for invalid response
    if refTime.isdigit():
        pass
    else:
        print("")
        print("[!] Invalid response. Value must be a number.")
        input("[!] Press Enter to try again:")
        print("")
        continue

    print("")
    print("-------------------------------------------------------------------------------------------")
    print("[+] Opening " + targetURL + ". Refreshing the page " + cycleNum + " times. [+]")
    print("-------------------------------------------------------------------------------------------")

    # Opens Firefox
    driver = webdriver.Firefox()

    # Begin program
    count = 1
    while count < int(cycleNum) + 1:
        driver.get(targetURL)
        time.sleep(int(refTime))
        driver.refresh()
        print("[+] Refreshing...")
        count = count+1
    # Prints after completion of page refresh
    print("-----------------------------------------------------------------------")
    print("[+] Completed. " + targetURL + " Refreshed " + cycleNum + " times. [+]")
    print("-----------------------------------------------------------------------")
    print("")
    input("Press Enter to Refresh another web page.")
    print("")
