#Add values to the string dynamically

str = "Employee Name: %s, Employee Age: %d, Employee Salary: %f" % ("John", 30, 10.5)
print (str)

#Tweak the floting point

str = "Employee Name: %s, Employee Age: %d, Employee Salary: %.f" % ("John", 30, 10.5)
print (str)

str = "Employee Name: %s, Employee Age: %d, Employee Salary: %.2f" % ("John", 30, 10.5)
print (str)

#Declare the string using {}

str = "Employee Name: {}, Employee Age: {}, Employee Salary: {}".format("John", 30, 10.5)
print (str)

str = "Employee Name: i{0}, Employee Age: {1}, Employee Salary: {2}".format("John", 30, 10.5)
print (str)

str = "Employee Name: i{0}, Employee Age: {2}, Employee Salary: {1}".format("John", 10.5, 30)
print (str)
