word = input("Enter word: ")
j = len(word)-1
k = 0
isPalindrome = True
while k<j:
    if word[k]!=word[j]:
        isPalindrome = False
        break
    k+=1
    j-=1 
print("Reč " + word + " " + ("je" if isPalindrome else "nije") + " palindrom")