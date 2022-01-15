def swapFileData():
    file1="text.txt"
    file2="essay.txt"
    with open(file1, 'r') as a:
        data_a=a.read()
    with open(file2, 'r') as b:
        data_b=b.read()
    with open(file2, 'w') as b:
        b.write(data_a)
    with open(file1, 'w') as a:
        a.write(data_b)
swapFileData()