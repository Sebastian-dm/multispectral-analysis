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
from numpy import extract, shape, mean, asmatrix, array, sum, size, nonzero, apply_over_axes, empty, vstack, savetxt, loadtxt, around, zeros
from os.path import exists, dirname
from PIL.Image import fromarray

############
# Dataload #
############
data_01 = data('28')
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
print("Calculating Covriance")
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
S = lambda x,mu: x.T*cov_sum.I*mu - 1/2*mu.T*cov_sum.I*mu
mu_1 = mean([mean(x) for x in C1])
mu_2 = mean([mean(x) for x in C2])

tau2 = zeros(shape(spec))
tau = empty((0,shape(spec)[0]))
print("Final classification")
for i in range(shape(spec)[0]):
    if i%50 == 0:
        print("Classifying row %s of 514" %i)
    row = []
    for u in range(shape(spec)[1]):
        x = spec[i,u,0:r]
        #S1 og S2 er matricer!
        S1 = S(x,mu_1)
        S2 = S(x,mu_2)
        C = S1 >= S2
        if sum(C) > size(C)-sum(C):
            tau2[i,u] = 255
            row.append(True)
        else:
            tau2[i,u] = 10
            row.append(False)
    tau = vstack([tau, row])

tau = around(tau)

print(tau)
print(shape(tau))

pixels_kød =sum(tau)
pixels_fedt = size(tau)-sum(tau)
print("Kød: ",int(pixels_kød),"  Fedt: ",int(pixels_fedt))

print(pixels_kød/pixels_fedt)

#data = day 01
    #kød = 72942
    #fedt = 191254
    #forhold = 0.38
    #[Finished in 345.145s]

#data = day 06
    #kød = 71587
    #fedt = 192609
    #forhold = 0.371670067338
    #[Finished in 350.866s]

#data = day 13
    #kød = 64854
    #fedt = 199342
    #forhold = 0.325340369817
    #[Finished in 398.991s]

#data = day 20
    #kød = 62428
    #fedt = 201768
    #forhold = 0.309404861029
    #[Finished in 398.991s]

#Gem billeder
path = dirname(__file__) + "/output/tau.jpg"
img = fromarray(tau2, "L")
img.save(path)
