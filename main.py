# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#               ------CITIREA UNUI TABLOU UNIDIMENSIONAL------
#                              varianta (1)
   ###############################################################
#m=int(input("numarul de linii= \n"))
#n=int(input("numarul de coloane= \n"))

                                #########
#T=[[0 for x in range(n)] for y in range(m)]

#for i in range(m):
#    for j in range(n):
#       T[i][j] = int(input(f"T[{i}][{j}]= "))

#for linie in T:
#    for elem in linie:
#       print(elem, end=" ")
#    print()
    ##############################################################

#                            varianta (2)

T=[]
while True:
    linie=input(f"Elementele de pe linia {len(T)} sunt: ")
    if len(linie)!=0:
        T.append([int(x) for x in linie.split()])
    else:
        break
for linie in T:
    for elem in linie:
        print(elem, end=" ")
    print()