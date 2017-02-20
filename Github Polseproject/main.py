# -*- coding: utf-8 -*-
"""
Forklaring
"""
##########
# Import #
##########
from dataLoad import data
from thresholds import threshold
from statistics import calc
from numpy import extract, shape, mean, asmatrix, array, sum, size, nonzero, apply_over_axes, empty, vstack, savetxt, loadtxt, around
from os.path import exists, dirname
from PIL.Image import fromarray

############
# Dataload #
############
data_01 = data('01')
spec = data_01.specMasked()

###################
# Tærskelsværdier #
###################
threshold = threshold(data_01.spec(),data_01.anno())
C1 = []
C2 = []
#Bestemmer hvor mange bånd der kigges på i scriptet
r = shape(spec)[2]
for i in range(r):
    m = spec[:,:,i]
    t = threshold[i]
    c1 = extract(m >= t, m)
    c2 = extract(m < t, m)

    C1.append(c1)
    C2.append(c2)

#############
# Kovarians #
#############
calcs = calc(C1,C2)
cov_1 = calcs.cov_classes()[0]
cov_2 = calcs.cov_classes()[1]
cov_sum = calcs.cov_sum()

######################
# Diskriminant værdi #
######################
'''
#Test
    x = spec[214,214,0:r]
    S1 = S(x,mu_1)
    S2 = S(x,mu_2)
    C = S1 >= S2
    print(C)
    if sum(C) > size(C)-sum(C):
        print(True)
    else:
        print(False)
'''
data = spec
S = lambda x,mu: x.T*cov_sum.I*mu - 1/2*mu.T*cov_sum.I*mu
mu_1 = mean([mean(x) for x in C1])
mu_2 = mean([mean(x) for x in C2])

tau = empty((0,shape(data)[0]))
for i in range(shape(data)[0]):
    row = []
    for u in range(shape(data)[1]):
        x = data[i,u,0:r]
        #S1 og S2 er matricer!
        S1 = S(x,mu_1)
        S2 = S(x,mu_2)
        C = S1 >= S2
        if sum(C) > size(C)-sum(C):
            row.append(True)
        else:
            row.append(False)
    tau = vstack([tau, row])
tau = around(tau)

print(tau)
print(shape(tau))

pixels_kød =sum(tau)
pixels_fedt = size(tau)-sum(tau)
print(pixels_kød,pixels_fedt)

print(pixels_kød/pixels_fedt)
#data = spec -->
    #kød = 72942
    #fedt = 191254
    #forhold = 0.38

#img = fromarray(tau)
#img.save(path)
