sir=input("Va rog sa introduceti titlul: \n")

punctuatie= " ,.?!/*-()$%&"

for x in punctuatie:
    sir=sir.replace(x," ")

exc= ["a", "an", "by", "on", "in", "at", "to", "for", "ago", "the", "past", "over", "into","onto"]


new=[]
sir=sir.lower()
cuv=sir.split()
i=1

for i in range(len(cuv)-1):
    if len(cuv[i])>=5:
        cuv[i]=cuv[i].title()
    elif cuv[i] not in exc:
        cuv[i]=cuv[i].title()
    new.append(cuv[i])
new.append(cuv[len(cuv)-1].title())
sir=" ".join(new)
print(sir)