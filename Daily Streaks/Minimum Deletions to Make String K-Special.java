# Java


class Solution {
    private List<Integer> nums = new ArrayList<>();

    public int minimumDeletions(String word, int k) {
        int[] freq = new int[26];
        int n = word.length();
        for (int i = 0; i < n; ++i) {
            ++freq[word.charAt(i) - 'a'];
        }
        for (int v : freq) {
            if (v > 0) {
                nums.add(v);
            }
        }
        int ans = n;
        for (int i = 0; i <= n; ++i) {
            ans = Math.min(ans, f(i, k));
        }
        return ans;
    }

    private int f(int v, int k) {
        int ans = 0;
        for (int x : nums) {
            if (x < v) {
                ans += x;
            } else if (x > v + k) {
                ans += x - v - k;
            }
        }
        return ans;
    }
}



# Python3


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def f(v: int) -> int:
            ans = 0
            for x in nums:
                if x < v:
                    ans += x
                elif x > v + k:
                    ans += x - v - k
            return ans

        nums = Counter(word).values()
        return min(f(v) for v in range(len(word) + 1))



# cpp


class Solution {
public:
    int minimumDeletions(string word, int k) {
        int freq[26]{};
        for (char& c : word) {
            ++freq[c - 'a'];
        }
        vector<int> nums;
        for (int v : freq) {
            if (v) {
                nums.push_back(v);
            }
        }
        int n = word.size();
        int ans = n;
        auto f = [&](int v) {
            int ans = 0;
            for (int x : nums) {
                if (x < v) {
                    ans += x;
                } else if (x > v + k) {
                    ans += x - v - k;
                }
            }
            return ans;
        };
        for (int i = 0; i <= n; ++i) {
            ans = min(ans, f(i));
        }
        return ans;
    }
};




