from pyautogui import sleep
import pyautogui
from datetime import datetime
from config import size_w, size_h, pos_w, pos_h, chrome, res, os, max_round_login, max_round_check_element, delay_all_process, chrome_mac

def clickChromeScreen(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Chrome Window Screen")
        clickImage(arr, 'title', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Chrome Window Screen Not Found!")

def login(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Connect Wallet Button")
        clickImage(arr, 'connect', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Connect Wallet Button Not Found!")
    
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click MetaMask Button")
        clickImage(arr, 'metamask', os, loopCheck=False)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " MetaMask Button Not Found!")

    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Sign Button")
        clickImageFull(arr, 'sign', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Sign Button Not Found!")
        
    chrome = pyautogui.locateOnScreen(res + '/main.png', region=(arr), confidence=0.8)
    i = 0
    while chrome == None:
        chrome = pyautogui.locateOnScreen(res + '/main.png', region=(arr), confidence=0.8)
        sleep(1)
        i += 1
        if i > max_round_check_element:
            break

def heroes(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Heroes Button")
        clickImage(arr, 'heroes', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Heroes Button Not Found!")

def hunt(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Treasure Hunt Button")
        clickImage(arr, 'hunt', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Treasure Hunt Button Not Found!")

def back(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Back Button")
        clickImage(arr, 'back', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Back Button Not Found!")

def complete(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click New Map Button")
        clickImage(arr, 'newmap', os)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " New Map Button Not Found!")

def closeHeroes(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Close Button")
        clickImage(arr, 'close', os, gray=False)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Close Button Not Found!")

def error(arr):
    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click OK Button")
        clickImage(arr, 'ok', os, loopCheck=False)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " OK Button Not Found!")

    try:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Click Close Button")
        clickImage(arr, 'errorclose', os, gray=False, loopCheck=False)
    except:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Close Button Not Found!")

def refresh():
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Refresh Chrome Window Screen")
    if os == "0.5":
        pyautogui.hotkey('command', 'shift', 'r')
    else:
        pyautogui.hotkey('ctrl', 'shift', 'r')

def checkGameStage(arr):
    if pyautogui.locateOnScreen(res + '/connect.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "LOGIN"
    elif pyautogui.locateOnScreen(res + '/main.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "MAIN"
    elif pyautogui.locateOnScreen(res + '/upgrade.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "HEROES"
    elif pyautogui.locateOnScreen(res + '/complete.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "COMPLETE"
    elif pyautogui.locateOnScreen(res + '/ingame.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "INGAME"
    elif pyautogui.locateOnScreen(res + '/error.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "ERROR"
    elif pyautogui.locateOnScreen(res + '/says.png', region=(arr), grayscale=True, confidence=0.8) != None:
        return "SAYS"
    else:
        return "UNDEFINED"

def clickImage(arr, name, multiple, gray=True, loopCheck=True):
    chrome = pyautogui.locateOnScreen(res + '/' + name + '.png', region=(arr), grayscale=gray, confidence=0.8)
    i = 0
    while chrome == None and loopCheck:
        chrome = pyautogui.locateOnScreen(res + '/' + name + '.png', region=(arr), grayscale=gray, confidence=0.8)
        sleep(1)
        i += 1
        if i > max_round_check_element:
            break
    x, y = pyautogui.center(chrome)
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Clicking at " + str((int(x*multiple), int(y*multiple))))
    pyautogui.moveTo(x*multiple, y*multiple)
    pyautogui.click(x*multiple, y*multiple)
    sleep(1)

def clickImageFull(arr, name, multiple, gray=True, loopCheck=True):
    chrome = pyautogui.locateOnScreen(res + '/' + name + '.png', grayscale=gray, confidence=0.8)
    i = 0
    while chrome == None and loopCheck:
        chrome = pyautogui.locateOnScreen(res + '/' + name + '.png', grayscale=gray, confidence=0.8)
        sleep(1)
        i += 1
        if i > max_round_check_element:
            break
    x, y = pyautogui.center(chrome)
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Clicking at " + str((int(x*multiple), int(y*multiple))))
    pyautogui.moveTo(x*multiple, y*multiple)
    pyautogui.click(x*multiple, y*multiple)
    sleep(1)

def scrollToBottom(arr, num):
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Scroll to bottom")
    for i in range(num):
        clickImage(arr, 'ing', os)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y-100, os)
        pyautogui.mouseUp(button='left')

def manageHeroes(arr):
    scrollToBottom(arr, 3)
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Update Heroes Status")
    while 1:
        try:
            pyautogui.scroll(-50)
            clickImage(arr, 'work', os, gray=False, loopCheck=False)
            if checkGameStage(arr) == "ERROR":
                print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Error Found!")
                error(arr)
        except:
            break
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Resting Heroes Not Found!")

def process(arr):
    clickChromeScreen(arr)
    count = 0
    while True:
        stage = checkGameStage(arr)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Current Stage =", stage)
        if count > max_round_login:
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Reach Max Round, Skipping The Process")
            break
        elif stage == "LOGIN":
            if count > 0:
                print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Refresh Round =", str(count))
                refresh()
            login(arr)
            count += 1
        elif stage == 'MAIN':
            heroes(arr)
        elif stage == "HEROES":
            manageHeroes(arr)
            closeHeroes(arr)
            hunt(arr)
            break
        elif stage == "INGAME":
            back(arr)
        elif stage == "COMPLETE":
            complete(arr)
        elif stage == "ERROR":
            error(arr)
        elif stage == "SAYS":
            refresh()
            login(arr)
        else:
            clickChromeScreen(arr)
            sleep(15)
            count+=1
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Done Everything!")
    
def init():
    print()
    print("**************************")
    print(f"***{'BOMBERCRYPTO BOT' : ^20}***")
    print("**************************")
    print()

def relocateScreen():
    scn = []
    total = pyautogui.getWindowsWithTitle('Chrome')
    for i in range(len(total)):
        win = pyautogui.getWindowsWithTitle('Chrome')[i]
        win.size = (size_w, size_h)
        win.moveTo(chrome[i][0]*pos_w, chrome[i][1]*pos_h)
        scn.append([chrome[i][0]*pos_w, chrome[i][1]*pos_h, size_w, size_h])
        pyautogui.sleep(0.5)
    return scn

def main():
    init()
    screen = chrome_mac
    if os == 1:
        screen = relocateScreen()
    while True:
        i = 0
        while i < len(screen):
            print("--------------- Start Process " + str(i+1) + " ---------------")
            process(screen[i])
            i += 1
            print("---------------  End Process " + str(i) + "  ---------------")
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Finish all processes. Continue in " + str(int(delay_all_process/60)) + " minute")
        sleep(delay_all_process)

if __name__ == '__main__':
    main()