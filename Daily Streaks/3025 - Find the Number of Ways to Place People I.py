###  PYTHON3


from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x ascending, y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0
        
        for i in range(n):
            x1, y1 = points[i]
            max_y = float('-inf')
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if y2 <= y1 and y2 > max_y:
                    ans += 1
                    max_y = y2
        return ans

# 🔽 Example usage
points = [[1, 4], [2, 3], [3, 2], [4, 1]]
solution = Solution()
print(solution.numberOfPairs(points))  # ✅ Output: 6


                ###   OR



class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for _, y2 in points[i + 1 :]:
                if max_y < y2 <= y1:
                    max_y = y2
                    ans += 1
        return ans






###   JAVA



class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        int ans = 0;
        int n = points.length;
        final int inf = 1 << 30;
        for (int i = 0; i < n; ++i) {
            int y1 = points[i][1];
            int maxY = -inf;
            for (int j = i + 1; j < n; ++j) {
                int y2 = points[j][1];
                if (maxY < y2 && y2 <= y1) {
                    maxY = y2;
                    ++ans;
                }
            }
        }
        return ans;
    }
}




###   C++

class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0] || (a[0] == b[0] && b[1] < a[1]);
        });
        int n = points.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int y1 = points[i][1];
            int maxY = INT_MIN;
            for (int j = i + 1; j < n; ++j) {
                int y2 = points[j][1];
                if (maxY < y2 && y2 <= y1) {
                    maxY = y2;
                    ++ans;
                }
            }
        }
        return ans;
    }
};
