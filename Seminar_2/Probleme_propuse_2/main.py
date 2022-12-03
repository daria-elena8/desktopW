str= input("Introduceti sirul:\n")

sep=" ,.?!/();:"
for x in sep:
    str=str.replace(x, " ")
word=str.split()
i=0
mul=set()

for i in range(len(word)):
    if word[i] not in mul:
        mul.add(word[i])
print(f"Numarul de cuvinte distincte este {len(mul)}\n")
print(f"Cuvintele distincte sunt {mul}")