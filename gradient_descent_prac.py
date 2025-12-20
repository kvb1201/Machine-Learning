import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gradient_descent(x,y):
    m_curr = c_curr =0
    learning_rate = 0.000008
    n = len(x)
    iterations = 10000
    for i in range(iterations):
        y_pred = m_curr*x+c_curr
        cost = (1/n) * sum([val**2 for val in (y-y_pred)])
        mder = -(2/n)*sum(x*(y-y_pred))
        cder = -(2/n)*sum(y-y_pred)
        print("cost: {}, m_curr: {}, c_curr: {}, iteration: {}".format(cost,m_curr,c_curr,i))
        m_curr -= learning_rate*mder
        c_curr -= learning_rate*cder
    plt.scatter(x,y)
    plt.xlabel("X - axis")
    plt.ylabel("Y -axis")
    plt.title("Gradient Descent in Linear Regression")
    plt.plot(x,y_pred)
    plt.show()



data = pd.read_csv('test_scores.csv')
x = data['math']
y = data['cs']
gradient_descent(x,y)

