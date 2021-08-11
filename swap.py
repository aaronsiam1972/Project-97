def swapfiles():
    varA = open("text1.txt", "r")
    varB = open("text2.txt", "r")
    
    a = varA.read()
    b = varB.read() 

    with open(a, "w") as x:
        x.write(b)

    with open(b, "w") as y:
        y.write(a)


swapfiles()