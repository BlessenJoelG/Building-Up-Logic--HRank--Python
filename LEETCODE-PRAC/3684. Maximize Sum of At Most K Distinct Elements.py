class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(set(nums),reverse = True)
        if len(nums)<k:
            return nums
        else:
            return nums[0:k]