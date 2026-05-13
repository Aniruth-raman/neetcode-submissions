class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        res = []
        for i in range(n):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                target = -sorted_nums[i]
                if sorted_nums[j] + sorted_nums[k] == target:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while sorted_nums[j] == sorted_nums[j - 1] and j < k:
                        j += 1
                elif sorted_nums[j] + sorted_nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res
