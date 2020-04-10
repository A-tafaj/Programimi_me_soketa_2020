#import socket
from socket import *
from datetime import*
from _thread import *
from runpy import *
import math
import random
from random import randint

def IPADDRESS():
    return "Ip adresa juaj eshte %s" % addr[0]

def PORT():
    return "Porti qe perdor klienti eshte: %s" % addr[1]

def COUNT(request):
    zanore = ['A', 'E', 'I', 'U', 'O']
    bashketinglloret = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    numroZ = 0
    numroB = 0
    message = str(request[1:]).upper()
    for i in range (0, len(message)):
        if(message[i] in zanore):
            numroZ += 1
    for i in range (0, len(message)):
        if(message[i] in bashketinglloret):
            numroB += 1
    return "Zanore: "+str(numroZ)+", bashketingellore: "+ str(numroB)

def PALINDROME(request):
    return request == request[::-1]


def REVERSE(teksti):
    whs=teksti.strip()
    gjatesia=len(whs)
    prapthi=whs[gjatesia::-1]
    return prapthi

def TIME():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def GAME():
    return str(random.sample(range(0, 35), 5))

def GCF(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        return "Argumentet e dhena nuk jane numra te plote"
    return str(math.gcd(num1, num2))

def Consumption(km, literPerkm, cmimi):
    try:
        km=float(km)
        literPerkm=float(literPerkm)
        cmimi=float(cmimi)
    except:
        return "Argumentet e dhena nuk jane numra"
    return "Udhetimi do ju kushtoje: "+str(((literPerkm/100)*km)*cmimi)+"euro"

def BMI(masa,gjatesia):
    try:
        masa = float(masa)
        gjatesia = float(gjatesia)
    except:
        return "Argumentet e dhena nuk jane numra"
    gjatesiaCm = (gjatesia/100)
    bmi = masa/(gjatesiaCm**2)
    if ( bmi < 16):
        return("Nenpeshe jasht mase!")
    elif ( bmi >= 16 and bmi < 18.5):
        return("Nenpeshe")
 
    elif ( bmi >= 18.5 and bmi < 25):
        return("Shendetshem")
 
    elif ( bmi >= 25 and bmi < 30):
        return("Mbipeshe")
 
    elif ( bmi >=30):
        return("Mbipeshe jasht mase!")


def CONVERT(tipi, numri):
    try:
        numri = float(numri)
        if (numri < 0):
            return "Nuk pranohen vlera negative"
        if (tipi == "cmToFeet"):
            return numri/30.48
        elif (tipi == "FeetToCm"):
            return numri*30.48
        elif (tipi == "kmToMiles"):
            return numri/1.609
        elif (tipi == "MileToKm"):
            return numri*1.609
        else:
            return "Konvertimi i kerkuar nuk ekziston"
    except ValueError:
        return ("Nuk eshte numer!")


def Kerkesat(data, conn):
    try:
        request = data.split()
        response = ""
        if request[0] == "IPADDRESS":
            response = IPADDRESS()
        elif request[0] == "PORT":
            response = PORT()
        elif request[0] == "COUNT": 
            response = COUNT(request)
        elif request[0] == "PALINDROME":
            response = str(PALINDROME(request[1]))
        elif request[0] == "REVERSE":
            response = str(REVERSE(request[1]))
        elif request[0] == "TIME":
            response = TIME()
        elif request[0] == "GAME":
            response = GAME()
        elif request[0] == "GCF":
            response = GCF(request[1], request[2])
        elif request[0] == "BMI":
            response = BMI(request[1], request[2])
        elif request[0] == "CONSUMPTION":
            response = Consumption(request[1], request[2], request[3])
        elif request[0] == "CONVERT":
            response = str(CONVERT(request[1], request[2]))
        else:
            response = "Keni dhene kerkese jo valide"
        conn.sendall(str.encode(response))
    except:
        response = "Perseritni kerkesen, kem hasur ne gabim"
        conn.sendall(str.encode(response))
    
def client_thread(conn):
    while True:
        data = conn.recv(128).decode()
        if not data:
            break
        Kerkesat(data, conn)
    conn.close()

host = 'localhost'
port = 13000
s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))
s.listen(5)
print("-Serveri ka startuar dhe eshte duke pritur kerkesat-")

while True:
    conn, addr = s.accept()
    print("Lidhur me " + addr[0] + ":" + str(addr[1])) 
    start_new_thread(client_thread, (conn,))

s.close()

