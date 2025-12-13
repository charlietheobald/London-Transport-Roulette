import random
import time
def stops(minStops, maxStops):
    stopCount = random.randint(minStops,maxStops)
    print(stopCount,"stops")
    
def direction():
    direction = random.randint(1,2)
    if direction == 1:
        return("Northbound / eastbound")
    elif direction == 2:
        return("Southbound / westbound")
         
time.sleep(1)

def mode(minMode, maxMode):
    mode = random.randint(minMode,maxMode)
    if mode == 1 or mode == 2:
        return("Tube")
    elif mode == 8 or mode == 9:
        return("Overground / Elizabeth line")
    elif mode == 3 or mode == 4:
        return("National Rail")
    elif mode == 5:
        return("Trams / DLR")
    elif mode == 6 or mode == 7:
        print("Bus")
        lower = int(input("Enter lowest bus route number"))
        upper = int(input("Enter highest bus route number"))
        return busSelection(lower, upper)

def busSelection(lower, upper):
    lowerCalc = round(lower-(0.05*lower))
    upperCalc = round(upper+(0.05*upper))
    bussel = random.randint(lowerCalc,upperCalc)
    return(bussel)


# optional Challenges - for advanced users only!
#elif mode == 10:
    #print("Challenge\n")
    #challengeList = ["Insert your challenges here"]
    #challengeNum = random.randint(0,len(challengeList) - 1)
    #print(challengeList[challengeNum])

def main():
    time.sleep(1)
    print(mode(1,9))
    print(direction())
    time.sleep(2)
    (stops(3, 11))
    
main()