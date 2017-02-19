# -*- coding: utf-8 -*-
"""
Forklaring
"""

##########
# Import #
##########
from dataLoad import data
from thresholds import threshold
from statistic import calc

from numpy import extract, shape

############
# Dataload #
############
data_01 = data('01')
spec = data_01.specMasked()

###################
# Tærskelsværdier #
###################
threshold_01 = threshold(data_01.spec(),data_01.anno())

C1 = []
C2 = []
for i in range(3):#shape(spec)[2]):
    m = spec[:,:,i]
    t = threshold_01[i]
    c1 = extract(m >= t, m)
    c2 = extract(m < t, m)

    C1.append(c1)
    C2.append(c2)

#############
# Statestik #
#############
### Samlede kovarians
calcs = calc(C1,C2)
cov_kød = calcs.cov_classes()[0]
cov_fedt = calcs.cov_classes()[1]
cov_sum = calcs.cov_sum()
print(cov_kød,'\n')
print(cov_fedt,'\n')
print(cov_sum)

### Diskriminant værdi
#print(shape(data_01.spec()))

#Si =
