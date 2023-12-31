'''
3.Strings
    3.1. String Indexing,
    3.2. String Slicing,
    3.3. Update & Delete String,
    3.4. String Concatenation ,
    3.5. Iterating through a String
    3.6. String Membership
    3.7. String Partitioning
    3.8. Sting Functions
    3.9. Using Escape Character'''


# Define string using single quotes
mystr = 'Hello World'
print(mystr)

# string creation using double quotes
str1 = "Hello Python"
print(str1)

# Define string using triple quotes
mystr1 = '''Hello
World , Data Engineering '''

print(mystr1)

## example
mystr2 = """ Hi Everyone
Welcome to Data Engineering Course"""

print(mystr2)

# example 2
strvar = ('Happy ''Monday ''Everyone ')
print(strvar)

# example 3
newstr = 'Hello '
newstr = newstr*5
print(newstr)

# Length of string
print(len(newstr))

# 3.1. String Indexing
    #3.1.1. Forward Indexing
    #3.1.2. Backward Indexing

indstr = 'Data Engineering'
print(indstr)

print(indstr[0]) # First Character in string
print(indstr[len(indstr)-1]) # Last character in string
print(indstr[-1]) # Last character in string
print(indstr[6]) # Fetach 7th element of the string
print(indstr[4]) # it treats spaces also a element

# 3.2. String Slicing

strslice = 'Data Engineering World'

print(strslice[0:5]) # Fetch all characters from 0 to 5 index location except last character

print(strslice[5:10]) # String Slicing - Retreive all characters from 5 to 10

print(strslice[-4:]) # retreive last four characters of the string

print(strslice[-6:]) # retreive last 6 characters of the string

print(strslice[:4]) # retreive first four characters of the string

print(strslice[:6]) # retreive first six characters of the string

# 3.3 Update and Delete String

# str1 = 'Hello Python'
# print(str1)

# Strings are immutable which means elements of a string can't be changed
# once they have been assigned

# str1[0:5] = 'HOLAA'

# Delete a string

del str1

# print(str1)

