#######  PYTHON3



from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        xor = [0] * n
        time = 0
        in_time = [0] * n
        out_time = [0] * n

        # First DFS to calculate xor of each subtree
        def dfs(u, p):
            nonlocal time
            xor[u] = nums[u]
            parent[u] = p
            in_time[u] = time
            time += 1
            for v in graph[u]:
                if v == p:
                    continue
                dfs(v, u)
                xor[u] ^= xor[v]
            out_time[u] = time
            time += 1

        dfs(0, -1)
        total = xor[0]
        ans = float('inf')

        # Check if u is in subtree of v
        def is_in_subtree(u, v):
            return in_time[v] <= in_time[u] <= out_time[v]

        # Try every pair of edges (represented by child node)
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = i, j
                if is_in_subtree(a, b):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = total ^ xor[b]
                elif is_in_subtree(b, a):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = total ^ xor[a]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = total ^ xor[a] ^ xor[b]
                max_val = max(x, y, z)
                min_val = min(x, y, z)
                ans = min(ans, max_val - min_val)

        return ans


                    ###################

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def dfs(i, fa, x):
            res = nums[i]
            for j in g[i]:
                if j != fa and j != x:
                    res ^= dfs(j, i, x)
            return res

        def dfs2(i, fa, x):
            nonlocal s, s1, ans
            res = nums[i]
            for j in g[i]:
                if j != fa and j != x:
                    a = dfs2(j, i, x)
                    res ^= a
                    b = s1 ^ a
                    c = s ^ s1
                    t = max(a, b, c) - min(a, b, c)
                    ans = min(ans, t)
            return res

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        s = 0
        for v in nums:
            s ^= v
        n = len(nums)
        ans = inf
        for i in range(n):
            for j in g[i]:
                s1 = dfs(i, -1, j)
                dfs2(i, -1, j)
        return ans









#######################################                JAVA




class Solution {
    private int s;
    private int s1;
    private int n;
    private int ans = Integer.MAX_VALUE;
    private int[] nums;
    private List<Integer>[] g;

    public int minimumScore(int[] nums, int[][] edges) {
        n = nums.length;
        g = new List[n];
        this.nums = nums;
        Arrays.setAll(g, k -> new ArrayList<>());
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            g[a].add(b);
            g[b].add(a);
        }
        for (int v : nums) {
            s ^= v;
        }
        for (int i = 0; i < n; ++i) {
            for (int j : g[i]) {
                s1 = dfs(i, -1, j);
                dfs2(i, -1, j);
            }
        }
        return ans;
    }

    private int dfs(int i, int fa, int x) {
        int res = nums[i];
        for (int j : g[i]) {
            if (j != fa && j != x) {
                res ^= dfs(j, i, x);
            }
        }
        return res;
    }

    private int dfs2(int i, int fa, int x) {
        int res = nums[i];
        for (int j : g[i]) {
            if (j != fa && j != x) {
                int a = dfs2(j, i, x);
                res ^= a;
                int b = s1 ^ a;
                int c = s ^ s1;
                int t = Math.max(Math.max(a, b), c) - Math.min(Math.min(a, b), c);
                ans = Math.min(ans, t);
            }
        }
        return res;
    }
}





###########################     C++



class Solution {
public:
    vector<int> nums;
    int s;
    int s1;
    int n;
    int ans = INT_MAX;
    vector<vector<int>> g;

    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        n = nums.size();
        g.resize(n, vector<int>());
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            g[a].push_back(b);
            g[b].push_back(a);
        }
        for (int& v : nums) s ^= v;
        this->nums = nums;
        for (int i = 0; i < n; ++i) {
            for (int j : g[i]) {
                s1 = dfs(i, -1, j);
                dfs2(i, -1, j);
            }
        }
        return ans;
    }

    int dfs(int i, int fa, int x) {
        int res = nums[i];
        for (int j : g[i])
            if (j != fa && j != x) res ^= dfs(j, i, x);
        return res;
    }

    int dfs2(int i, int fa, int x) {
        int res = nums[i];
        for (int j : g[i])
            if (j != fa && j != x) {
                int a = dfs2(j, i, x);
                res ^= a;
                int b = s1 ^ a;
                int c = s ^ s1;
                int t = max(max(a, b), c) - min(min(a, b), c);
                ans = min(ans, t);
            }
        return res;
    }
};

















