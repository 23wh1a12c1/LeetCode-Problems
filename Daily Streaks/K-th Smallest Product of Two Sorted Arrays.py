class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        A1, A2 = [-x for x in nums1 if x < 0][::-1], [x for x in nums1 if x >= 0]
        B1, B2 = [-x for x in nums2 if x < 0][::-1], [x for x in nums2 if x >= 0]
        
        neg = len(A1) * len(B2) + len(A2) * len(B1)
        if k > neg:
            k -= neg
            s = 1
        else:
            k = neg - k + 1
            B1, B2 = B2, B1
            s = -1
        
        def count(A, B, t):
            res = 0
            
            j = len(B) - 1
            for x in A:
                while j >= 0 and x * B[j] > t:
                    j -= 1
                
                res += j + 1
            
            return res
        
        left, right = 0, 10 ** 10
        
        while left < right:
            mid = left + (right - left) // 2
            
            if count(A1, B1, mid) + count(A2, B2, mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left * s
