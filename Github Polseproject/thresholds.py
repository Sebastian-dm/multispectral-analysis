# -*- coding: utf-8 -*-
"""
Fedt er grøn i annotering
Kød er blå
Rød er uvidst
"""

##########
# Import #
##########
from dataLoad import data
import numpy as np

def annoMean(spec, anno, annoSpec):
    """
    Funktionen finder middelværdier for pixels i

    input
    --------------
    spec [Array]:
        multispectral picture as array of pixels
    anno [Array]:
        annotation picture as array of pixels
    annoColor [int]:
        choose index of spectre in annotation pic
            0 for red
            1 for green
            2 for blue
    output
    ---------------
    tuple of blue and green arrays of mean values one float per spectre
    """

    meanArray = []
    for i in np.arange(len(spec[0,0,:])):
        valueArray = spec[:,:,i][anno[:,:,annoSpec] == 255]
        meanArray.append(np.mean(valueArray))

    return meanArray

def threshold(spec,anno):
    print("Initial classification")
    gMean = annoMean(spec,anno,1)
    bMean = annoMean(spec,anno,2)
    threshold = []
    for i in np.arange(len(gMean)):
        threshold.append((gMean[i]+bMean[i])/2)
    return threshold


if __name__ == "__main__":
    data = data("01")
#    print(annoMean(data.spec(),data.anno(),2))
    print((threshold(data.spec(),data.anno())))
