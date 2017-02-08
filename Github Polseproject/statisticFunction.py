from numpy import size, sum, array
from math import sqrt
from multiSpecPic import multiSpecPic

class analyzeData:
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
        """Variance"""
        return self.__varianceVal


#    def __setSigma(self,dArray)

if __name__ == "__main__":
    pic = multiSpecPic("01")
    print(pic.data)

#    arr = array([[1,2,3],[2,3,4],[4,5,6],[6,7,8]])
#    test = analyzeData(arr)
#    print(test.var())
