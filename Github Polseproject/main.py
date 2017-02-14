# -*- coding: utf-8 -*-
"""
Forklaring
"""

##########
# Import #
##########
import numpy as np
from dataLoad import data
from thresholds import threshold

###############
# Main Script #
###############


###############
# test        #
###############


if __name__ == "__main__":
    data1 = data("01")
    spec1 = data1.spec()

    for i in range(len(threshold())):
        print(np.ma.masked_where(spec1[:,:,i]>threshold()[i],spec1[:,:,i]))
    #print(annoMean(data.spec(),data.anno(),2))
