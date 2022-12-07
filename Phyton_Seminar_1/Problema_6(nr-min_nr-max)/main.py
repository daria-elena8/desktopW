n=int(input("n= "))
lcif=n%10

new=n%10
n=n//10
p=1
mini=n
while n:
    if int(n%10)>lcif:
        new = new + p * (n % 10)
    else:
         new=new*10+int(n%10)
    lcif=n%10
    n=n//10
    p=p*10
    if n<10:
        n=new
        if new>=mini:
            n=0


print(f"valoarea noua a numarului este {mini}")
