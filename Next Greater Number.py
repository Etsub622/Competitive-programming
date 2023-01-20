class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        for i in range(len(nums1)):
            temp = nums2.index(nums1[i])
            new_arr = nums2[temp:]

            for j in range(1,len(new_arr)):
                if new_arr[j] > nums1[i]:
                    res[i] = new_arr[j]
                    break
        return res
