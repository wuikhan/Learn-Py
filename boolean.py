"""
Boolean 
"""

a = True
b = False

print(a)
print(b)

print("********")

# Boolean of 0 is false, everything else is true

print(bool(0))  # 0 means false
print(bool(1))  # 1,2... is true
print(bool(2))

# empty string will be considered as 0 that is why result will be false

c = ""
print(bool(c))  # this will print false

d = "some value"
print(bool(d))