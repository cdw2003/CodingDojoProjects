array1 = ["Cheryl", "Ricky", "Melanie", "Sunil", "Bonnie", "Alice"]
array2 = [2,5,7,3,5,6,7,0,20]

puts array1.at(2)

puts array2.fetch(5)

array1.delete("Alice")
puts array1

puts array2.reverse

puts array1.length

puts array2.sort
puts array2.sort.reverse

puts array1.slice!(1)
puts array1

puts array2.shuffle.join(",")

puts array1.insert(1, "Nathan")

puts array2.values_at(0,8).join("of")
