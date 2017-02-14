# -*- coding: utf-8 -*-
"""
Comment til branch 01
"""
from numpy import arange, shape
from scipy.io import loadmat
from PIL.Image import fromarray
from os.path import dirname

class multiSpecPic:
    def __init__(self, nData="01"):
        self.nData = nData
        self.path = dirname(__file__) + "/data/multispectral_day%s.mat" % nData
        self.data = loadmat(self.path)["immulti"]

    def getLayer(self, nLayer):
        """
        Returns specified layer as a 2d array of values between 0 and 255
            nlayer       [int] indentifying number of layer to get.
        """
        return self.data[:,:,nLayer]

    def getPixel(self,r,c,l):
        return self.data[r,c,l]

    def saveImgs(self):
        for i in range(shape(self.data)[2]):
            savepath = dirname(__file__) + "/output/lag%s.jpg" % i
            img = fromarray(self.getLayer(i))
            img.save(savepath)

# MAIN #
if __name__ == "__main__":
    msInst = multiSpecPic("01")
    print(msInst.getLayer(2))
    #msInst.saveImgs()
