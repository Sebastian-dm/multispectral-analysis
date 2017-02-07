# -*- coding: utf-8 -*-
import numpy as np
import scipy.io
from PIL import Image

class multiSpecPic:
    def __init__(self, nData="01"):
        self.nData = nData
        self.path = "C:/Users/sebas/Google Drev/Dokumenter/DTU/DTU Kurser/Matematisk Modellering/Øvelser/01 Pølsens Kvalitet/Modtaget/data/multispectral_day%s.mat" % nData
        self.data = scipy.io.loadmat(self.path)["immulti"]

    def getLayer(self, nLayer):
        """
        Returns specified layer as a 2d array of values between 0 and 255
            nlayer       [int] indentifying number of layer to get.
        """
        return self.data[:,:,nLayer]

    def getPixel(self,r,c,l):
        return self.data[r,c,l]

    def getLayerPixel(self,r,c,l):
        return self.data[r,c,l]

    def saveImgs(self):
        for i in np.arange(19):
            savepath = "Output/lag%s.jpg" % i
            img = Image.fromarray(self.getLayer(i))
            img.save(savepath)

# MAIN #
if __name__ == "__main__":
    msInst = multiSpecPic("01")
    msInst.saveImgs()
