sir=input("Introduceti cuvintele, apoi apasati ENTER: \n")
new=[]
maxi=0
separatori= ",.!?"
for x in separatori:
    sir=sir.replace(x, " ")

word=sir.split()
for i in range(len(word)):
    if len(word[i])>maxi:
        maxi=len(word[i])
        new=[]
    elif (len(word[i])==maxi) & (word[i] not in new):
           new.append(word[i])
print(f"Cel mai lung cuvant din sir are lungimea {maxi}, iar cuvintele din sir cu aceasta lungime sunt:\n")
i=0
while i<len(new):
    print(new[i])
    i=i+1
