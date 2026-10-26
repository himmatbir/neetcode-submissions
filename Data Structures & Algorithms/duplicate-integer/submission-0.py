class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet: set[int]= set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False

        