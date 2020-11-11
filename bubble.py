a = [8,5,6,2,4]
l = len(a)
while True:
    has_change = False
    for i in range(1,l):
        if a[i] < a[i-1]:
            tmp     = a[i]
            a[i]    = a[i-1]
            a[i-1]  = tmp
            has_change = True
    if not has_change:
        break 
print(a)