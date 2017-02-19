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
from numpy import extract, shape, mean, asmatrix, array, sum, size

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
for i in range(shape(spec)[2]):
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
mu_1 = mean([mean(x) for x in C1])
mu_2 = mean([mean(x) for x in C2])

S = lambda x,mu: x.T*cov_sum.I*mu - 1/2*mu.T*cov_sum.I*mu

x = data_01.spec()[214,214,:]
S1 = S(x,mu_1)
S2 = S(x,mu_2)
C = S1 < S2
print(C)
if sum(C) > size(C)-sum(C):
    print(1)
else:
    print(2)

'''
tau = []
for i in range(shape(data_01.spec())[0]):
    row = []
    for u in range(shape(data_01.spec())[1]):
        x = data_01.spec()[i,u,:]
        S1 = S(x,mu_1)
        S2 = S(x,mu_2)
        C = S1 < S2
        if sum(C) > size(C)-sum(C):
            row.append(1)
        else:
            row.append(2)
    tau.append(array(row))

print(tau)
'''
