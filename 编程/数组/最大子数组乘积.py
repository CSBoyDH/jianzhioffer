def maxproduct(nums):

    n = len(nums)
    CurMax = nums[0]
    CurMin = nums[0]
    res = nums[0]
    for i in range(1,n):
        mx = CurMax
        mn = CurMin
        CurMax =max(max(nums[i],mx*nums[i]),mn*nums[i])
        CurMin = min(min(nums[i], mx * nums[i]), mn * nums[i])
        res = max(res,CurMax)
    return res
print(maxproduct([-2.5,4,0,3,0.5,8,-1]))
