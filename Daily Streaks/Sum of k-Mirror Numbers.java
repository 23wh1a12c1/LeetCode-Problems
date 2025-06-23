# JAVA


class Solution {
    long getPalindrome(int half, boolean odd) {
        long n = half, tmp = half;
        if (odd) tmp /= 10;
        while (tmp > 0) {
            n = n * 10 + tmp % 10;
            tmp /= 10;
        }
        return n;
    }

    boolean isPalindromeBaseK(long n, int k) {
        StringBuilder s = new StringBuilder();
        while (n > 0) {
            s.append(n % k);
            n /= k;
        }
        int i = 0, j = s.length() - 1;
        while (i < j && s.charAt(i) == s.charAt(j)) {
            i++; j--;
        }
        return i >= j;
    }

    public long kMirror(int k, int n) {
        long ans = 0;
        for (int len = 1; ; len++) {
            int start = (int)Math.pow(10, len - 1);
            int end = (int)Math.pow(10, len);

            for (int half = start; half < end; half++) {
                long pal = getPalindrome(half, true);
                if (isPalindromeBaseK(pal, k)) {
                    ans += pal;
                    if (--n == 0) return ans;
                }
            }

            for (int half = start; half < end; half++) {
                long pal = getPalindrome(half, false);
                if (isPalindromeBaseK(pal, k)) {
                    ans += pal;
                    if (--n == 0) return ans;
                }
            }
        }
    }
}



# CPP


class Solution {
    long long getPalindrome(int half, bool odd) {
        long long n = half, tmp = half;
        if (odd) tmp /= 10;
        while (tmp) {
            n = n * 10 + tmp % 10;
            tmp /= 10;
        }
        return n;
    }
    bool isPalindromeBaseK(long long n, int k) {
        string s;
        while (n) {
            s += '0' + n % k;
            n /= k;
        }
        int i = 0, j = s.size() - 1;
        while (i < j && s[i] == s[j]) ++i, --j;
        return i >= j;
    }
public:
    long long kMirror(int k, int n) {
        long long ans = 0;
        for (int len = 1; true; ++len) {
            for (int half = pow(10, len - 1); half < pow(10, len); ++half) {
                auto pal = getPalindrome(half, true);
                if (isPalindromeBaseK(pal, k)) {
                    ans += pal;
                    if (--n == 0) return ans;
                }
            }
            for (int half = pow(10, len - 1); half < pow(10, len); ++half) {
                auto pal = getPalindrome(half, false);
                if (isPalindromeBaseK(pal, k)) {
                    ans += pal;
                    if (--n == 0) return ans;
                }
            }
        }
    }
};




                       #  OR


class Solution {
    long getPalindrome(int half, bool odd) {
        long pal = half;
        if (odd) half /= 10;
        for (; half; half /= 10) pal = pal * 10 + half % 10;
        return pal;
    }
    bool isPalindromeBaseK(long n, int k) {
        long mul = 1;
        while (mul * k <= n) mul *= k;
        for (; n; mul /= k * k) {
            if (n / mul != n % k) return false;
            n = (n - (n / mul) * mul - n % k) / k;
        }
        return true;
    }
public:
    long long kMirror(int k, int n) {
        long long ans = 0;
        for (int len = 1; true; ++len) {
            int begin = pow(10, (len - 1) / 2), end = pow(10, (len + 1) / 2);
            for (int half = begin; half < end; ++half) {
                long pal = getPalindrome(half, len % 2);
                if (isPalindromeBaseK(pal, k)) {
                    ans += pal;
                    if (--n == 0) return ans;
                }
            }
        }
    }
};
