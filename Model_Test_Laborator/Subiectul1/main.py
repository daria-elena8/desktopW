doc=[]
x=[]
l=[]
def citire_numere(f):
    line=f.readline()
    while line!="":
          x=line.strip().split(" ")
          l=[]
          for elem in x:
               l.append(int(elem))
          doc.append(l)
          line=f.readline()
    f.close()

def prelucrare_lista(doc):
    m=len(doc[0])
    for line in doc:
        mini = 1000
        for elem in line:
            if elem<mini:
                mini=elem
        while mini in line:
            try:
               line.remove(mini)
            except ValueError:
               break
        if len(line)<m:
            m=len(line)
    for x in range(len(doc)):
        line=[]
        line=doc[x]
        line=line[:m]
        doc[x]=line

f=open("numere.in", "r")
citire_numere(f)
print(doc)

d=[]
k=int(input("k="))
for line in doc:
    for elem in line:
        if k==len(str(elem)):
            if elem not in d:
                d.append(elem)
d.sort(reverse=True)
print(d)

prelucrare_lista(doc)
for line in doc:
    print(*line)
