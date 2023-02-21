dirs = ["o1", "o2"]

for i in dirs:
    for j in range(1,2):
        with open(i+"/"+str(j)) as f:
            for line in f:
                print(line)
                break