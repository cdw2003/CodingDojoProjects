a = ['magical','unicorns', [1,2,3,4]]
def typelist(input):
    countstr = 0
    totalstr = 'String: '
    countint = 0
    sumint = 0
    if isinstance(input,list):
        for i in input:
            if type(i) == str:
                totalstr = totalstr + " " + i
                countstr += 1
            elif type(i) == int:
                sumint += i
                countint += 1
            elif type(i) == list:
                for x in range(0, len(i)):
                    if type(i[x]) == str:
                        totalstr = totalstr + " " + x
                        countstr += 1
                    elif type(i[x]) == int:
                        sumint += i[x]
                        countint += 1
        if countstr == len(input):
            print "The array you entered is of string type"
            print totalstr
        elif countint == len(input):
            print "The array you entered is of integer type"
            print "Sum: ", sumint
        else:
            print "The array you entered is of mixed type"
            print totalstr
            print "Sum: ", sumint

typelist(a)
