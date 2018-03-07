# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,
# 2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,
# 如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,
# 他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
# 上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
# LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。
class Solution:
    def IsContinuous(self, numbers):
        # 如果扑克牌为空，返回假
        if not numbers or len(numbers) < 5:
            return False
        # write code here
        numbers.sort()
        # 输出0的个数
        zero_num = 0
        for i in range(0, len(numbers)):
            if numbers[i] != 0:
                zero_num = i
                break
        # 输出gap的个数
        start = zero_num
        next = zero_num + 1
        end = len(numbers)
        gap_num = 0
        while next < end:
            # 如果出现对子的情况，一定不可能成为顺子
            if numbers[next] == numbers[start]:
                return False
            gap_num += numbers[next] - (numbers[start] + 1)
            start = next
            next += 1
        # 判断能够成为顺子
        if zero_num >= gap_num:
            return True
        return False
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return numbers
        new_list = [i for i in numbers if i > 0]
        new_list.sort()
        if len(new_list)==1:
            return True
        n = 0
        for j in range(len(new_list)-1):
            if (new_list[j+1] - new_list[j]) > 0:
                n += (new_list[j+1] - new_list[j])
            else:
                return False
        if n <= 4:
            return True
        else:
            return False