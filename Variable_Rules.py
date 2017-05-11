# Author: Waqas Khan
# Date:May 09,2017
# Email: wuikhan@gmail.com

import keyword
print(keyword.kwlist)

#it is not allowing us to declare and variable because its a keyword
#and = 10
#h3llo = 20

#example > not recommended because it may confuse the developers

a = b = c = 10
print(a)
print(b)
print(c)

#example > not recommended because it may confuse the developers in the future

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)
