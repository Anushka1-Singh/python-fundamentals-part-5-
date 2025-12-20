# word search "python" in txt file

data=True
line=1
word="python"
with open("practice problem/sample1.txt","r") as f:
    while data:
        data=f.readline()
        if word in data:
            print(f"word found at line {line}")
            print(word)
            break
            
        line +=1
        
