class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            if not idx:
                idx[nums[i]]=i
                continue
            if target-nums[i] in idx:
                return [idx[target-nums[i]],i]
            idx[nums[i]]=i