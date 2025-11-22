# kicsi vibe coding
import time 
import colorama
from colorama import Fore,Back,Style
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ","'",'"',"?","!"]
szo = []
def get_info():
     kerdes = input("Enter your word: ")
     return kerdes

kerdes = get_info()

def text(text=kerdes):
     calc = 0
     betuk = ""
     space = " "
     hossz = len(text)
     for i in range(0,hossz):
          for i,n in enumerate(abc):
               szo.append(n)
               print(space,"".join(szo),flush=True)
               print(Fore.CYAN + (hossz+4)*"-")
               time.sleep(0.05)
               if n == text[calc]:
                    calc+=1
                    betuk+=n
                    break
               elif n.capitalize() == text[calc]:
                    calc+=1
                    betuk+=n.capitalize()
                    break
               else:
                    szo.clear()
                    szo.extend(betuk)
                    continue
     print()
     qstn = input("press enter to exit ")

text()

