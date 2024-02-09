# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(len(nums))
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i == j) or (i > j):
                    continue
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
                # print(i, nums[i], j, nums[j], nums[i]+nums[j])
