from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import sys
import codecs

print('''
=============================================================================================================
  ___ ___________________  .____        _________
 /   |   \__    ___/     \ |    |      /   _____/ ________________  ______   ___________
/    ~    \|    | /  \ /  \|    |      \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \\
\    Y    /|    |/    Y    \    |___   /        \  \___|  | \// __ \|  |_> >  ___/|  | \/
 \___|_  / |____|\____|__  /_______ \ /_______  /\___  >__|  (____  /   __/ \___  >__|
       \/                \/        \/         \/     \/           \/|__|        \/

-------------------------------------------------------------------------------------------------------------
Description: Simple program that grabs the HTML source code from a given website with option to save to disk.
Keywords: [Python 3, HTML Scraper, HTML Grabber, HTML Parser, Web Scraper, HTML Source Code]
Dec 2016 v1.3
by
NoDisassemble.me
-------------------------------------------------------------------------------------------------------------
''')

while True:
    # Def for getting url Title
    def getTitle(url):
        try:
            html = urlopen(url)
        except HTTPError:
            return None
        try:
            bsObj = BeautifulSoup(html.read(), "html.parser")
            title = bsObj.h1
        except AttributeError:
            return None
        return title

    # Def for getting HTML source code
    def getHtml(url):
        try:
            html = urlopen(url)
        except HTTPError:
            return None
        try:
            bsObj = BeautifulSoup(html.read(), "html.parser")
            fullHtml = bsObj.prettify()
        except AttributeError:
            return None
        return fullHtml

    # User input for url to be scrapped.
    targetURL = input("Enter full URL for HTML Scraper: ")

    # Begin loading bar
    loading = "[+] Scraping HTML from " + targetURL + ": [-------------------]"
    print("")
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("[!] This may take some time...")

    # Begin program
    title = getTitle(targetURL)
    print("")
    print("----------------------------------------------------------------------")
    print("[+] Begin HTML Scraping for " + targetURL + " [+]")
    print("----------------------------------------------------------------------")
    print("")
    if title is None:
        print("Title could not be found")
    else:
        print(title)
        print("------END TITLE-------")
    # Gets HTML source code
    fullHtml = getHtml(targetURL)
    if fullHtml is None:
        print("HTML could not be found")
    else:
        if sys.stdout.encoding != 'cp850':
            sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
        if sys.stderr.encoding != 'cp850':
            sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
        print(fullHtml)
        # Save file to disk
        print("")
        print("------------------------------------------------------------------------")
        print("[!] End HTML Scraping for " + targetURL + " [!]")
        print("------------------------------------------------------------------------")
        print("")
        # Save File to Disk if answer Yes
        saveAs = input("Save output to disk? [Yes, No] ")
        if saveAs in ["Yes", "yes", "Y", "y"]:
            fileName = input("Save file as: ")
            saveFile = open(fileName, "w", encoding="utf8")
            saveFile.write("----------------------------------------------------------------- \n")
            saveFile.write("[+] Begin HTML Scraping for " + targetURL + " [+] \n")
            saveFile.write("----------------------------------------------------------------- \n")
            saveFile.write("\n")
            saveFile.write(fullHtml)
            saveFile.write("\n")
            saveFile.write("----------------------------------------------------------------- \n")
            saveFile.write("[!] End HTML Scraping for " + targetURL + " [!] \n")
            saveFile.write("----------------------------------------------------------------- \n")
            saveFile.close()
            loading = "[+] Saving " + fileName + " to Disk: [-------------------]"
            print("")
            for i in range(101):
                time.sleep(0.03)
                sys.stdout.write("\r" + loading + " %d%%" % i)
                if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
                    loading = loading.replace("-", "=", 1)
                sys.stdout.flush()
            print("")
            print("[+] File Saved.")
            time.sleep(1)
            print("")
            input("Press Enter to try another URL:")
            print("")
            continue
        # Save File to Disk if answer NO
        if saveAs in ["No", "no", "N", "n"]:
            print("")
            print("[!] File discarded...")
            time.sleep(1)
            print("")
            input("Press Enter to try another URL:")
            print("")
            continue
        # Save File to Disk if any other answer
        else:
            print("")
            print("[!] Invalid response.")
            time.sleep(1)
            print("")
            input("Press Enter to try another URL:")
            print("")
