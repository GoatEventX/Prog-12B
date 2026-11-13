# IMPORT
from colorama import Fore, Back, Style
import subprocess

# GLOBÁLIS VÁLTOZÓK

menu_elemek = [
    [11,"Whiskey(non-alcoholic)", 10000],
    [12,"Vodka(non-alcoholic)", 15500],
    [13,"Hubertus(non-alcoholic)", 4700],
    [14,"Baileys Chocolate(Extra-alcoholic)", 100],
    [15,"Nuka-Cola",2700],
    [31,"Merci", 4550],
    [32,"Milka", 450],
    [33,"Dörmi", 550],


]

# FÜGGVÉNY DEFINICIOK
def menu():
    subprocess.run(["cls"], shell=True)
    print(f"{Fore.RED}Válassz menüt{Fore.RESET}")
    print(f"{"=" * 40}")
    for m in menu_elemek:
            print(f"[{m[0]}]{m[1]:40} ({m[2]:>6} Ft)")
def visszajaro(v):
    vissza=0
    ezer=0
    otszaz=0
    ketszaz=0
    szaz=0 
    otven=0
    ezres="ezres"
    otszazas="ötszázas"
    ketszazas="kétszázas"
    szazas="százas"
    otvenes="ötvenes"
    osszvissza=0
    for i in range(len(menu_elemek)):
        if menu_elemek[i][0]==v:
            vissza=penz-menu_elemek[i][2]
    while vissza/1000 >= 1:
        ezer+=1
        vissza=vissza-1000
    while vissza/500 >= 1:
        otszaz+=1
        vissza=vissza-500
    while vissza/200 >= 1:
        ketszaz+=1
        vissza=vissza-200
    while vissza/100 >= 1:
        szaz+=1
        vissza=vissza-100
    while vissza/50 >= 1:
        otven+=1
        vissza=vissza-50
    
    osszvissza=1000*ezer+500*otszaz+200*ketszaz+100*szaz+50*otven
    
    return ezer,ezres,otszaz,otszazas,ketszaz,ketszazas,szaz,szazas,otven,otvenes,osszvissza

def kiadtermek(v):
    termek=""
    for i in range(len(menu_elemek)):
        if menu_elemek[i][0]==v:
            termek=menu_elemek[i][1]
    return termek
def vanepenz(p,v):
    Nincs=True
    for i in range(len(menu_elemek)):
        if menu_elemek[i][0]==v:
            if menu_elemek[i][2] > p:
                Nincs=False
    return Nincs
# ---------------------
"""
print("Csak Ezeket a Kp bankjegyeket fogadjuk el: 1000,500,200,100,50")
termek=input("Nyomd Be a számot Vagy nyomja K a kilépésig")
"""

# Program
menu()

while True:

    menu()
    penz=int(input("A pénzt tegye be: "))
    valasz = int(input("Mit Szeretnél?: "))
    if valasz == 11:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 12:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 13:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 14:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 15:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 31:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 32:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == 33:
        if vanepenz(penz,valasz) == True:
            print(f"{visszajaro(valasz)}FT a visszajáró Tessék itt a {kiadtermek(valasz)}")
        else:
            print("Nincs elég pénze")
        input("Üss egy billentyűt a folytatáshoz...")