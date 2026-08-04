class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1=[]
        for i,num in enumerate(nums):
            nums1.append([num,i])       #copy of list

        nums1.sort()
        i,j=0,len(nums)-1
        while j>i:
            sum=nums1[i][0]+nums1[j][0]
            if sum==target:
                return [nums1[i][1],nums1[j][1]]
            elif sum < target:
                i=i+1
            else:
                j=j-1
                
        return []
        