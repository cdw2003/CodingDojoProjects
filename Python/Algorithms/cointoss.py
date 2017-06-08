import random
def cointoss():
    numheads = 0
    numtails = 0
    for i in range(1, 30):
        random_num = random.random()
        rounded = round(random_num)
        if rounded == 1:
            numheads += 1
            print "Attempt #{}:".format(i), "Throwing a coin...It's a head!...Got {} head(s) so far".format(numheads), "and {} tail(s) so far.".format(numtails)
        elif rounded == 0:
            numtails += 1
            print "Attempt #{}:".format(i), "Throwing a coin...It's a head!...Got {} head(s) so far".format(numheads), "and {} tail(s) so far.".format(numtails)

cointoss()
