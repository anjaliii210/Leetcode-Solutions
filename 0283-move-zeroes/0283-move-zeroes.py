class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos=pos+1
        
        
        #fill all leftover positions with 0
        while pos<len(nums):
            nums[pos]=0
            pos=pos+1

                


        