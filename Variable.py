# Author: Waqas Khan
# Date:May 09,2017
# Email: wuikhan@gmail.com

# declare a variable and initialize it
f = 0;
print(f)

# re-declaring the variable worls
f = "abcd"
print(f)

# ERROR : different types can not be combined
# print "String is " + 123
print("String is " + str(123))

print("*********1**********")
f = "This is variable"
print (f)

# Global vs local variable function
def somefunction():
    # global f
    f = "def"
    print (f)

somefunction()
print (f)

print("********2***********")
f = "This is variable"
print (f)


# Global vs local variable function
def somefunction():
    global f
    f = "def"
    print (f)

somefunction()
print (f)

print("********3***********")
c = "nyc"
d = c
print(c==d) #OR
print(d is c)
