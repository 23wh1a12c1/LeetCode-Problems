# JAVA



class Solution {
    public String makeFancyString(String s) {
        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray()) {
            int n = ans.length();
            if (n > 1 && ans.charAt(n - 1) == c && ans.charAt(n - 2) == c) {
                continue;
            }
            ans.append(c);
        }
        return ans.toString();
    }
}


   #############   OR


class Solution {
    public String makeFancyString(String s) {
        StringBuffer sb = new StringBuffer();
        int length = s.length();
        char prev = ' ';
        int count = 1;
        for (int i = 0; i < length; i++) {
            char curr = s.charAt(i);
            if (curr == prev)
                count++;
            else {
                count = 1;
                prev = curr;
            }
            if (count < 3)
                sb.append(curr);
        }
        return sb.toString();
    }
}





# PYTHON3



class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for c in s:
            if len(ans) > 1 and ans[-1] == ans[-2] == c:
                continue
            ans.append(c)
        return ''.join(ans)


############


class Solution:
    def makeFancyString(self, s: str) -> str:
        deque = collections.deque()
        
        for c in s:
            deque.append(c)
            
            while len(deque) >= 3 and deque[-1] == deque[-2] == deque[-3]:
                deque.pop()
        
        return "".join(deque)






# C++

class Solution {
public:
    string makeFancyString(string s) {
        int i = 0, j = 0, N = s.size();
        while (i < N) {
            int start = i;
            while (i < N && s[i] == s[start]) {
                if (i - start < 2) s[j++] = s[i];
                ++i;
            }
        }
        s.resize(j);
        return s;
    }
};








