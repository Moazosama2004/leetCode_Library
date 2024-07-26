class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []

        for index in range(len(nums)) :
            if index == 0 :
                running_sum.append(nums[index])
            else :
                running_sum.append(running_sum[index-1] + nums[index])
        return running_sum
        