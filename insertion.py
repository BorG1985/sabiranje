a = [8,5,6,2,4]
l = len(a) 
for i in range(1,l):
    j = i
    while a[j]<a[j-1] and j>0:
        tmp = a[j]
        a[j] = a[j-1]
        a[j-1] = tmp
        j-=1 
print(a)