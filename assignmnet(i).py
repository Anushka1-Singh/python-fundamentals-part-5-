#Each write moves the file cursor forward
#After the loop finishes, the cursor is at the end
#Reading starts from the current cursor position
#Cursor is already at the end → nothing left to read because of w
#So even if reading were allowed, it would return empty.

with open("names.txt", "w") as aish:
    for i in range(5):
        aish.write(input("entered by user : ") + '\n')

with open("names.txt", "r") as f:
    # readlines() reads all lines into a list, whereas readline() reads only one line at a time.
    content = f.readlines()
    for name in content:
        print(name, end='')  # keep the '\n' already in the file
#print(names, end=' ')	all names on same line with spaces
#print(names)	each name on its own line, but extra blank lines appear
#print(names, end='')	perfect, one name per line exactly




#QUESTION
# 1) Open "names.txt" in write mode and write 5 names entered by the user
# 1) Open "names.txt" in write mode and write 5 names entered by the user
# 2) Open the same file in read mode and print all names
#content = file.readlines()  , Reads all lines into a list
#print(name, end='')  , end='' prevents extra blank lines
