# Author: Waqas Khan
# Date:May 09,2017
# Email: wuikhan@gmail.com

"""
Arthimetic Order of Precedence
"""

print(2+4+3+4)
print(2+4+3+8)
print(2+4+3+10)

# the order is div or multi first and then we do addition or subtraction, priroity is always div/multi
print(2+4*3/2)

#same example but within parenthisis the order has changed
print((2+4) * 3 / 2)

#in this example the order again has changed within the brackets now it is multiplying first
print((2+4*2) * 3 / 2)

a = 10
a = a + 1
print(a) #OR

b = 10
b += 2
print(b)

b -= 4
print(b)

b *= 2
print(b)

b /= 4
print(b)


