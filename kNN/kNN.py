__author__ = 'josunghwan'

from numpy import *

def createDataSet():
    group = array([[1, 1.1], [1.1, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


if __name__=='__main__':
    group, labels = createDataSet()
    print group