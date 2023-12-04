import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#### READ DATA ####
path = 'txt1.txt'
data = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])


# add a ones column - this makes the matrix multiplication work out easier
data.insert(0, 'Ones', 1)

# set X (training data) and y (target variable)
X=np.array( data.iloc[:,:-1] )   
y=np.array( data.iloc[:,-1]  ).reshape(len(X),1)    #  'pandas.core.frame.DataFrame'

cols = data.shape[1] # ==4 length of columns
##define theta
cols = (len(data.axes[1])) -1 #length of columns 
theta = np.zeros(cols).reshape(cols,1) 


### Create Function Sigmoid ###
def sigmoid(z):
    g = 1/(1+np.exp(-z))
    return g


#### COST FUNCTION ####
def ComputeCost(X,y,theta):
    theta = np.matrix(theta)
    X     = np.matrix(X)
    y     = np.matrix(y)

    z  =(X * theta)
    
    G_z=sigmoid(z)
    
    summation=np.sum(  (np.multiply(-y, np.log(G_z)))  - (np.multiply((1 - y), np.log(1 - G_z))) )
    
    m = X.shape[0]
    return summation / m

print('COST VALUE = ' , round(ComputeCost(X, y, theta),3))




#### GRADIEN DESCENT ####
def GradientDescent(X, y, theta, alpha, iters):
    global start,end
    
    start = time.time()

        
    New_Theta   = np.matrix(np.zeros(theta.shape))  # same shape of my Theta matrix
    parameters  = int(theta.ravel().shape[1])       #get how much theta that i have
    costs       = np.zeros(iters) 
    m           = len(X)
    
    for i in range(iters):
        z  =( X * theta )
        G_z=sigmoid( z ) 
        term=(G_z - y)
        
        for j in range(parameters):
            term1 = np.multiply(term , X[:,j])
            New_Theta[j,0] = theta[j,0] - (  (alpha) * (np.sum(term1)/m )  )

            
        theta    = New_Theta
        costs[i] = ComputeCost(X,y, theta)
    
    end = time.time()

    return theta, costs


# initialize variables for learning rate and iterations
alpha = 0.1
iters = 100

# perform gradient descent to "fit" the model parameters
New_theta, costs = GradientDescent(X, y, theta, alpha, iters)

def New_Theta():
    c=0
    for i in New_theta:
        print(f"Theta {c} : {round((float(i)),5)}")
        c+=1
New_Theta()

print('\nFinal Cost = ' , round(ComputeCost(X,y,New_theta) , 4)) # final cost
print(f"\nTIME IS : {round((end-start),4)} Sec.")