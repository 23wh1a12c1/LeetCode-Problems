####   PYTHON3


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        i = j = maxCnt = 0
        while i < len(s):
            counter[ord(s[i]) - ord('A')] += 1
            maxCnt = max(maxCnt, counter[ord(s[i]) - ord('A')])
            if i - j + 1 > maxCnt + k:
                counter[ord(s[j]) - ord('A')] -= 1
                j += 1
            i += 1
        return i - j


                  ###

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = max_count = 0
        res = 0

        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            max_count = max(max_count, freq[c])

            # If window is invalid, shrink from the left
            while (right - left + 1) - max_count > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res





######     JAVA


class Solution {
    public int characterReplacement(String s, int k) {
        int[] counter = new int[26];
        int i = 0;
        int j = 0;
        for (int maxCnt = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            ++counter[c - 'A'];
            maxCnt = Math.max(maxCnt, counter[c - 'A']);
            if (i - j + 1 - maxCnt > k) {
                --counter[s.charAt(j) - 'A'];
                ++j;
            }
        }
        return i - j;
    }
}



#####   C++


class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> counter(26);
        int i = 0, j = 0, maxCnt = 0;
        for (char& c : s) {
            ++counter[c - 'A'];
            maxCnt = max(maxCnt, counter[c - 'A']);
            if (i - j + 1 > maxCnt + k) {
                --counter[s[j] - 'A'];
                ++j;
            }
            ++i;
        }
        return i - j;
    }
};








