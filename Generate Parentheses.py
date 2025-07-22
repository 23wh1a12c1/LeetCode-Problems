############      PYTHON3




class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(st = "", oc = 0, cc = 0):

            if len(st) == 2*n:
                res.append(st)
                return
            if oc < n:
                backTrack(st + "(", oc + 1, cc)
            if cc < oc:
                backTrack(st + ")", oc, cc + 1)
        
        backTrack()
        return res


                    ###########



lass Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, t):
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + '(')
            dfs(l, r + 1, t + ')')

        ans = []
        dfs(0, 0, '')
        return ans

############

class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
  
    def dfs(left, path, res, n):
      if len(path) == 2 * n:
        if left == 0:
          res.append("".join(path))
        return

      if left < n:
        path.append("(")
        dfs(left + 1, path, res, n)
        path.pop()
      if left > 0:
        path.append(")")
        dfs(left - 1, path, res, n)
        path.pop()

    res = []
    dfs(0, [], res, n)
    return res





################ JAVA





class Solution {
    private List<String> ans = new ArrayList<>();
    private int n;

    public List<String> generateParenthesis(int n) {
        this.n = n;
        dfs(0, 0, "");
        return ans;
    }

    private void dfs(int l, int r, String t) {
        if (l > n || r > n || l < r) {
            return;
        }
        if (l == n && r == n) {
            ans.add(t);
            return;
        }
        dfs(l + 1, r, t + "(");
        dfs(l, r + 1, t + ")");
    }
}







###############  C++






class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        function<void(int, int, string)> dfs = [&](int l, int r, string t) {
            if (l > n || r > n || l < r) return;
            if (l == n && r == n) {
                ans.push_back(t);
                return;
            }
            dfs(l + 1, r, t + "(");
            dfs(l, r + 1, t + ")");
        };
        dfs(0, 0, "");
        return ans;
    }
};













