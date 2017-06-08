#Multiples
def MultiplesOdd(): #first define a function that does not take any parameters.
    for i in range (1,1001): #run a for loop that goes from 1 to 1,001 so that 1,000 is included.
        if i % 2 == 1: #use an if statement to select only the odd values.
            print i #print the i values that meet the condition of being odd values.
#
MultiplesOdd() #run the function to print the values.

def Multiples5(): #first define a function that does not take any parameters.
    for i in range (5, 1000001): #run a for loop that goes from 1 to 1 million and 1.
        if i % 5 == 0: #use an if statement to test whether the value is divisible by 5.
            print i #if the value meets the condition of being divisible by 5, print the value.

Multiples5() #run the function to print the values.

#Sum List
a = [1, 2, 5, 10, 255, 3]  #first define the variable a to establish the array.
def Sum(array):     #then define a function Sum that takes an array as its parameter.
    sum = 0  #establish a variable for sum so that sum can be calculated as we run through the array.
    for i in range (0,len(array)-1): #create a for loop to iterate through the values of the array.
        sum += a[i]  #update the sum by adding each value of the array to the sum.
    print sum #print the final value of sum.

Sum(a) #run the function to print the final sum value.

#Average List
a = [1, 2, 5, 10, 255, 3]  #first define the variable a to establish the array.
def Avg(array):  #then define a function Avg that takes an array as its parameter.
    sum = 0  #establish a variable for sum so that the sum can be caluclated as we run through the array.
    for i in range (0,len(array)-1): #create a for loop to iterate through the values of the array.
        sum += a[i]  #update the sum by adding each value of the array to the sum.
    print sum/len(array) #print the value of the sum divided by the length of the array to get the average.

Avg(a) #run the function to print the average value.
