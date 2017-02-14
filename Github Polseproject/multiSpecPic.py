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
        self.day = day
        '''
        if save_img == 'anno':
            self.img = self.anno()
        elif save_img == 'png':
            self.img = self.png()
        elif save_img == 'spec':
            self.img = self.spec()
        '''
    def anno(self):
        path = dirname(__file__) + "/data/annotation_day%s.png" % self.day
        return array(open(path))

    def png(self):
        path = dirname(__file__) + "/data/color_day%s.png" % self.day
        return array(open(path))

    def spec(self):
        path = dirname(__file__) + "/data/multispectral_day%s.mat" % self.day
        return loadmat(path)["immulti"]

    '''
    def save(self):
        for i in range(shape(self.img)[2]):
            path = dirname(__file__) + "/output/lag%s.jpg" % i
            img = fromarray(self.img[:,:,i])
            img.save(path)
    '''

# MAIN #
if __name__ == "__main__":
    dataload = data("01")
    print(shape(dataload.spec()))
    print((dataload.anno()))
