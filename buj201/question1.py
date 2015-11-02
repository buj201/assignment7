'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
import numpy as np

def generate_q1_answers():
    #Create initial 2D array
    vec = np.arange(1,16).reshape(3,5).T
    
    #Question 1A
    vec_1A = vec[np.array([1,3])]
    print 'Question 1A: \n', vec_1A

    #Question 1B
    vec_1B = vec[:, 1]
    print 'Question 1B: \n', vec_1B

    #Question 1C
    vec_1C = vec[np.arange(1,4)]
    print 'Question 1C: \n', vec_1C

    #Question 1D
    vec_1D = np.array([i for i in vec.flat if 2<i<12])
    print 'Question 1D: \n', vec_1D