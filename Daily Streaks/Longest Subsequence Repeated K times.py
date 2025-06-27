# PYTHON3


from collections import deque, Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_k_repeated_subsequence(pattern: str) -> bool:
            i = j = match_count = 0
            while i < len(s) and match_count < k:
                if s[i] == pattern[j]:
                    j += 1
                    if j == len(pattern):
                        match_count += 1
                        j = 0
                i += 1
            return match_count == k

        # Step 1: Frequency pruning - only keep characters that appear at least k times
        freq = Counter(s)
        valid_chars = [c for c in freq if freq[c] >= k]
        valid_chars.sort()  # ensure lexicographic order for BFS
        s = ''.join([c for c in s if c in valid_chars])

        # Step 2: BFS to build valid patterns
        q = deque([""])
        ans = ""

        while q:
            curr = q.popleft()
            for c in valid_chars:
                candidate = curr + c
                if is_k_repeated_subsequence(candidate):
                    if len(candidate) > len(ans) or (len(candidate) == len(ans) and candidate > ans):
                        ans = candidate
                    q.append(candidate)

        return ans











# CPP


---->  BFS

class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        queue<string> q{ {""} };
        unordered_set<string> valid{""};
        string ans;
        while (q.size()) {
            auto x = q.front();
            q.pop();
            for (char c = 'a'; c <= 'z'; ++c) {
                auto y = x + c;
                auto suffix = y.substr(1);
                if (valid.count(suffix) == 0) continue; // suffix must be also valid.
                int matched = 0, i = 0, j = 0;
                for (; i < s.size() && matched < k; ++i) {
                    if (s[i] == y[j]) ++j;
                    if (j == y.size()) j = 0, ++matched;
                }
                if (matched == k) {
                    ans = y;
                    q.push(y);
                    valid.insert(y);
                }
            }
        }
        return ans;
    }
};


#  CPP
---->    DFS

class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        int cnt[26] = {};
        string ans;
        auto isSubsequence = [&]() {
            int matched = 0, i = 0, j = 0, M = s.size(), N = ans.size();
            for (; i < M && matched < k; ++i) {
                if (s[i] == ans[j]) ++j;
                if (j == N) j = 0, matched++;
            }
            return matched == k;
        };
        function<bool(int)> dfs = [&](int len) {
            if (ans.size() == len) return true;
            for (int i = 25; i >= 0; --i) {
                if (cnt[i] == 0) continue;
                ans.push_back('a' + i);
                if (isSubsequence() && dfs(len)) return true;
                ans.pop_back();
            }
            return false;
        };
        for (char c : s) cnt[c - 'a']++;
        for (int &n : cnt) n /= k;
        int j = 0;
        for (int i = 0; i < s.size(); ++i) { // remove the characters in `s` that doesn't occurrs `k` times.
            if (cnt[s[i] - 'a']) s[j++] = s[i];
        }
        s.resize(j);
        for (int len = 7; len >= 1; --len) {
            if (dfs(len)) return ans;
        }
        return "";
    }
};
