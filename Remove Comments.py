# PYTHON3



class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        t = []
        block_comment = False
        for s in source:
            i, m = 0, len(s)
            while i < m:
                if block_comment:
                    if i + 1 < m and s[i : i + 2] == "*/":
                        block_comment = False
                        i += 1
                else:
                    if i + 1 < m and s[i : i + 2] == "/*":
                        block_comment = True
                        i += 1
                    elif i + 1 < m and s[i : i + 2] == "//":
                        break
                    else:
                        t.append(s[i])
                i += 1
            if not block_comment and t:
                ans.append("".join(t))
                t.clear()
        return ans






# JAVA



class Solution {
    public List<String> removeComments(String[] source) {
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean blockComment = false;

        for(String s : source) {
            int n = s.length();
            for(int i=0;i<n;i++) {
                if(blockComment) {
                    if(i+1 < n && s.charAt(i) == '*' && s.charAt(i+1) == '/') {
                        blockComment = false;
                        i++;
                    }
                }
                else {
                    if(i+1 < n && s.charAt(i) == '/' && s.charAt(i+1) == '*') {
                        blockComment = true;
                        i++;
                    }
                    else if(i+1 < n && s.charAt(i) == '/' && s.charAt(i+1) == '/') {
                        break;
                    }
                    else {
                        sb.append(s.charAt(i));
                    }
                }
            }
            if (!blockComment && sb.length() > 0) {
                res.add(sb.toString());
                sb.setLength(0);
            }
        }
        return res;

    }
}





# C++





class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> ans;
        string t;
        bool blockComment = false;
        for (auto& s : source) {
            int m = s.size();
            for (int i = 0; i < m; ++i) {
                if (blockComment) {
                    if (i + 1 < m && s[i] == '*' && s[i + 1] == '/') {
                        blockComment = false;
                        ++i;
                    }
                } else {
                    if (i + 1 < m && s[i] == '/' && s[i + 1] == '*') {
                        blockComment = true;
                        ++i;
                    } else if (i + 1 < m && s[i] == '/' && s[i + 1] == '/') {
                        break;
                    } else {
                        t.push_back(s[i]);
                    }
                }
            }
            if (!blockComment && !t.empty()) {
                ans.emplace_back(t);
                t.clear();
            }
        }
        return ans;
    }
};






















