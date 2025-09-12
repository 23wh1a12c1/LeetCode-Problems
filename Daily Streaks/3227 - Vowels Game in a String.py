###   JAVA


class Solution {
    public boolean doesAliceWin(String s) {
        for (int i = 0; i < s.length(); ++i) {
            if ("aeiou".indexOf(s.charAt(i)) != -1) {
                return true;
            }
        }
        return false;
    }
}



###   PYTHON3


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        return any(c in vowels for c in s)




#### C++


class Solution {
public:
    bool doesAliceWin(string s) {
        string vowels = "aeiou";
        for (char c : s) {
            if (vowels.find(c) != string::npos) {
                return true;
            }
        }
        return false;
    }
};















