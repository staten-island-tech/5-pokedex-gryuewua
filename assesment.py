def occupied(t,x,y):
    found=0
    for i in range(t):
        if (x[i] == "c" and y[i] == "c"):
            found += 1
    print(found)    

occupied(5,"ccc..","c.cc.")