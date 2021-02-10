def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)

writeFile("test1.txt", "written by File IO")
s = readFile("test1.txt")
print(s)