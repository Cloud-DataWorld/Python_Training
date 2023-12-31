'''
1.Numeric
2.Float
3.Complex Data Type
4.Boolean
5.Strings
4.List
5.Tuple
6.Dict
'''
import sys

val1 = 10 # Integer data type
print(val1)
print(type(val1)) # type of object
print(sys.getsizeof(val1)) # size of integer object in bytes
print(val1, "is Integer?", isinstance(val1,int)) # val1 is an instance of integer

# Float Data Type
val2 = 10.25 # Float data type
print(val2)
print(type(val2))
print(sys.getsizeof(val2))
print(val2,"is float ?", isinstance(val2,float))

# Complex Data Type
val3 = 25 + 10j #complex data type
print(val3)
print(type(val3))
print(sys.getsizeof(val3))
print(val3,"is complex ?",isinstance(val3,complex))

# get Size of a data type in bytes

print(sys.getsizeof(int()))
print(sys.getsizeof(float()))
print(sys.getsizeof(complex()))


# Boolean Data Type
# Boolean data type can have only two possible values true or false

bool1 = True
bool2 = False

print(type(bool1))
print(type(bool1))
print(type(bool2))
print(isinstance(bool1,bool))
print(isinstance(bool2,bool))
print("Boolean Examples")
print(bool(0))
print(bool(1))
print(bool(None))
print(bool(False))

