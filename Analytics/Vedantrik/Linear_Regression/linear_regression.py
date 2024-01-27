import pandas as pd
import numpy as np
from getpass import getpass
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def time_to_seconds(time_str):
    try:
        hours, minutes = map(int, time_str.split(':'))
        total_seconds = hours * 3600 + minutes * 60
        return total_seconds
    except ValueError:
        print("Invalid time format. Please use HH:MM.")

def linear_regression(points):
    dataset = pd.read_csv('C:\\Users\\Shardul\\Desktop\\PROGRAMMING\\IOconnect\\Analytics\\Vedantrik\\Linear_Regression\\IOconnect_dataset.csv')

    dataset.columns[dataset.isna().any()]
    dataset['SECONDS'] = (dataset['TIME'].apply(time_to_seconds))
    dataset = dataset.drop(columns=['TIME'])

    # X = dataset['SECONDS'].values.reshape(-1,1)
    # X = np.array([[1],[2],[3],[4],[5],[6],[7]])
    X = np.array([[x+1] for x in range(len(points))])
    # print(X)

    # now take points from the analysis db to the linear reg code and then generate the pred points

    # Y = dataset.iloc[:, :-1]
    Y = np.array(points)
    # print(Y)
    model = LinearRegression()
    model.fit(X, Y)

    Y_pred = model.predict(X)
    plt.scatter(X, Y, color="black", label="Actual Data points" )
    plt.plot(X, Y_pred, color="blue", linewidth=2, label="Predicted Data")
    plt.xticks(rotation=45)

    plt.xlabel("Days")
    plt.ylabel("Temp")
    plt.legend()
    # Add a title
    plt.title("Scatter Plot with Regression Line")


    result = dict()
    result['points'] = dict()
    
    for i in range(len(points)):
        result['points']['p'+str(i+1)] = model.predict([[i]])[0]

    result['slope'] = model.coef_[0]
    result['intercept'] = model.intercept_

    plt.show()
    return result

# dictionary = dict()
# dictionary[1] = dict()
# dictionary[1][1] = 3
# print(dictionary)
# print(linear_regression([1,2,3,4,5,6,7]))