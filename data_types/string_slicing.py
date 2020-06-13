#String Slicing

name = "John Citizen"

print (name[0:])
print (name[:7])

print (name[0: 4])

print (name[:])

#Negative Index using slicing

print (name[-1])
print (name[-7: -1])
print (name[-7:])

#String Slicing using Steps
print (name[::2])

#Reverse a string using slicing
print (name[::-1])

#More examples of using string slicing and step

number = "0123456789"

#Print all even numbers

print (number[2::2])

#Print all odd numbers

print (number[1::2])

#Print all odd numbers less than 7

print (number[1:7:2])
