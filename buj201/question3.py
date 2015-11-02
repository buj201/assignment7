'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
import numpy as np

def generate_q3_answers():
    a = np.random.random(30).reshape(10,3)
    ranks = np.argsort(np.abs(a-0.5*np.ones((10,3))))
    mask = (ranks == 0)
    extract_from_a = a[mask]
    print extract_from_a
