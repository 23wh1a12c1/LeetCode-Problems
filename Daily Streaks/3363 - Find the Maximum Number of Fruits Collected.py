####      C++


class Solution {
    using ll = long long;
    static constexpr int INF = std::numeric_limits<int>::max();

    // DFS + Memoization
    int dfs(const vector<vector<int>>& fruits,
            int row, int col, int moves,
            vector<vector<int>>& mem,
            const vector<pair<int,int>>& dirs)
    {
        int n = fruits.size();
        if (row == n-1 && col == n-1)   //Reached target cell
            return moves == 0 ? 0 : INF;
        if (moves == 0 || row == col)   //Move NOT-allowed
            return INF;
        if (mem[row][col] != -1)        //Repeating Sub-problem
            return mem[row][col];

        ll max_fruits = -1;
        for (auto [delta_row, delta_col] : dirs) {
            int new_row = row + delta_row;
            int new_col = col + delta_col;
            if (new_row >= 0 && new_row < n && new_col >= 0 && new_col < n) {//Boundary check
                int val = dfs(fruits, new_row, new_col, moves-1, mem, dirs);
                if (val != INF)
                    max_fruits = max(max_fruits, (ll)val);
            }
        }
        return mem[row][col] = (max_fruits < 0 ? INF : fruits[row][col] + max_fruits);
    }

public:
    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int n = fruits.size();

        // Step-1: Collect fruits in the main diagonal
        ll first = 0;
        for (int i = 0; i < n; ++i)
            first += fruits[i][i];

        // Step-2: (2nd path: from top-right corner) only down-left/down/down-right
        vector<pair<int,int>> down_dirs = {{1,-1},{1,0},{1,1}};
        vector<vector<int>> mem(n, vector<int>(n, -1));
        int second = dfs(fruits, 0, n-1, n-1, mem, down_dirs);

        // 3) third path: only up-right/right/down-right
        vector<pair<int,int>> right_dirs = {{-1,1},{0,1},{1,1}};
        for (auto& row : mem) fill(row.begin(), row.end(), -1);
        int third = dfs(fruits, n-1, 0, n-1, mem, right_dirs);

        return first + second + third;
    }
};



####      JAVA



import java.util.*;

class Solution {
    private static final int INF = Integer.MAX_VALUE;
    private int n;
    private int[][] fruits;
    private int[][] memo;
    private List<int[]> dirs;

    // DFS + memoization
    private int dfs(int row, int col, int moves) {
        // Reached bottom-right?
        if (row == n - 1 && col == n - 1) {
            return (moves == 0) ? 0 : INF;
        }
        // No moves left or on main diagonal (forbidden)
        if (moves == 0 || row == col) {
            return INF;
        }
        if (memo[row][col] != -1) {
            return memo[row][col];
        }
        long best = -1;
        for (int[] d : dirs) {
            int nr = row + d[0], nc = col + d[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                int val = dfs(nr, nc, moves - 1);
                if (val != INF) {
                    best = Math.max(best, (long) val);
                }
            }
        }
        int result = (best < 0 ? INF : fruits[row][col] + (int) best);
        memo[row][col] = result;
        return result;
    }

    public int maxCollectedFruits(int[][] fruits) {
        this.n = fruits.length;
        this.fruits = fruits;

        // 1) Sum of main diagonal
        long first = 0;
        for (int i = 0; i < n; i++) {
            first += fruits[i][i];
        }

        // 2) Second path: from top-right to bottom-right (down-left/down/down-right)
        dirs = Arrays.asList(
            new int[]{1, -1},
            new int[]{1, 0},
            new int[]{1, 1}
        );
        memo = new int[n][n];
        for (int[] row : memo) Arrays.fill(row, -1);
        int second = dfs(0, n - 1, n - 1);

        // 3) Third path: from bottom-left to bottom-right (up-right/right/down-right)
        dirs = Arrays.asList(
            new int[]{-1, 1},
            new int[]{0, 1},
            new int[]{1, 1}
        );
        for (int[] row : memo) Arrays.fill(row, -1);
        int third = dfs(n - 1, 0, n - 1);

        return (int) (first + second + third);
    }
}



####    PYTHON3




from functools import lru_cache
from typing import List

INF = float('inf')

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # 1) Sum of main diagonal
        first = sum(fruits[i][i] for i in range(n))

        # Helper DFS with memoization
        def make_dfs(dirs):
            @lru_cache(None)
            def dfs(r: int, c: int, moves: int) -> int:
                # Reached bottom-right?
                if r == n - 1 and c == n - 1:
                    return 0 if moves == 0 else INF
                # No moves left or on main diagonal
                if moves == 0 or r == c:
                    return INF

                best = -1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        val = dfs(nr, nc, moves - 1)
                        if val != INF:
                            best = max(best, val)
                return INF if best < 0 else fruits[r][c] + best
            return dfs

        # 2) Second path: from top-right to bottom-right
        down_dirs = [(1, -1), (1, 0), (1, 1)]
        dfs_down = make_dfs(down_dirs)
        second = dfs_down(0, n - 1, n - 1)

        # 3) Third path: from bottom-left to bottom-right
        right_dirs = [(-1, 1), (0, 1), (1, 1)]
        dfs_right = make_dfs(right_dirs)
        third = dfs_right(n - 1, 0, n - 1)

        return first + second + third





