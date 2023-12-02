###$$ IMPORTING NUMPY LIBRARY $$###

### to import special function from numpy
# from numpy import (any function)

### to import all functions from numpy
# from numpy import * 

### import numpy as some thing and re use when need it 
import numpy as np


###$$ CREATE MATRICES $$###
# there are many types to create matrix #

# first way to create matrix 
# is convert a list to a matrix 
# and reshape it to our dimantions

my_list=[i for i in range(1,21)]   # create our list
my_array_1=np.array(my_list)       # convert list into array
my_array_2=my_array_1.reshape(5,4) # reshape our array 

## OUTPUT ##
print(f"list is :{my_list}\n array before reshape is :\n{my_array_2}\n array after reshape is :\n{my_array_2}")

print("--------------------------1--------------------------")
# second way to create matrix
# is making it by sorting it elements
# by function arange()

my_array_3=np.arange(1,21)         # create our array
my_array_4=my_array_3.reshape(4,5) # reshape our array
## another way ##
my_array_5=np.linspace(1,20,20)    # create our array
my_array_6=my_array_5.reshape(5,4) # reshape our array

## OUTPUT ##
print(f"array before reshape is :\n{my_array_3}\n array after reshape is :\n{my_array_4}")

print(f"Another way \n\n array before reshape is :\n{my_array_5}\n array after reshape is :\n{my_array_6}")

print("--------------------------2--------------------------")
# third way to create matrix
# by choise it elements 
# from between two values 

## (FLOAT VALUES) ##
my_array_7=np.random.uniform(1,20,(2,2)) # ( start , end ,(dimintions))
## (INTEGER VALUES) ##
my_array_8=np.random.randint(1,20,(2,2)) # ( start , end ,(dimintions))

## OUTPUT ##
print(f"array with float values:\n{my_array_7}\n array with integer values :\n{my_array_8}")

print("--------------------------3--------------------------")
# fourth way to create matrix
# that it elements is choise
# from between 1 & 0 

my_array_9=np.random.random((3,3)) # ((dimintions))
my_array_10=np.random.rand(3,2)    # (dimintions)

## OUTPUT ##
print(f"my_array_9 is \n{my_array_9}\n my_array_10 is \n{my_array_10}")

print("--------------------------4--------------------------")
print("-----------------------------------------------------")
###$$ SPECIAL CASES OF MATRICES $$###
# there are many special cases of matrices #

# IDENTITY MATRIX
# is a square matrix that all elements is 
# zeros exept that is in diagonal is equal to 1

my_array_11=np.eye(5) # (number of columns or rows)
print(f"my_array_11 is \n {my_array_11}")

print("--------------------------5--------------------------")
# ZEROS MATRIX
# is a matrix that all elements is zeros

my_array_12=np.zeros(5)
my_array_13=np.zeros((5,5))    # ((dimintions))
my_array_14=np.zeros((2,2,2))  # ((dimintions))

print(f"my_array_12 \n{my_array_12}\n my_array_13 \n{my_array_13} \n my_array_14 \n{my_array_14}")

print("--------------------------6--------------------------")
# ONES MATRIX
# is a matrix that all elements is ones

my_array_15=np.ones(5)
my_array_16=np.ones((5,5))     # ((dimintions))
my_array_17=np.ones((2,2,2))   # ((dimintions))

print(f"my_array_15 \n{my_array_15}\n my_array_16 \n{my_array_16} \n my_array_17 \n{my_array_17}")

print("--------------------------7--------------------------")
# FULL MATRIX
# is a matrix that elements are a same value

my_array_18=np.full((3,3),6)
print(f"my_array_18 \n{my_array_18}")

print("--------------------------8--------------------------")
print("-----------------------------------------------------")
###$$ OPERATORS & CONDITIONS IN MATRICES $$###
#this is some of operators can we use as condtions
#   <   >   =   '"<="'   >=
my_array_19=np.arange(1,21).reshape(4,5)
my_array_20=my_array_19<=5  # return matrix of boolean values
print(f"matrix :\n{my_array_19}\nboolean matrix :\n{my_array_20}")

print("--------------------------9--------------------------")
# all()  &  any() functions 
# used to ask about if all elements is (condition)
# or any of elements have this (condition)

my_array_21=np.random.randint(1,20,(4,5))
my_array_22=np.all(my_array_21>5,axis=0) # axis=0 is columns
my_array_23=np.any(my_array_21>5,axis=1) # axis=1 is rows

print(f"matrix is :\n{my_array_21}\n ALL() :\n{my_array_22}\n ANY() :\n{my_array_23}")

print("--------------------------10--------------------------")

