class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            # print(m,l,r)
            if nums[m] <= nums[l] <= nums[m - 1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return 0
    
res = Solution()
print(res.findMin([3,1,2]))