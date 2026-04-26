class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1p = m - 1
        nums2p = n - 1

        for right in range(len(nums1) - 1, -1, -1):
            if nums1p >= 0 and nums2p >= 0 and nums1[nums1p] >= nums2[nums2p]:
                nums1[right], nums1[nums1p] = nums1[nums1p], nums1[right]
                nums1p -= 1
            elif nums2p >= 0:
                nums1[right] = nums2[nums2p]
                nums2p -= 1