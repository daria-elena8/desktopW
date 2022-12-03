sir=input("Introduceti cuvintele:\n")
sep=",.?!():;"

for x in sep:
    n=sir.find(x)
    if n!=-1:
        sir=sir[:(n-1)]+" "+sir[n]+" "+sir[(n+1):]
word=sir.split()
print(f"Numarul de cuvinte si semne de punctuatie este {len(word)}\nIar acestea sunt {word}")