def fooBar():
    countmult = 0
    countsquare = 0
    for i in range(100,100001):
        for x in range(2,i):
            if i % x == 0:
                countmult +=1
            if i - (x*x) == 0:
                countsquare +=1
        if countmult == 0:
            print "Foo"
            countmult = 0
        if countsquare == 1:
            print "Bar"
            countsquare = 0
        if countmult != 0 and countsquare == 0:
            print "FooBar"

fooBar()
