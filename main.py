
import webbrowser
import colorama
from colorama import Fore, Back, Style
colorama.init()
print("\n" * 100) 

def aik():
   print("---------------------------------------------------------")
def zhasyl_svet(aik):
    print("\033[32m {}" .format(aik))
#Back.BLUE+
def aikhack():
   print("")
   zhasyl_svet("░█████╗░██╗██╗░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗")     
   zhasyl_svet("██╔══██╗██║██║░██╔╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝")
   zhasyl_svet("███████║██║█████═╝░███████║███████║██║░░╚═╝█████═╝░")
   zhasyl_svet("██╔══██║██║██╔═██╗░██╔══██║██╔══██║██║░░██╗██╔═██╗░")
   zhasyl_svet("██║░░██║██║██║░╚██╗██║░░██║██║░░██║╚█████╔╝██║░╚██╗")
   zhasyl_svet("╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
   aik()
   print(Style.RESET_ALL)



q = input("Как открыть новый текстовый редактор? ")

print("\n" * 100)
if q == "nano":
   print("")
   
else:
   print("---------------------")
   print("---КІРУГЕ БОЛМАЙДЫ---")
   print("---------------------")
   exit()

aikhack()
print("1) My YouTube\n--------------\n2) My Instagram\n--------------\n3) My Telegram\n--------------\n4) Exit\n--------------\n5) Время хакинга\n--------------\n")
a=int(input("Выбери цифра! = "))
if a==1:
   webbrowser.open('https://www.youtube.com/channel/UCRRoeUXnd2VOUxK_WTblgeA', new=2)
elif a==2:
   webbrowser.open('https://www.instagram.com/abekenv/', new=2)
elif a==3:
   webbrowser.open('https://t.me/Abeken11', new=2)   
elif a==4:
   exit()
elif a==5:
   pass 
else:
   print("Куасын брат :)")
   exit()
