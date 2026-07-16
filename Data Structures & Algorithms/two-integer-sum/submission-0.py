class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for index,number in enumerate(nums):
            difference=target-number
            if difference in prev:
                return [prev[difference],index]
            prev[number]=index