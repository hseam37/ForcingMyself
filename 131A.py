
'''
Author: hasan.seam
https://codeforces.com/problemset/problem/131/A
'''

word = str(input())
newWord = ''
if(len(word)==1 and word[0].islower()):
    newWord =  word.upper()
elif(word.isupper()):
    newWord = word.lower()
elif(word[1:].isupper()):
    newWord += word[0].upper()
    newWord += word[1:].lower()
else:
    newWord = word

print(newWord)


