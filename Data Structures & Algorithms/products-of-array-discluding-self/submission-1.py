class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1,len(nums)):
            left.append(left[-1]*nums[i-1])
        # print(left)
        right = [1]
        for i in range(len(nums)-2,-1,-1):
            # print(nums[i])
            right.insert(0,right[0]*(nums[i+1]))
        # print(right)
        res = []
        for i,j in zip(left,right):
            res.append(i*j)
        return res
