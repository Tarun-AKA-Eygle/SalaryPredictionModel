# Polynomial regression
# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def showdataset():
    dataset= pd.read_csv('Position_Salaries.csv')

    return(dataset)
    
def Showliner():
     #importing dataset 

    dataset= pd.read_csv('Position_Salaries.csv')
    X = dataset.iloc[:, 1:2].values

    y = dataset.iloc[:, 2].values

    # Fitting Simple Linear Regression to the dataset

    from sklearn.linear_model import LinearRegression

    lin_reg = LinearRegression()
    lin_reg.fit(X, y)  


    #Visualising  the Linear Regression result
    plt.scatter(X,y,color='red')
    plt.plot(X,lin_reg.predict(X),color='blue')
    plt.title('Level V/s Salary (Linear Regression)')
    plt.xlabel('Level')
    plt.ylabel('Salary')
    plt.show()

def Showpoly():
    #importing dataset 

    dataset= pd.read_csv('Position_Salaries.csv')

    

    X = dataset.iloc[:, 1:2].values

    y = dataset.iloc[:, 2].values

    # Fitting Simple Linear Regression to the dataset

    from sklearn.linear_model import LinearRegression

    lin_reg = LinearRegression()
    lin_reg.fit(X, y)  

    # Fitting Polynomial Regression to the dataset

    from sklearn.preprocessing import PolynomialFeatures

    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    lin_reg2 = LinearRegression()
    lin_reg2.fit(X_poly,y)

    

    #Visualising  the Polynomial Regression result
    X_grid = np.arange(min (X),max (X),0.1)
    X_grid = X_grid.reshape((len(X_grid),1))
    
    plt.scatter(X, y, color='red')
    plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)),color = 'blue')
    plt.title('Regression')
    plt.xlabel('Level')
    plt.ylabel('Salary')
    plt.show()


    


    
    


def PredictionModel(mat):
    #importing dataset 

    dataset= pd.read_csv('Position_Salaries.csv')

    

    X = dataset.iloc[:, 1:2].values

    y = dataset.iloc[:, 2].values

    # Fitting Simple Linear Regression to the dataset

    from sklearn.linear_model import LinearRegression

    lin_reg = LinearRegression()
    lin_reg.fit(X, y)  

    # Fitting Polynomial Regression to the dataset

    from sklearn.preprocessing import PolynomialFeatures

    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    lin_reg2 = LinearRegression()
    lin_reg2.fit(X_poly,y)

    #Visualising  the Linear Regression result
    plt.scatter(X,y,color='red')
    plt.plot(X,lin_reg.predict(X),color='blue')
    plt.title('Level V/s Salary (Linear Regression)')
    plt.xlabel('Level')
    plt.ylabel('Salary')
    #plt.show()


    #Visualising  the Polynomial Regression result
    X_grid = np.arange(min (X),max (X),0.1)
    X_grid = X_grid.reshape((len(X_grid),1))
    
    plt.scatter(X, y, color='red')
    plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)),color = 'blue')
    plt.title('Regression')
    plt.xlabel('Level')
    plt.ylabel('Salary')
    #plt.show()

    
    #Predicting a new result with Linear Regression model
    return(int(lin_reg2.predict(poly_reg.fit_transform(mat))))

