name = "John Citizen"

#Print first character using index
print (name[0])

#Print last character using negative index
print (name[-1])

#Print the length of the string using len()
print(len(name))

#string.index method
print(name.index("n"))

#string.count method
print(name.count("n"))

#string.find method
print(name.find("hn"))

#Convert to lower using lower()
print(name.lower())

#Convert to upper using upper()
print(name.upper())

#startswith and endswith example
print(name.startswith("J"))
print(name.endswith("z"))

#Strip Method example
name1 = "   John Citizen   "
name2 = "$$$John Citizen$$$"
print(name1.strip())
print(name2.strip("$"))

#Replace Method Example
print(name1.replace(" ",""))

#Split Method Example
companies = "Amazon,Google,Microsoft"
print(companies.split(","))
#Now let's get the first element
print(companies.split(",")[0])

#Join Method Example
print("_".join(name))
