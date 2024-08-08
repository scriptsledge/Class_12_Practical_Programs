file1 = open("myfile.txt","r",encoding='utf-8')
lines = file1.readlines()

count = 1
for line in lines:
    print("Line{} : {}".format(count, line.strip()))
    count += 1
