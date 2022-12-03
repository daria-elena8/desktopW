cuv= input("Introduceti cuvantul de baza:\n")
n=int(input("Introduceti numarul de cuvinte:\n"))
sir=input("Introduceti cuvintele:\n")

word=sir.split()
i=0
for i in range(len(word)):
    if len(word[i])==len(cuv):
        print(word[i])
