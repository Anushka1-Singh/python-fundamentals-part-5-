try:
    with open("data.txt", "r") as f:
        content = f.read()
        if content == "":
            raise ValueError("empty file")
except (FileNotFoundError, ValueError):
    content = "hi everything is gonna alright, just take care of yourself"
    with open("data.txt", "w") as f:
        f.write(content)
    print("file created or updated")
finally:
    print("text typed in data.txt ----")
print(content)
