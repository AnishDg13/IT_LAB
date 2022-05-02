text=input("Enter words:")
text2='' + text
words=text.split()
words.sort()
print('Output of sort() method:\n')
for word in words:
    print(word)

words2=text2.split()

for i in range (len(words2)-1):
    for j in range (len(words2) -1 -i):
        if (words2[j]>words2[j+1]):
            temp=words2[j]
            words2[j]=words2[j+1]
            words2[j+1]=temp

print('Output of Bubble Sort:')

for word in words2:
    print(word)