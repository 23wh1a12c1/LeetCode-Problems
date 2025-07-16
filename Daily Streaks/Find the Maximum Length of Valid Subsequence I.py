# PYTHON3



class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        a = [[0]*2 for _ in range(2)]

        for num in nums:
            for num1 in range(2):
                a[num % 2][num1] = a[num1][num % 2] + 1
        return max(map(max,a))




# JAVA




class Solution {
  public int maximumLength(int[] nums) {
    int[][] dp = new int[k][k];

    for (final int x : nums)
      for (int y = 0; y < 2; ++y)
        dp[x % 2][y] = dp[y][x % 2] + 1;

    return Arrays.stream(dp).flatMapToInt(Arrays::stream).max().getAsInt();
  }
}



# C++


class Solution {
 public:
  int maximumLength(vector<int>& nums) {
    vector<vector<int>> dp(2, vector<int>(2));

    for (const int x : nums)
      for (int y = 0; y < 2; ++y)
        dp[x % 2][y] = dp[y][x % 2] + 1;

    return accumulate(dp.begin(), dp.end(), 0,
                      [](int acc, const vector<int>& row) {
      return max(acc, ranges::max(row));
    });
  }
};


















