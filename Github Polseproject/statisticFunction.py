from numpy import size, sum, array, shape
from math import sqrt
from multiSpecPic import multiSpecPic

class analyzeLayer:
    def __init__(self,dArray):
        self.__setMean(dArray)
        self.__setVariance(dArray)

    def __setMean(self,dArray):
        self.__meanVal = sum(dArray)/size(dArray)
    def mean(self):
        """Returns the equivalent mean to the array
                dArray       [array] data of type array"""
        return self.__meanVal

    def __setVariance(self,dArray):
        self.__varianceVal = sqrt(sum((dArray-self.mean())**2)/(size(dArray)-1))
    def var(self):
        """Returns the equivalent variance to the array
                dArray       [array] data of type array"""
        return self.__varianceVal

'''
    def __setSigma(self,dArray):
        """Returns the covariance to the array
                dArray       [array] data of type array"""
            return sum((dArray))
'''

#Main
if __name__ == "__main__":
    pic = multiSpecPic("01")
    data = pic.data[:,:,0]
    print(shape(data))
    test = analyzeLayer(data)
    print(test.var(),test.mean())
