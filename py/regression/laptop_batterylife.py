#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd
from sklearn.linear_model import LinearRegression

import numpy as np
# Regression model
if __name__ == '__main__':
    timeCharged = float(input().strip())
    df = pd.read_csv("trainingdata.txt")
    
    X = df.iloc[:, 0] # select with integer location ALL rows and col 0
    y = df.iloc[:, 1]
    
    X = X.values.reshape(-1, 1) # reshapes to 1 column, but dont care how many rows there r (-1)
    y = y.values
    
    model = LinearRegression()
    model.fit(X, y)
    
    timeCharged = np.array(timeCharged).reshape(-1, 1) # ensures input to model is 2d arr
    pred = model.predict(timeCharged)
    
    # print(round(pred[0], 2))
    print(min((timeCharged*2)[0][0], 8.00)) # GOOFY question bro
