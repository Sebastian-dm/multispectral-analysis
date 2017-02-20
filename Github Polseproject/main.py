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
from numpy import savetxt, extract, shape, mean, asmatrix, array, sum, size, nonzero, apply_over_axes, empty, vstack, savetxt, loadtxt, around, zeros
from os.path import exists, dirname
import PIL.Image as Image

############
# Dataload #
############
data_01 = data('01')
spec = data_01.specMasked()
nLayers = len(spec[0,0,:])

###################
# Tærskelsværdier #
###################

#Find grænseværdi for klassifikation
threshold = threshold(data_01.spec(),data_01.anno())

#For hvert lag udtrækkes lister for elementer klassificeret som hhv kød og fedt
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
print("Calculating Covriance")
calcs = calc(C1,C2)
#cov_1 = calcs.cov_classes()[0]
#cov_2 = calcs.cov_classes()[1]
cov_sum = calcs.cov_sum()

######################
# Diskriminant værdi #
######################

S = lambda x,mu: x.T*cov_sum.I*mu - 1/2*mu.T*cov_sum.I*mu
mu_1 = mean([mean(x) for x in C1])
mu_2 = mean([mean(x) for x in C2])

tauPic = a = zeros((shape(spec)[0],shape(spec)[1]), dtype=(float,3))
#tau = empty((0,shape(spec)[0]))
print("Final classification")
for r in range(shape(spec)[0]):
    if r%50 == 0:
        print("Classifying row %s of 514" %r)
    row = []
    for c in range(shape(spec)[1]):
        x = spec[r,c,:]
        if spec[r,c].count() == len(spec[r,c]):
            #S1 og S2 er matricer!
            S1 = S(x,mu_1)
            S2 = S(x,mu_2)
            C = S1 >= S2
            if sum(C) > size(C)-sum(C):
                tauPic[r,c] = (255,0,0)
                #row.append(True)
            else:
                tauPic[r,c] = (255,255,255)
                #row.append(False)
        else:
            tauPic[r,c] = (0,0,0)
    #tau = vstack([tau, row])
#savetxt("out.csv", tauPic, delimiter=',')

"""
pixels_kød = sum(tau)
pixels_fedt = size(tau)-sum(tau)
print("Koed: ",int(pixels_kød),"  Fedt: ",int(pixels_fedt))
print(pixels_kød/pixels_fedt)

pixels_kød = sum(tau2)
pixels_fedt = size(tau2)-sum(tau2)
print("Koed: ",int(pixels_kød),"  Fedt: ",int(pixels_fedt))
print(pixels_kød/pixels_fedt)
"""
#Gem billeder
tauPicture = Image.new("RGB",(514,514),color=(50,50,50))
tauPictue.putdata(tauPic)
path = dirname(__file__) + "/output/tau.jpg"
#img = fromarray(tauPic, "RGB")
tauPicture.save(path)
