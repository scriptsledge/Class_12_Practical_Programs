file1 = open("file1.txt")
file2 = open("file2.txt","w")
for line in file1:
    print(file1.read())
    if "a" in line:
        line = line.replace("a", " ")
    else:
        file2.write(line)
file1.close()
file2.close()