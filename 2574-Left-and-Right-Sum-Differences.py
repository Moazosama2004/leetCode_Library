class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []

        right = sum(nums)
        left = 0

        for index in range(len(nums)) :
            right -= nums[index]
            total_sum = abs(left - right)
            answer.append(total_sum)
            left += nums[index]
        return answer