'Assessment parking spaces'

'''def occupied(t,x,y):
    found=0
    for i in range(t):
        if (x[i] == "c" and y[i] == "c"):
            found += 1
    print(found)    

occupied(5,"c....","c.cc.")'''

'Assessment language'

def language(x):
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

language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")