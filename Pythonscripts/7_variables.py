'''
A python variable is a reserved memory location to store values. A variable is created the moment you first assign a value to it
'''

p = 30

'''
id() function returns the "identity" of the object .
the identity of an object - Is an integer
                          - Guaranteed to be unique
                          - Constant for this object during its lifetime
'''
print(id(p))

# Example 2 : memory address of the variable

print(hex(id(p)))

# Example 2

p = 20
q = 20  # Create new reference q which will point to value 20. p & q will be pointing to same memory location.
r = q

print(p,type(p),id(p),hex(id(p))) # Creates an integer object with value 20 and assigns the variable p to

print(q,type(q), id(p),hex(id(q)))

print(r,type(r),id(p),hex(id(r)))

# Example 3 : Variable Overwriting

x = 10
x = x+20
print(x)

# Example 4 : Variable Assignment

intvar = 10 # Integer variable
floatvar = 2.57 # Float variable
strvar = "Python Language" # string variable

print(intvar)
print(floatvar)
print(strvar)

# Example 5 :  Multiple Assignments

intvar,floatvar,strvar = 100, 3.57, "python language"
print(intvar,floatvar,strvar)

# Example 6 : All variables pointing to the same value
p1=p2=p3=p4 =44
print(p1,p2,p3,p4)