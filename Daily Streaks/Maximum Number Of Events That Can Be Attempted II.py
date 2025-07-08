# PYTHON3



class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dfs(i: int, k: int) -> int:
            if i >= len(events):
                return 0
            _, ed, val = events[i]
            ans = dfs(i + 1, k)
            if k:
                j = bisect_right(events, ed, lo=i + 1, key=lambda x: x[0])
                ans = max(ans, dfs(j, k - 1) + val)
            return ans

        events.sort()
        return dfs(0, k)







# JAVA





class Solution {
    private int[][] events;
    private int[][] f;
    private int n;

    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, (a, b) -> a[0] - b[0]);
        this.events = events;
        n = events.length;
        f = new int[n][k + 1];
        return dfs(0, k);
    }

    private int dfs(int i, int k) {
        if (i >= n || k <= 0) {
            return 0;
        }
        if (f[i][k] != 0) {
            return f[i][k];
        }
        int j = search(events, events[i][1], i + 1);
        int ans = Math.max(dfs(i + 1, k), dfs(j, k - 1) + events[i][2]);
        return f[i][k] = ans;
    }

    private int search(int[][] events, int x, int lo) {
        int l = lo, r = n;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (events[mid][0] > x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}






#   C++




class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        ranges::sort(events);
        int n = events.size();
        int f[n][k + 1];
        memset(f, 0, sizeof(f));
        auto dfs = [&](this auto&& dfs, int i, int k) -> int {
            if (i >= n || k <= 0) {
                return 0;
            }
            if (f[i][k] > 0) {
                return f[i][k];
            }

            int ed = events[i][1], val = events[i][2];
            vector<int> t = {ed};

            int p = upper_bound(events.begin() + i + 1, events.end(), t,
                        [](const auto& a, const auto& b) { return a[0] < b[0]; })
                - events.begin();

            f[i][k] = max(dfs(i + 1, k), dfs(p, k - 1) + val);
            return f[i][k];
        };

        return dfs(0, k);
    }
};
