# TRY AND EXCEPT
try:
    with open("data.txt","r") as f:
        content=f.read()
except FileNotFoundError:
    print("file not found")
else:
    print(content)
finally:
    print("end of program","----")

# write a program that tries to open data.txt in read mode. 
# if the file does nnot exist , catch the exception and print "file not found"



