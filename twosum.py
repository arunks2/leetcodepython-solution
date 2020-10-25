# problem statement: https://leetcode.com/problems/two-sum/

# solution 1 (Bad solution)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index, n in enumerate(nums):
#             for i in range(index+1, len(nums)):
#                 s = n + nums[i]
#                 if s == target:
#                     return [index, i]

Solution 2 (Much Better Solution)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        
        for i, n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            leftover = target - n
            if leftover in h:
                if i != h[leftover]:
                    return [i, h[leftover]]
                    


c