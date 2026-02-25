class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        danhsachsohang ={}
        for i,n in enumerate (nums):
            complement = target - n
            if complement in danhsachsohang:
                return (danhsachsohang[complement],i)
            else:
                danhsachsohang[n] = i