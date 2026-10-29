class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int]= []
        numMap: dict[int, int]= {}
        for index in range(len(nums)):
            if target-nums[index] in numMap:
                result.append(numMap[target-nums[index]])
                result.append(index)
                return result
            else:
                numMap[nums[index]]= index
        