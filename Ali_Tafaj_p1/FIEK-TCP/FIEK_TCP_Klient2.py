
import socket


print(" - MIRSEVINI - TCP client".center(30, ' ')+"\n")
serverName = input("Vendosni emrin e serverit ose klikoni \"enter\" per vlere te nenkuptuar: ")
if (serverName == ''):
    serverName = 'localhost'
serverPort = input("Vendosni portin e serverit ose klikoni \"enter\" per vlere te nenkuptuar: ")
if (serverPort == ''):
    serverPort = 13000
else:
    try:
        serverPort = int(serverPort)
    except:
        print("Vlera e portit nuk eshte valide!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((serverName, serverPort))
    print("Shtypni \"perfundo\" per ta mbyllur\n")
    while True:
        request = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE,"
                        +"PALINDROME, TIME, GAME, GFC, CONVERT, BMI, CONSUMPTION): ")
        if (request == "perfundo"):
            break
        elif (len(request.encode()) > 128):
            print("Kerkesa nuk mund te jete me te madhe se 128 bytes")
            continue
        elif (request == ""):
            continue
       # s.sendall(str.encode(request))
        s.send(request.encode("ASCII"))
        response = s.recv(128).decode("ASCII") #("UTF-8")
        print('Pergjigja: ', response)#repr(response)
except:
    print ("Nuk jeni lidhur me serverin!")
s.close()

