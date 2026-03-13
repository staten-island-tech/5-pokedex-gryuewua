'Assessment: Parking spaces'

""" def occupied(t,x,y):
    found=0
    for i in range(t):
        if (x[i] == "c" and y[i] == "c"):
            found += 1
    print(found)    

occupied(5,"c....","c.cc.") """

'Assessment: Language'

""" def language(x):
    s=0
    t=0
    for i in x:
        if (i == "s" or i == "S"):
            s += 1
        if (i == "t" or i == "T"):
            t += 1
    if t > s:
        print("(probably)English")
    else:
        print("(probably)French")

language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.") """

'Assessment: Magnus'

""" def honi(x):
    found=0
    y=0
    H=1
    O=2
    N=3
    for i in x:
        if (i == "H"):
            y = 1
        if y == H:
            if (i == "O"):
                H += 1
        if H == O:
            if (i == "N"):
                O += 1
        if O == N:        
            if (i == "I"):
                found+=1
                y=0
                H=1
                O=2
                N=3
                
    print(found)

honi('UAOSIDIOUAWIOUADWHWAOIDUWAOIDUNIFHOLYBUMBRONIHHHHOOOOLLLLYYYBUUUUMMMNIIII') """

'Assessment: Gambling'

def slots (quarters, m1, m2, m3):
    plays = 0
    m = 1
    while quarters > 0:
        if m == 1 and quarters > 0:
            quarters -= 1
            m1 += 1
            plays += 1
            m = 2
            if m1 == 35:
                quarters += 30
                m1 = 0
        if m == 2 and quarters > 0:
            quarters -= 1
            m2 += 1 
            plays += 1
            m = 3
            if m2 == 100:
                quarters += 60
                m2 = 0
        if m == 3 and quarters > 0:
            quarters -= 1
            m3 += 1
            plays += 1
            m = 1
            if m3 == 10:
                quarters += 9 
                m3 = 0 
    else:
        print (f"Martha plays {plays} times before going broke.")

slots (48, 3, 10, 4)