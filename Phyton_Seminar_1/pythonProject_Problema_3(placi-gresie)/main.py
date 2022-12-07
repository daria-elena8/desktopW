L1=int(input("lungimea= "))
L2=int(input("latimea= "))
for i in range(L1,1,-1):
    if L1*L2%(i*i)==0:
        print(f"avem nevoie de {L1*L2//(i*i)} placi de gresie cu latura de {i} cm")
        break
