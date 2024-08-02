class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_double_digit = 0
        sum_single_digit = 0

        for num in nums:
            if num > 9:
                sum_double_digit += num
            else:
                sum_single_digit += num
        return  abs(sum_single_digit - sum_double_digit) != 0 

            