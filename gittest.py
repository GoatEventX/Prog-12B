szamok=[]

for i in range(5):
    szamok.append(int(input("adja meg egy számot: ")))
atlag=0.0
for i in range(len(szamok)):
    atlag += szamok[i]
print(f"Átlag: {atlag/len(szamok)}")