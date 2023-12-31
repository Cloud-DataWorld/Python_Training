# Indentation refers to the spaces at the beginning of a code line.
# It is very important as python uses indentation to indicate a block of code.
# If the indentation is not correct  we will end up with IndentationError error.

# example 1
# 1. correct indentation
p =10
if p==10:
    print( 'P is equal to 10')

# 2. if indentation is skipped  we will encounter "IndentationError"
# p =10
# if p==10:
# print('P is equal to 10')

# example 2
# 3. Correct indentation
for i in range(0,5):
    print(i)

# 4. if indentation is skipped we will encounter "IndentationError"
# for i in range(0,5):
# print(i)

# example 3
# 5 correct indentation but less readable
for i in range(5,10): print(i)

# example 4
j=20
for i in range(10,15):
    print(i) # inside the for loop
print(j) # outside the for loop