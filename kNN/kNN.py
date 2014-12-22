__author__ = 'josunghwan'

from numpy import *
import operator
def createDataSet():
    group = array([[1, 1.1], [1.1, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify(target, data_set, labels, k):
    print data_set
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


if __name__=='__main__':
    group, labels = createDataSet()
    classify([1, 1.1], group, labels, 3)


