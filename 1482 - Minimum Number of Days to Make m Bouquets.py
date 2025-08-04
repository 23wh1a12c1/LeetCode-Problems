###  PYTHON3


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def check(day: int) -> bool:
            cnt = cur = 0
            for bd in bloomDay:
                cur = cur + 1 if bd <= day else 0
                if cur == k:
                    cnt += 1
                    cur = 0
            return cnt >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left



####  JAVA


class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if (m * k > bloomDay.length) {
            return -1;
        }
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int bd : bloomDay) {
            min = Math.min(min, bd);
            max = Math.max(max, bd);
        }
        int left = min, right = max;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (check(bloomDay, m, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean check(int[] bloomDay, int m, int k, int day) {
        int cnt = 0, cur = 0;
        for (int bd : bloomDay) {
            cur = bd <= day ? cur + 1 : 0;
            if (cur == k) {
                cnt++;
                cur = 0;
            }
        }
        return cnt >= m;
    }
}




####   C++


class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if (m * k > bloomDay.size()) {
            return -1;
        }
        int mi = INT_MIN, mx = INT_MAX;
        for (int& bd : bloomDay) {
            mi = min(mi, bd);
            mx = max(mx, bd);
        }
        int left = mi, right = mx;
        while (left < right) {
            int mid = left + right >> 1;
            if (check(bloomDay, m, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    bool check(vector<int>& bloomDay, int m, int k, int day) {
        int cnt = 0, cur = 0;
        for (int& bd : bloomDay) {
            cur = bd <= day ? cur + 1 : 0;
            if (cur == k) {
                ++cnt;
                cur = 0;
            }
        }
        return cnt >= m;
    }
};

