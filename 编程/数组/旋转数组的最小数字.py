# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
# -*- coding:utf-8 -*-
class Solution:

    def minNumberInRotateArray(self,rotateArray):
        left = 0  # 左侧的指针
        right = len(rotateArray) - 1  # 右侧的指针
        mid = 0  # 中间的指针
        while rotateArray[left] >= rotateArray[right]:
            # 当两个指针走到挨着的位置时，即right - left == 1,right就是最小数了
            if right - left == 1:
                mid = right
                break
            mid = left + (int)((right - left) / 2)
            # 如果中间位置的数既等于left位置的数又等于right位置的数
            if rotateArray[left] == rotateArray[mid] and rotateArray[right] == rotateArray[mid]:
                return self.minInorder(rotateArray, left, right)
                # 若中间位置的数大于左边位置的数，说明最小的数在mid位置的右边中，让left走到mid的位置
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
                # 若中间位置的数小于右边指针位置的数，说明最小的数在mid位置的左边，让right走到mid的位置
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
        return rotateArray[mid]
        # 顺序查找数组里的最小值

    def minInorder(self,rotateArray, left, right):
        minNum = rotateArray[left]
        length = right - left
        for i in range(length):
            if rotateArray[left + i] < minNum:
                minNum = rotateArray[left + i]
        return minNum