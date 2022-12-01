sir= input("Sirul de caractere este :\n")
subs= input("\nSubsirul care trebuie cautat este: \n")
nrap= 0
i=0
while i < len(sir):

          if sir.find(subs, i) !=ValueError:
              nrap=nrap+1
              m=sir.find(subs, i)
              i=m+len(subs)
          else:
               break

print(f"Numarul de aparitii al subsirului {subs} in sirul {sir} este: {nrap}\n")
