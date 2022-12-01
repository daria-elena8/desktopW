cuv= input("Va rog introduceti cuvantul pentru care trebuie sa gasim rima:\n")
p=int(input("\nIntroduceti numarul de litere la care trebui sa rimeze:\n"))
sir=input("\n In final, va rog introduceti cuvintele: \n")
i=0
s=cuv[-p: ]
word=sir.split(" ")
for i in range(len(word)):
    if word[i].endswith(s) ==0:
        word[i]=-1

print(f"\ncuvintele care au acelasi sufix cu {cuv} sunt: \n")
i=0
for i in range(len(word)):
    if word[i]!=-1:
        print(word[i])