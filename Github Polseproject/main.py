# -*- coding: utf-8 -*-
"""
Forklaring
"""

##########
# Import #
##########
from numpy import shape, mean
from dataLoad import data
from thresholds import threshold

############
# Dataload #
############
data = data('01')
#print(shape(data.spec()))
#print(shape(data.anno()))
#print(shape(data.color()))

##############
# Thresholds #
##############
thresholds = threshold(data.spec(),data.anno())
#print(len(threshold))
print(thresholds)



##############
# Statestics #
##############
