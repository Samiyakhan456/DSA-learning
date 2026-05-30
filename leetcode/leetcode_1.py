class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],index]
            seen[num] = index
            return [num, complement]
        #The enumerate() function in Python is used to 
        # iterate over an iterable while keeping track 
        # of both the index and the value
            
        