list1 = [10, 12, 15]
print(min(list1))
print(max(list1))

#Max and min doesn't work with lists with strings as items within it.

#Add an item to the list using append method
list1.append(20)
print(list1)

# Del method to delete

del list1[3]
print(list1)

#Pop method to remove an element
list1.pop(0)
print(list1)

#Remove method to remove an element
list1.remove(15)
print(list1)

#Insert method
list1.insert(1, "Debasis")
print(list1)

#Extentend method to join to lists
list2 = [12, 13, 19]
list3 = [20, 22, 25]

list2.extend(list3)
print(list2)

#Index method
print(list2.index(19))

# Count Method (for multiple duplicate items in the list)
list2.append(12)
print(list2.count(12))

# Sort and reverse method to sort
list4 = [4, 7, 2, 11, 9, 99]
print(list4)
list4.sort()
print(list4)
list4.reverse()
print(list4)

print(sorted(list4))
print(sorted(list4, reverse = True))