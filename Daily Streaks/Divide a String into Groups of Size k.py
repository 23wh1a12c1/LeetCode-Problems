# PYTHON


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i : i + k].ljust(k, fill) for i in range(0, len(s), k)]


# JAVA


class Solution {
    public String[] divideString(String s, int k, char fill) {
        int n = s.length();
        String[] ans = new String[(n + k - 1) / k];
        if (n % k != 0) {
            s += String.valueOf(fill).repeat(k - n % k);
        }
        for (int i = 0; i < ans.length; ++i) {
            ans[i] = s.substring(i * k, (i + 1) * k);
        }
        return ans;
    }
}


# CPP


class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.size();
        if (n % k)
            for (int i = 0; i < k - n % k; ++i) s.push_back(fill);
        vector<string> ans;
        for (int i = 0; i < s.size() / k; ++i) ans.push_back(s.substr(i * k, k));
        return ans;
    }
};
