# -*- coding: utf-8 -*-
"""
Forklaring
"""

##########
# Import #
##########
from numpy import array, shape, zeros, size, append, empty, insert, extract, concatenate, vstack, column_stack, mean, cov, ma
from dataLoad import data
from thresholds import threshold
from numpy import sum as npsum

############
# Dataload #
############
data_01 = data('01')
spec = data_01.specMasked()


##############
# Thresholds #
##############
threshold_01 = threshold(data_01.spec(),data_01.anno())

kød = []
fedt = []
for i in range(shape(spec)[2]):
    m = spec[:,:,i]
    t = threshold_01[i]
    C1 = extract(m >= t, m)
    C2 = extract(m < t, m)

    kød.append(C1)
    fedt.append(C2)


##############
# Statestics #
##############
### Class Covariance
l = len(kød)
ml_kød = max(map(lambda x: len(x), kød))
ml_fedt = max(map(lambda x: len(x), fedt))

norm_kød = empty((0,ml_kød))
norm_fedt = empty((0,ml_fedt))

'''
#Kontrol ift. funktion
    kød_cov = []
    for i in range(l):
        for u in range(l):
            a = zeros(ml_kød)
            a[0:len(kød[i])] = kød[i]

            b = zeros(ml_kød)
            b[0:len(kød[u])] = kød[u]

            cov_kød = 1/(len(a)-1)*sum([(a[i]-mean(a))*(b[i]-mean(b)) for i in range(ml_kød)])

            kød_cov.append(cov_kød)
    print(len(kød_cov))
'''

for i in range(l):
    m_kød = zeros(ml_kød)
    m_kød[0:len(kød[i])] = kød[i]

    m_fedt = zeros(ml_fedt)
    m_fedt[0:len(fedt[i])] = fedt[i]

    norm_kød = vstack([norm_kød, m_kød])
    norm_fedt = vstack([norm_fedt, m_fedt])

cov_kød = cov(norm_kød)
cov_fedt = cov(norm_fedt)

### Overall Covariance
mk = sum(map(lambda x: len(x), kød))
mf = sum(map(lambda x: len(x), fedt))

cov = ((mk-1)*cov_kød + (mf-1)*cov_fedt)/(mk-1+mf-1)

print(shape(cov),len(cov))
