#Odd Even
def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print "Number is {}.".format(i), "This is an even number."
        elif i % 2 == 1:
            print "Number is {}.".format(i), "This is is an odd number."

odd_even()

#Multiply
a = [2,4,10,16]
def multiply(arr, num):
    for i in range(0, len(arr)):
        arr[i] = arr[i]*num
    return arr

multiply(a,5)

#Hacker Challenge
def layered_multiples(arr):
    new_array = []
    for i in arr:
        countarr=[]
        for x in range(0,i):
            countarr.append(1)
        new_array.append(countarr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
