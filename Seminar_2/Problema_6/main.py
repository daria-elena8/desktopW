sir=input("Va rog introduceti textul:\n")
sep=",!#*()?"
for x in sep:
    sir=sir.replace(x, " ")
word=sir.split()
i=0
nr1=0
nr2=0
print(word)
sum=0.0
while i<len(word)-1:
    if word[i].isalpha()==0:
        print(word[i])
        if nr1==0:
            nr1=float(word[i])
        else:
            nr2 =float(word[i])
            sum=sum+ (nr1*nr2)
            nr1=0.0
    i=i+1
print(f"Suma totala a cheltuielilor este {sum} lei")