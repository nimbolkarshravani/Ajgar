###  जादूगर 	

कम  = 1
ज्elifदा  = 1000

print(" १  से  १००० के बीच कोई भी एक संख्या दीजिए . मई आपका मन पढ़कर वो संख्या बताऊँगा , बस १० सवालों मई ")

## ये सवाल नो है 
सवाल_नो  = 1
while  कम  < ज्elifदा :
    print (कम ,ज्elifदा )
    ## you will realise that you need the "+1" below...
    बीच  = (कम  + ज्elifदा )//2 + 1
    परिणाम  = input("%d: क्या आपकी संख्या  %d से कम हु (y/n)?" % (सवाल_नो , बीच ))
    if  परिणाम.lower()[0] == 'y':
        ज्elifदा  = बीच  -1
    else :
        कम  = बीच 
    सवाल_नो = सवाल_नो + 1

print ("आपकी संख्या है :", कम)
    