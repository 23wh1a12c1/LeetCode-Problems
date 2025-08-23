####   PYTHON3



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        self.nums1, self.nums2 = nums1, nums2
        self.m, self.n = len(nums1), len(nums2)

        a = self.kth(0, 0, (self.m + self.n + 1) // 2)
        b = self.kth(0, 0, (self.m + self.n + 2) // 2)
        return (a + b) / 2.0

    def kth(self, i, j, k):
        # If one array is exhausted
        if i >= self.m:
            return self.nums2[j + k - 1]
        if j >= self.n:
            return self.nums1[i + k - 1]

        # Base case: smallest k
        if k == 1:
            return min(self.nums1[i], self.nums2[j])

        p = k // 2
        x = self.nums1[i + p - 1] if i + p - 1 < self.m else float('inf')
        y = self.nums2[j + p - 1] if j + p - 1 < self.n else float('inf')

        if x < y:
            return self.kth(i + p, j, k - p)
        else:
            return self.kth(i, j + p, k - p)




#####  JAVA


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);

        int m = nums1.length, n = nums2.length, left = 0, right = m, half = (m + n + 1) / 2;

        while (left <= right) {
            int i = (left + right) / 2, j = half - i;
            int l1 = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int r1 = (i == m) ? Integer.MAX_VALUE : nums1[i];
            int l2 = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int r2 = (j == n) ? Integer.MAX_VALUE : nums2[j];

            if (l1 <= r2 && l2 <= r1) {
                if ((m + n) % 2 == 1) return Math.max(l1, l2);
                return (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
            } 
            if (l1 > r2) right = i - 1; 
            else left = i + 1;
        }
        return 0.0; 
    }
}






                                            ##   OR
class Solution {
    private int m;
    private int n;
    private int[] nums1;
    private int[] nums2;

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        m = nums1.length;
        n = nums2.length;
        this.nums1 = nums1;
        this.nums2 = nums2;
        int a = f(0, 0, (m + n + 1) / 2);
        int b = f(0, 0, (m + n + 2) / 2);
        return (a + b) / 2.0;
    }

    private int f(int i, int j, int k) {
        if (i >= m) {
            return nums2[j + k - 1];
        }
        if (j >= n) {
            return nums1[i + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[i], nums2[j]);
        }
        int p = k / 2;
        int x = i + p - 1 < m ? nums1[i + p - 1] : 1 << 30;
        int y = j + p - 1 < n ? nums2[j + p - 1] : 1 << 30;
        return x < y ? f(i + p, j, k - p) : f(i, j + p, k - p);
    }
}
