class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for index in range(len(nums)) :
            freq = bin(index).split('b')[-1].count('1')
            if freq == k :
                sum += nums[index]
        return  sum