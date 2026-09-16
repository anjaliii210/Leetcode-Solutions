class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==0 : return 0
        if len(nums)==1 : return 1
        i=1  #to keep elements
        a=1 #for traversal
        curr=nums[0]
        while a<len(nums):
            if nums[a]==curr:
                a=a+1
            else:
                nums[i]=nums[a]
                curr=nums[a]
                i=i+1
                a=a+1
        return i   #return no of elements so +1
                
        