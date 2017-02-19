# -*- coding: utf-8 -*-
"""
Comment til branch 01
"""
from numpy import shape, array
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
        path = dirname(__file__) + "/data/multispectral_day%s.mat" % self.__day
        self.__getSpec = loadmat(path)["immulti"]
    def spec(self):
        """
        Loader multispektralbånds billederne
        """
        return self.__getSpec

# MAIN #
if __name__ == "__main__":
    dataload = data("01")
    print(shape(dataload.spec()))
    print((dataload.spec()))

    
    '''
    if save_img == 'anno':
        self.img = self.anno()
    elif save_img == 'png':
        self.img = self.png()
    elif save_img == 'spec':
        self.img = self.spec()
    '''
    '''
    def save(self):
        for i in range(shape(self.img)[2]):
            path = dirname(__file__) + "/output/lag%s.jpg" % i
            img = fromarray(self.img[:,:,i])
            img.save(path)
    '''
