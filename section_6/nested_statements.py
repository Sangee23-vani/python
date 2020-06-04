x = 25
def printer():
    x = 50
    return x

print(x)
print(printer())
print(x)

# LEGB

# L - Local         ->
lambda num : num ** 2       # num is a local varable

# E - Enclosing function local
x = 25                      # Global
def printer():
    x = 50                  # Enclosing function local
    return x

print(x)
print(printer())

# G - Global
x = 25                      # Takes the global variable
def printer():
    return x
print(x)
print(printer())
