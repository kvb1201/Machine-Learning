import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def gradient_descent(x,y):
    m_curr = b_curr =0
    iterations = 10000
    learning_rate = 0.08
    n = len(x)
    for i in range(iterations):
        y_pred = m_curr*x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_pred) ])
        mder = -(2/n) * sum(x*(y-y_pred))
        bder = -(2/n)*sum((y-y_pred))
        m_curr -= learning_rate*mder
        b_curr -= learning_rate*bder
        
        print("m {},b {}, iteration {} cost {}".format(m_curr,b_curr,i,cost))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)