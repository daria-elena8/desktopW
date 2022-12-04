#Algoritm de criptare prin cifrul lui Cesar

sir=input("Introduceti sirul:\n")
n=int(input("Introduceti numarul de litere la care sa se faca criptarea textului:\n"))
nou=[]
i=0
cod=0
x=0


L = ['A','Ă','Â','B','C','D','E','F','G','H','I','Î','J','K','L','M','N','O','P','Q','R','S','Ș','T','Ț','U','V','W','X','Y','Z']
print(L)


#l=[]
#c=0
#l[1]='ă'
#l[2]='â'
#l[11]='î'
#l[22]='ș'
#l[24]='ț'

##### NU MERGE PT LITERE DECAT INITIALIZAREA MANUALA

#print(l)
for i in range(len(sir)):
    if sir[i].isalpha()!=0:
        if sir[i] in L:
            nou.append(L[(L.index(sir[i])+n)%30])
    else:
        nou.append(sir[i])

afis= "".join(nou)

print(f"Sirul criptat este :\n{afis}")