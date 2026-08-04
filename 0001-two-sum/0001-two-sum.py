class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map={}   #value: index

        for i,n in enumerate(nums):   #checks if complement exists as value in map
            diff=target-n
            if diff in map:
                return [map[diff],i]
            map[n]=i

        