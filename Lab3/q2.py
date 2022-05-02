
f1=open("file1.txt","r")
f2=open("file2.txt","w")
content =""
for char in f1:
    content=content+char

content=content[::-1]

for i in content:
    f2.write(i)