# coding: utf-8
import numpy as np
def calc_one_loop(new_points, points):
    
    #‌ m is the number of new points (test samples)
    m = len(new_points)
    # n is the number of points (training samples)
    n = len(points)
    # Distance matrix
    d = np.zeros((m, n))
    
    # For each new point
    for i in range(m):
        # Calculate the distance between the new point and all the points
        a = new_points[i] - points
        d[i] = np.sum(np.square(a), axis=1)
        
    return d
