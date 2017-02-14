# -*- coding: utf-8 -*-
"""
Comment til branch 01
"""
from numpy import shape, array
from scipy.io import loadmat
from PIL.Image import fromarray, open
from os.path import dirname

class data:
    def __init__(self, day="01"):
        self.day = day

    def spec(self):
        spec_path = dirname(__file__) + "/data/multispectral_day%s.mat" % self.day
        return loadmat(spec_path)["immulti"]

    def save(self):
        for i in range(shape(self.spec())[2]):
            savepath = dirname(__file__) + "/output/lag%s.jpg" % i
            img = fromarray(self.spec()[:,:,i])
            img.save(savepath)

    def anno(self):
        anno_path = dirname(__file__) + "/data/annotation_day%s.png" % self.day
        return array(open(anno_path).convert('L'))

#    def png:


# MAIN #
if __name__ == "__main__":
<<<<<<< HEAD
    msInst = multiSpecPic("01")
    print(msInst.getLayer(2))
    #msInst.saveImgs()
=======
    dataload = data("01")
    print((dataload.anno()))
    #.spec()[:,:,0])
    dataload.save()
>>>>>>> origin/master
