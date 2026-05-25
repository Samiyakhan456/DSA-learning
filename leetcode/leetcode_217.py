# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False