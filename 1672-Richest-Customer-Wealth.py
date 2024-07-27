class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for index in range(len(accounts)):
            wealthy = sum(accounts[index])
            if index == 0 :
                max = wealthy
            if wealthy > max:
                    max = wealthy
        
        return max
        