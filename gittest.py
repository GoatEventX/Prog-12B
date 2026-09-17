szamok=[]

for i in range(5):
    szamok.append(int(input("adja meg egy számot: ")))
atlag=0.0
for i in range(len(szamok)):
    atlag += szamok[i]
print(f"Átlag: {atlag/len(szamok)}")
i=0
while i < len(szamok) and szamok[i]%2 != 0:
    i += 1
if i < len(szamok):
    print("Van páros fasz szopó")
else:
    print("Nincs páros cigány")
