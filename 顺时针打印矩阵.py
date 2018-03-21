# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下矩阵：
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 则依次打印出数字
# 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
from numpy.core.tests.test_mem_overlap import xrange


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        if n==1 and m==1:
            res=[matrix[0][0]]
            return res
        for o in xrange((min(m,n)+1)//2):
            [res.append(matrix[o][i]) for i in xrange(o,m-o)]
            [res.append(matrix[j][m-1-o]) for j in xrange(o,n-o) if matrix[j][m-1-o] not in res]
            [res.append(matrix[n-1-o][k]) for k in xrange(m-1-o,o-1,-1) if matrix[n-1-o][k] not in res]
            [res.append(matrix[l][o]) for l in xrange(n-1-o,o-1,-1) if matrix[l][o] not in res]
        return res

