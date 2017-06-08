#Part 1
def draw_stars(arr):
    for i in range(0, len(arr)):
        for j in range(0,arr[i]):
            print "*",
        print "\t"

draw_stars()

#Part 2
def draw_stars(arr):
    for i in range(0, len(arr)):
        if type(arr[i]) == int:
            for j in range(0,arr[i]):
                print "*",
            print "\t"
        elif type(arr[i]) == str:
            for x in range(0,len(arr[i])):
                print arr[i][0].lower(),
            print "\t"

draw_stars()
