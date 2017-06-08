a = [1,2,5,6,2]
b = [1,2,5,6,2]
c = [1,2,5,6,5]
d = [1,2,5,6,5,3]
e = [1,2,5,6,5,16]
f = [1,2,5,6,5]
g = ['celery','carrots','bread','milk']
h = ['celery','carrots','bread','cream']

def compareArrays(array1,array2):
    countdiff = 0
    if len(array1) == len(array2):
        for i in range (0, len(array1)):
            if array1[i] != array2[i]:
                countdiff += 1
        if countdiff > 0:
            print "The lists are not the same."
        else:
            print "The lists are the same."
    else:
        print "The lists are not the same."

compareArrays(g,h)
