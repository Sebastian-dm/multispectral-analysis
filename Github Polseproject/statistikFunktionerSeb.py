# -*- coding: utf-8 -*-
"""
Indeholder statistikfunktioner til brug til klassificering af
intensitets-pixelværdier i spektralbåndsbilleder.
"""
##########
# IMPORT #
##########
import numpy as np

###############
# DEFINITIONS #
###############

def mean():
    mu = (0,0)
    return mu

def colCov():
    """
    Sigma(a,b)
    Beregner den samlede kovarians "Collcected Covariance" for dimension a og b

    input:
    a [int]
        dimension
    b [int]
        dimension
    """
    cov1 =
    cov2 =
    colCov = 
    return colCov

def discr(x):
    """
    Si(x) -> (S1,S2)
    Beregner diskriminantværdien for hver klasse
    på tværs af lag på pixelplaceringen x
    retuneres som tuple med værdierne (S1,S2)

    input:
    x [array]
        liste af intensitetsværdierne på alle 19 lag til pixelplacering.
    """

    classes = [1,2]
    S = (0,0)

    for i in classes:
        S[i] = np.transpose(x)*np.linalg.inv(colCov())*mean()[i]-1/2*np.transpose(mean()[i])*np.linalg.inv(colCov())*mean()[i]

    return S

########
# MAIN #
########
if __name__ == "__main__":
    data = data("01")
    print(shape(data.spec()))
    print((data.spec()))

    #print(shape(data01.spec()))
    #print((data01.anno()))
    data.save("specMasked")
