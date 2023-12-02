from numpy import *
import numpy 
"""
###change sort
x=random.randint(1,101,size=(5,3)) ## == x=random.randint(1,101,(10,10))
print(x)
y=x.tolist()
random.shuffle(y)
z=array(y)
print(z)

for x in y:
    random.shuffle(x)
print(y)
"""
""" 
### Ask about Difference between Elemnts of two matreces

x=arange(12).reshape(3,4)
z=arange(12).reshape(3,4)
a=2*z
print(x,"\n-------------\n",a)
print(isclose(x,z,rtol=0.1))
print(isclose(x,a,rtol=0.1))
""" 
"""  
### Multiply Elements in matreces عنصر ف اخوة 
x=arange(25).reshape(5,5)
z=arange(25).reshape(5,5)
a=multiply(x,z)
b=x*z
print(a)
print(b)



##multiply elemnts in matrix in each other
x =arange(9).reshape(3,3)
z =arange(1,9)
print(x)
print(z)
print(multiply.reduce(x))#columns
print(multiply.reduce(z))


##multiply each elemnt in all elemnt in it row
x=arange(9).reshape(3,3)
print(x)
print(multiply.outer(x,x))



### power of elemnts in matrices
x =arange(5)
print(x)
print(power(x,2))
print(x**2)
### Sum elemnts of matrices 
x =arange(15)
print(add.reduce(x))
print(sum(x))
"""
""" 
# x=[]
# for i in range(10):
#     x.append([])
#     for o in range(10):
#         if i!=o:
#             x[i].append(0)
#         else:
#             x[i].append(o+1)
# print(array(x))
"""

### poly nomial ###
import numpy as np


# Polynomial = np.polynomial.Polynomial
# X= np.array([0,20,40,60,80,100,120,140,160,180])
# Y= np.array([10,9,8,7,6,5,4,3,2,1])

# points,stats = Polynomial.fit(X,Y,1,full=True)

# print(points)



# a = poly1d((-7))
# b = poly1d((-7,2))
# c = poly1d((-7,2,1))
# print(a,"\t",a(1))
# print(b,"\t",b(1))
# print(c,"\t",c(1))
#-----------------)
# b=polyval((-7,2),1)
# c=polyval((-7,2,1),1)

# print(b)
# print(c)


###drivediv
# a=poly1d((-7,2,1))
# b=polyder(a)
# c=b(3)
# print(a,"\n-----1-----",b,"\n",c)



#####----------
# a=poly1d((-7,2,1))
# b=polyder(a)
# print(a,"\n-----2-----",b)
# ### integrition
# a=polyint(b)
# print("Integration : ",a)


###dates
# x = datetime64('2015-07-04')
# y = x + range(50)
# print(x,"\n-----------",y) 

###$$$ PANDAS $$$###
import pandas as pd

















