# -*- coding: utf-8 -*-
"""

"""

##########
# Import #
##########
from multiSpecPic import data
import numpy as np

def annoMean(spec, anno, annoColor=0):
    """
    Funktionen finder middelværdier for pixels i

    input
    --------------
    spec [Array]:
        multispectral picture as array of pixels
    anno [Array]:
        annotation picture as array of pixels
    annoColor [int]:
        0 for blue
        1 for green
    output
    ---------------
    tuple of blue and green arrays of mean values one float per spectre
    """

    meanArray = []

    if annoColor:
            mask = spec[:,:,i][anno == (0,255,0)]
    else:
            mask = spec[:,:,i][anno == (0,0,255)]

    for i in np.arange(len(spec[0,0,:])):
        valueArray = spec[mask]
        meanArray.append(mean(blueValueArray))

    return meanArray


if __name__ == "__main__":
    annoMean(data.spec(),data.anno())
