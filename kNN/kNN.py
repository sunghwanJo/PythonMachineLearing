__author__ = 'josunghwan'

from numpy import *
import operator
import os

_basedir = os.path.dirname( os.path.abspath( __file__ ) )

def createDataSet():
    group = array([[1, 1.1], [1.1, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify(target, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_matrix = tile(target, (data_set_size, 1)) - data_set
    diff_matrix = diff_matrix ** 2
    diff_matrix = diff_matrix.sum(axis=1)
    distance_matrix = diff_matrix ** 0.5
    distance_indicies = distance_matrix.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[distance_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0)+1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def file_to_matrix(filename):
    result_matrix = []
    class_label = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            list_from_line = line.split('\t')
            class_label.append(list_from_line[-1])
            result_matrix.append(list_from_line[0:3])
    result_matrix = array(result_matrix)
    return result_matrix, class_label

if __name__=='__main__':
    group, labels = createDataSet()
    result = classify([1, 1.1], group, labels, 3)
    print result

    print 'file_to_matrix'
    print file_to_matrix(_basedir+'/data/datingTestSet.txt')



