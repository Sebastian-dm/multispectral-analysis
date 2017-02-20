# -*- coding: utf-8 -*-
"""
Comment til branch 01
"""
from numpy import shape, array, empty_like, ma, all, array_equal, equal, reshape, arange, zeros_like
from scipy.io import loadmat
#from scipy.misc import imread
from PIL.Image import fromarray, open
from os.path import dirname

class data:
    def __init__(self, day="01"):#, save_img='spec'
        self.__day = day
        self.__setAnno()
        self.__setColor()
        self.__setSpec()

    ### ANNOTERINGER ###
    def __setAnno(self):
        path = dirname(__file__) + "/data/annotation_day%s.png" % self.__day
        self.__getAnno = array(open(path))
    def anno(self):
        """
        Loader annoterings billederne
        """
        return self.__getAnno

    ### COLOR ###
    def __setColor(self):
        path = dirname(__file__) + "/data/color_day%s.png" % self.__day
        self.__getColor = array(open(path))
    def color(self):
        """
        Loader farve billederne
        """
        return self.__getColor

    ### SPEKTRALBÅND ###
    def __setSpec(self):
        print("loading spectral picture")
        path = dirname(__file__) + "/data/multispectral_day%s.mat" % self.__day
        self.__getSpec = loadmat(path)["immulti"]
    def spec(self):
        """
        Loader multispektralbånds billederne
        """
        return self.__getSpec

    ### MASKED SPEKTRALBÅND ###
    def specMasked(self):
        #Create array of black values [0,0,0], False values [0,0,..,nLayers]
        print("Masking Array")
        annoArr = self.anno()
        specArr = self.spec()
        blackArr = zeros_like(annoArr)
        nLayers = len(specArr[0,0,:])
        maskArr = empty_like(specArr)

        maskCount = 0
        for i in arange(shape(annoArr)[0]):
            for j in arange(shape(annoArr)[1]):
                if all(annoArr[i,j] == [0,0,0]):
                    maskCount += 1
                    maskArr[i,j] = array([True] * nLayers)

        maskedArr = ma.masked_where(maskArr, specArr)
        print("Percentage: ",int(maskCount/(514*514)*100))
        return maskedArr

    ### SAVE ###
    def save(self, data="spec"):

        if data == 'anno':
            path = dirname(__file__) + "/output/png.jpg"
            img = fromarray(self.anno())
            img.save(path)

        elif data == 'png':
            path = dirname(__file__) + "/output/png.jpg"
            img = fromarray(self.png())
            img.save(path)

        elif data == 'spec':
            dataArr = self.specMasked()
            for i in range(shape(dataArr)[2]):
                path = dirname(__file__) + "/output/lag%s.jpg" % i
                img = fromarray(dataArr[:,:,i])
                img.save(path)

        elif data == 'specMasked':
            #For hvert lag, lav seperat filnavn og gem billede
            dataArr = self.specMasked()
            for i in range(shape(dataArr)[2]):
                path = dirname(__file__) + "/output/lag%s.jpg" % i
                img = fromarray(dataArr[:,:,i])
                img.save(path)

# MAIN #
if __name__ == "__main__":
    data = data("01")
    print(shape(data.spec()))
    print((data.spec()))

    #print(shape(data01.spec()))
    #print((data01.anno()))
    data.save("specMasked")
