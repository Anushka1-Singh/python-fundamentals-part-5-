f=open("sample.txt","a")
f.write("\nnew text being appended\n to the file")
f.close()

f=open("sample.txt","r")
content=f.read()
print(content)