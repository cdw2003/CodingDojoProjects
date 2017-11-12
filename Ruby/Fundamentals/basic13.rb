# Print 1-255
for i in 1..255
  puts i
end

# Print odd between 1-255
(1..255).each { |i| puts i if i.odd? }

# Print sum
sum = 0
for i in 1..255
  sum = sum + i
end
puts sum

#Iterating through an array
my_array = [1,3,6,7,9]
my_array.each {|item| puts item}

#Find Max
def max(arr)
  puts arr.max_by {|number| number}
end
max([1,3,2,7,12])

#Get average
def average(arr)
  sum = 0
  for i in arr
    sum = sum + i
  end
  puts sum/arr.length
end
average([1,4,5,2,8])

#Array with odd numbers
y = []
(1..255).each { |i| y << i if i.odd? }
puts y

#Greater than Y
def greaterY(arr, y)
  puts arr.count { |elem| elem > y }
end
greaterY([1,5,4,7,8], 5)

#Square the values
arr = [1, 5, 10, -2]
puts arr.map! { |elem| elem * elem }

#Eliminate negative numbers
arr = [1,5,10,-2]
puts arr.each_index { |index| arr[index] = 0 if arr[index] < 0 }

#Max, min, average
arr = [1, 5, 10, -2]
sum = 0
for i in arr
  sum = sum + i
end
puts arr.max
puts arr.min
puts sum/arr.length

#Shift the values
arr = [1, 5, 10, 7, -2]
arr.rotate!(1)
arr[arr.length-1] = 0
puts arr

#Number to string
arr = [-1, -3, 2]
puts arr.each_index { |index| arr[index] = "Dojo" if arr[index] < 0 }
