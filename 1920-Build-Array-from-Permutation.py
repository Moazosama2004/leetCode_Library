class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [nums[nums[index]] for index in range(len(nums))] 
        return ans
        