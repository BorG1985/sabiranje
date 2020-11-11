a = [8,5,6,2,4]
l = len(a)
for i in range(l):
    min = i
    for j in range(i,l):
        if a[j] < a[min]:
            min = j
    tmp = a[i]
    a[i] = a[min]
    a[min] = tmp
print(a)