class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:



        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n12_is_odd=((len(nums1)+len(nums2))%2!=0)
        mid_idx=(len(nums1)+len(nums2)+1)//2

        def get_mean(eles:[]):
            if n12_is_odd:
                return max(eles[0], eles[1])
            else:
                target_ele = sorted(eles)[1:3]
                return sum(target_ele) / 2

        left = 0
        right = len(nums1) - 1

        while left<=right+1:
            n1_idx=(left+right+1)//2


            n2_idx=mid_idx-n1_idx
            n1_left_val=nums1[n1_idx-1] if n1_idx>0 else -1111111111
            n1_right_val=nums1[n1_idx] if n1_idx<len(nums1)  else 111111111

            n2_left_val=nums2[n2_idx-1] if n2_idx>0  else -111111111
            n2_right_val=nums2[n2_idx] if n2_idx<len(nums2)  else 111111111

            if (n1_right_val>=n2_left_val and n2_right_val>=n1_left_val):
                return get_mean([n1_left_val, n2_left_val, n1_right_val, n2_right_val])
            elif n1_idx < 0 or n1_idx >= len(nums1):
                return get_mean([n1_left_val, n2_left_val, n1_right_val, n2_right_val])
            elif n1_right_val<=n2_left_val:
                left=n1_idx+1
            elif n1_left_val>=n2_right_val:
                right=n1_idx-1


res=Solution().findMedianSortedArrays([1,2],[1,1])

print(res)