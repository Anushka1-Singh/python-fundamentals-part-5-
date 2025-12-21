# Append a new log
with open("log.txt", "a") as f:
    f.write("program run successfully\n")  # ensures newline after each log

# Read and print all logs
with open("log.txt", "r") as f1:
    content = f1.read()
    print(content)

#QUESTION
#create a program that
#1)opens a file log.txt in append mode
#2)adds a new log entry ("like program run successfully")
#3)opens the file in read mode and prints all logs
