####    PYTHON3


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        bins, rep = [], 1
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2

        ans = []
        for left, right in queries:
            cur = 1
            for i in range(left, right + 1):
                cur = cur * bins[i] % mod
            ans.append(cur)
        return ans


####   JAVA


class Solution {

    private static final int MOD = 1000000007;

    public int[] productQueries(int n, int[][] queries) {
        List<Integer> bins = new ArrayList<>();
        int rep = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                bins.add(rep);
            }
            n /= 2;
            rep *= 2;
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long cur = 1;
            int start = queries[i][0];
            int end = queries[i][1];
            for (int j = start; j <= end; j++) {
                cur = (cur * bins.get(j)) % MOD;
            }
            ans[i] = (int) cur;
        }
        return ans;
    }
}




#####   C++



class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> bins;
        int rep = 1;
        while (n) {
            if (n % 2 == 1) {
                bins.push_back(rep);
            }
            n /= 2;
            rep *= 2;
        }

        vector<int> ans;
        for (const auto& query : queries) {
            int cur = 1;
            for (int i = query[0]; i <= query[1]; ++i) {
                cur = static_cast<long long>(cur) * bins[i] % mod;
            }
            ans.push_back(cur);
        }
        return ans;
    }

private:
    static constexpr int mod = 1000000007;
};
