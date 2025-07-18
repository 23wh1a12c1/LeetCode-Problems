#  PYTHON3


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(c)
        return ''.join(ans)


############


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)
        
        for i, x in enumerate(s):
            if i in spaces:
                res.append(" ")
            
            res.append(x)
        
        return "".join(res)





# JAVA




class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0, j = 0; i < s.length(); i++) {
            if (j < spaces.length && i == spaces[j]) {
                sb.append(' ');
                j++;
            }
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}





#  C++


// Time: O(N + M) = O(N)
// Space: O(1) extra space
class Solution {
public:
    string addSpaces(string s, vector<int>& A) {
        string ans;
        ans.reserve(s.size() + A.size()); // Optional: pre-allocate enough space for the answer.
        int N = s.size(), j = 0, M = A.size(); // `A[j]` is the next index before which a space should be inserted
        for (int i = 0; i < N; ++i) {
            if (j < M && i == A[j]) { // If `i == A[j]`, we insert a space
                ans += ' ';
                ++j;
            }
            ans += s[i];
        }
        return ans;
    }
};













