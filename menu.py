# IMPORT
from colorama import Fore, Back, Style
import subprocess

# GLOBÁLIS VÁLTOZÓK

menu_elemek = [
    ["A) Big Mac", 0, 2000],
    ["B) Chicken MCnuggets (9db)", 0, 2230 ],
    ["C) Big Tasty Pesto Rosso", 0, 4120],
    ["D) Big Tasty", 0, 3840],
    ["X) Végeztem", 0, 0],
]


# FÜGGVÉNY DEFINICIOK
def menu():
    subprocess.run(["cls"], shell=True)
    print(f"{Fore.RED}Válassz menüt{Fore.RESET}")
    print(f"{"=" * 40}")
    for m in menu_elemek:
        if m[0].startswith("X"):
            print(f"{m[0]}")
        else:
            print(f"{m[0]:25} ({m[2]:>6} Ft)")


def rendeles(mit, db):
    i = 0
    while not menu_elemek[i][0].startswith(mit):
        i += 1
    menu_elemek[i][1] += db


def szamla():
    print(f"{'='*15}\n{'SZÁMLA':^15}\n{'='*15}\n")
    total = 0
    for i in range(len(menu_elemek) - 1):
        # print kajanev , reszosszeg mennyiseg
        if menu_elemek[i][1]>0:
            print(F"{menu_elemek[i]} Részösszeg {menu_elemek[i][1]*menu_elemek[i][2]}")
            total += menu_elemek[i][2]*menu_elemek[i][1]
    print(f"FIZETENDŐ ÖSSZEG: {total}Ft")


# ---------------------

# KOMMUNISTA PROGRAM


# Program
menu()

valasz = input("Mit Szeretnél?: ").strip().upper()
if valasz == "A":
    db = int(input("Mennyit kér?: "))
    rendeles("A", db)
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "B":
    db = int(input("Mennyit kér?: "))
    rendeles("B", db)
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "C":
    db = int(input("Mennyit kér?: "))
    rendeles("C", db)
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "D":
    db = int(input("Mennyit kér?: "))
    rendeles("D", db)
    input("Üss egy billentyűt a folytatáshoz...")
elif valasz == "X":
    print("Jó szar étvágyat")
    szamla()
    exit()

while True:
    menu()

    valasz = input("Mit Szeretnél?: ").strip().upper()
    if valasz == "A":
        db = int(input("Mennyit kér?: "))
        rendeles("A", db)
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "B":
        db = int(input("Mennyit kér?: "))
        rendeles("B", db)
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "C":
        db = int(input("Mennyit kér?: "))
        rendeles("C", db)
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "D":
        db = int(input("Mennyit kér?: "))
        rendeles("D", db)
        input("Üss egy billentyűt a folytatáshoz...")
    elif valasz == "X":
        print("Jó szar étvágyat")
        szamla()
        exit()
