import random

x=int(input("Unesite broj izmedju 1 i 10 : "))
print("Vaš broj je :", x)
y=random.randint(1,10)
print("CPU broj je : ", y)
print(y)
if x==y :
    print("pogodili te, cestitamo!")
else:
    print("Vise srece drugi put")
