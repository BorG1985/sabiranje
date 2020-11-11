start = [-1,-1] 

#Your code here

letters = ['A','B','C','D','E','F','G','H']
for y in range(8):
    print(y+1,end=" ")
    for x in range(8):
        chr = "O"
        if [x+1,y+1] == start:
            chr = "S"
        print(chr,end="")
    print()
print(end="  ")
for l in letters:
    print(l,end="")
print()