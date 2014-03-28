#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import numpy as np
import math
import random

def logsumexp(vec) :
	vec = np.array(vec)
	max_vec = max(vec)
	return max_vec + np.log(sum(np.exp(vec - max_vec)))

def cal_prob(y_list, x, WP=1, WL=1):
    y_list_sum = sum(y_list)
    nume = np.exp(WP*y_list_sum + WL*x)
    com_nume = np.exp(WP*(len(y_list)-y_list_sum) + WL*(1-x))

#    deno = logsumexp([nume, com_nume])
#    val = np.exp(nume-deno)
    deno = nume + com_nume
    val = float(nume)/deno

    rand_val = random.random()
    return 1 if rand_val < val else 0

def cal_MAE(WP=1, WL=1):
    y_img = np.array(x_img)
    cumu_img = np.array(y_img)

    T_val = 100
    y_img_list = []
    MAE_list
    for T in range(T_val):
        #print 'iter num:'
        #print T
        y_img[0,0] = cal_prob([y_img[0,1],y_img[1,0]], x_img[0,0], WP, WL)
        y_img[x_len-1,0] = cal_prob([y_img[x_len-1,1],y_img[x_len-2,0]], x_img[x_len-1,0], WP, WL)
        y_img[0,y_len-1] = cal_prob([y_img[0,y_len-2],y_img[1,y_len-1]], x_img[0,y_len-1], WP, WL)
        y_img[x_len-1,y_len-1] = cal_prob([y_img[x_len-1,y_len-2],y_img[x_len-2,y_len-1]], x_img[x_len-1,y_len-1], WP, WL)
        
        for i in range(1, x_len-1) :
            y_img[i, 0] = cal_prob([y_img[i-1, 0], y_img[i+1, 0], y_img[i, 1]], x_img[i, 0], WP, WL)
            y_img[i, y_len-1] = cal_prob([y_img[i-1, y_len-1], y_img[i+1, y_len-1], y_img[i, y_len-2]], x_img[i, y_len-1], WP, WL)

        for j in range(1, y_len-1) :
            y_img[0, j] = cal_prob([y_img[0, j-1], y_img[0, j+1], y_img[1, j]], x_img[0, j], WP, WL)
            y_img[x_len-1, j] = cal_prob([y_img[x_len-1, j-1], y_img[x_len-1, j+1], y_img[x_len-2, j]], x_img[x_len-1, j], WP, WL)

        for i in range(1, x_len-1):
            for j in range(1, y_len-1):
                y_img[i, j] = cal_prob([y_img[i-1, j], y_img[i+1, j], y_img[i, j-1], y_img[i, j+1]], x_img[i, j], WP, WL)

        cumu_img += y_img
#        MAE_val = 1/float(HW) * np.sum(np.abs(cumu_img/(T+2)-true_img))
#        print MAE_val
#        MAE_list.append(MAE_val)

#    np.savetxt('MAE3.txt', MAE_list)
    mean_img = cumu_img/(T_val + 1)#y_img_list.append(y_img)
    MAE = 1/float(HW) * np.sum(np.abs(mean_img-true_img))
    return MAE
            
if __name__ == '__main__':
    file_path = '../Data/stripes-noise.txt'
    true_img_file_path = '../Data/stripes.txt'
    x_img = np.loadtxt(file_path)
    true_img = np.loadtxt(true_img_file_path)

    x_len, y_len = x_img.shape
    HW = x_len * y_len
    print 1/float(HW) * np.sum(np.abs(x_img-true_img))

    WP_list = range(1,11)

    WF_list = range(1,11)
    WF_list = map(lambda a:a*0.05, WF_list)
    aux_list = range(1,10)
    aux_list = map(lambda a:a*0.5+0.5, aux_list)
    WF_list.extend(aux_list)

    WF_2 = range(1,11)
 #   WF_2 = map(lambda a:a*0.1+3.5, WF_2)

    for WP in WP_list:
        MAE_list = []
        for WF in WF_2:#WF_list:
            print WF
            MAE_list += [cal_MAE(WP, WF)]
            print MAE_list

        np.savetxt('MAE'+str(WP)+'.txt', MAE_list)

#MAE1.txt 0.1:0.1:1,1:1:10
