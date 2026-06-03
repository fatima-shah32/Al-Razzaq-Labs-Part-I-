# Creating variables
my_integer = 10
my_float = 20.5
my_string = "Hello, World!"
my_boolean = True

# Printing variables
print(my_integer)
print(my_float)
print(my_string)
print(my_boolean)

# Checking types
print(type(my_integer))
print(type(my_float))
print(type(my_string))
print(type(my_boolean))

# Type casting
new_float = float(my_integer)
print(new_float)
print(type(new_float))

new_string = str(my_float)
print(new_string)
print(type(new_string))

another_string = "15"
new_integer = int(another_string)
print(new_integer)
print(type(new_integer))

new_integer_from_boolean = int(my_boolean)
print(new_integer_from_boolean)
