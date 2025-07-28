#########    PYTHON3



class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = ans = 0
        for x in nums:
            mx |= x

        def dfs(i, t):
            nonlocal mx, ans
            if i == len(nums):
                if t == mx:
                    ans += 1
                return
            dfs(i + 1, t)
            dfs(i + 1, t | nums[i])

        dfs(0, 0)
        return ans

                  #######

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mmax = float('-inf')
        
        for mask in range(1, 1 << n):
            s = 0
            for j in range(n):
                if (mask >> j) & 1:
                    s |= nums[j]

            mp[s] += 1
            mmax = max(mmax, s)

        return mp[mmax]
                             ###########


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = ans = 0
        for x in nums:
            mx |= x

        def dfs(i, t):
            nonlocal mx, ans
            if i == len(nums):
                if t == mx:
                    ans += 1
                return
            dfs(i + 1, t)
            dfs(i + 1, t | nums[i])

        dfs(0, 0)
        return ans

############

# 2044. Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mmax = float('-inf')
        
        for mask in range(1, 1 << n):
            s = 0
            for j in range(n):
                if (mask >> j) & 1:
                    s |= nums[j]

            mp[s] += 1
            mmax = max(mmax, s)

        return mp[mmax]




#########    JAVA






class Solution {
    private int mx;
    private int ans;
    private int[] nums;

    public int countMaxOrSubsets(int[] nums) {
        mx = 0;
        for (int x : nums) {
            mx |= x;
        }
        this.nums = nums;
        dfs(0, 0);
        return ans;
    }

    private void dfs(int i, int t) {
        if (i == nums.length) {
            if (t == mx) {
                ++ans;
            }
            return;
        }
        dfs(i + 1, t);
        dfs(i + 1, t | nums[i]);
    }
}



                  #####
class Solution {
    private int mx;
    private int ans;
    private int[] nums;

    public int countMaxOrSubsets(int[] nums) {
        mx = 0;
        for (int x : nums) {
            mx |= x;
        }
        this.nums = nums;
        dfs(0, 0);
        return ans;
    }

    private void dfs(int i, int t) {
        if (i == nums.length) {
            if (t == mx) {
                ++ans;
            }
            return;
        }
        dfs(i + 1, t);
        dfs(i + 1, t | nums[i]);
    }
}







#######   C++


class Solution {
public:
    int countMaxOrSubsets(vector<int>& A) {
        int goal = 0, N = A.size(), ans = 0;
        for (int n : A) goal |= n;
        for (int m = 1; m < 1 << N; ++m) {
            int x = 0;
            for (int i = 0; i < N; ++i) {
                if (m >> i & 1) x |= A[i];
            }
            if (x == goal) ++ans;
        }
        return ans;
    }
};

                ##########
// Time: O(2^N)
// Space: O(2^N)
class Solution {
public:
    int countMaxOrSubsets(vector<int>& A) {
        int goal = 0, N = A.size(), ans = 0;
        vector<int> dp(1 << N);
        for (int n : A) goal |= n;
        for (int m = 1; m < 1 << N; ++m) {
            int lowbit = m & -m;
            dp[m] = dp[m - lowbit] | A[__builtin_ctz(lowbit)];
            if (dp[m] == goal) ++ans;
        }
        return ans;
    }
};







