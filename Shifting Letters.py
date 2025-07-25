##########    JAVA


class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] c = s.toCharArray();
        int n = c.length;
        long totalShifts = 0;

        for(int i=n-1;i>=0;i--) {
            totalShifts = (totalShifts +  shifts[i]) % 26;
            c[i] = (char)((c[i] - 'a' + totalShifts) % 26 + 'a');
        }
        return new String(c);
    }
}

        #############
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] cs = s.toCharArray();
        int n = cs.length;
        long t = 0;
        for (int i = n - 1; i >= 0; --i) {
            t += shifts[i];
            int j = (int) ((cs[i] - 'a' + t) % 26);
            cs[i] = (char) ('a' + j);
        }
        return String.valueOf(cs);
    }
}





################################################              PYTHON3




class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n, t = len(s), 0
        s = list(s)
        for i in range(n - 1, -1, -1):
            t += shifts[i]
            j = (ord(s[i]) - ord('a') + t) % 26
            s[i] = ascii_lowercase[j]
        return ''.join(s)








#########     C++



class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        long long t = 0;
        int n = s.size();
        for (int i = n - 1; ~i; --i) {
            t += shifts[i];
            int j = (s[i] - 'a' + t) % 26;
            s[i] = 'a' + j;
        }
        return s;
    }
};








