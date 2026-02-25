class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i in range (len(nums)):
            for n in range (len(nums)):
                if nums[i] + nums[n] == target and i != n:
                    return(i,n)
        