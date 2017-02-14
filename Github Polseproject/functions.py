# -*- coding: utf-8 -*-
"""

"""

##########
# Import #
##########
from multiSpecPic import data


def annoMean(pic1, pic2):
    """
    Funktionen finder middelværdier for pixels i

    input
    --------------
    pic1 [Array]:
        multispectral picture as array of pixels
    pic2 [Array]:
        annotation picture as array of pixels

    output
    ---------------
    array of mean values one float per spectre
    """

    print(pic1)
    print(pic2)

    """
    middenværdi = []
    for i to m:
        g = Data[Anno = (0,0,255))]
        mu = mean(g[:,i])

    g [[1..19],[1..19]..m]
    """

if __name__ == "__main__":
    annoMean(data.spec(),data.anno())
