#from numpy import size, sum, array, shape
from math import sqrt
from dataLoad import data
from numpy import array, shape, zeros, size, append, empty, insert, extract, concatenate, vstack, column_stack, mean, cov, ma, asmatrix, matrix, around, var


class calc:
    def __init__(self,dArray,aArray=[]):
        self.__setMean(dArray)
        self.__setVariance(dArray)
        self.__setCovClass(dArray,aArray)
        self.__setCovSum(dArray,aArray)

    ### MEAN ###
    def __setMean(self,dArray):
        try:
            self.__meanVal = mean(dArray)
        except:
            self.__meanVal = None
    def mean(self):
        """
        Den ækvivalente middel til arrayet
        """
        return self.__meanVal

    ### VARIANCE ###
    def __setVariance(self,dArray):
        try:
            self.__varianceVal = var(dArray)
        except:
            self.__varianceVal = None
    def var(self):
        """
        Den ækvivalente varians til arrayet
        """
        return self.__varianceVal

    ### COVARIANCE ###
    ### Class
    def __setCovClass(self,dArray,aArray):
        l = len(dArray)
        ml_kød = max(map(lambda x: len(x), dArray))
        ml_fedt = max(map(lambda x: len(x), aArray))

        norm_kød = empty((0,ml_kød))
        norm_fedt = empty((0,ml_fedt))

        for i in range(l):
            m_kød = zeros(ml_kød)
            m_kød[0:len(dArray[i])] = dArray[i]

            m_fedt = zeros(ml_fedt)
            m_fedt[0:len(aArray[i])] = aArray[i]

            norm_kød = vstack([norm_kød, m_kød])
            norm_fedt = vstack([norm_fedt, m_fedt])

        cov_kød = asmatrix(cov(norm_kød))
        cov_fedt = asmatrix(cov(norm_fedt))

        self.__covClass = cov_kød,cov_fedt
    def cov_classes(self):
        """
        De individuelle kovarianser for de to klasser
        """
        return self.__covClass


    ### Sum
    def __setCovSum(self,dArray,aArray):
        cov_kød = self.__covClass[0]
        cov_fedt = self.__covClass[1]

        mk = sum(map(lambda x: len(x), dArray))
        mf = sum(map(lambda x: len(x), aArray))
        cov_m = asmatrix(((mk-1)*cov_kød + (mf-1)*cov_fedt)/(mk-1+mf-1))
        self.__covSum = cov_m

    def cov_sum(self):
        """
        Den samlede kovarians for to klasser
        """
        return self.__covSum

#Main
if __name__ == "__main__":
    pic = data("01")
    data = pic.spec()[:,:,0]
    print(shape(data))
    test = calc(data)
    print(test.var(),test.mean())
