###  PYTHON3


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        modified = doubled[1:-1]  # remove first and last character
        return s in modified



###   JAVA


class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String doubled = s + s;
        // Remove first and last character
        String modified = doubled.substring(1, doubled.length() - 1);
        // Check if original string is present in modified string
        return modified.contains(s);
    }
}




###   C++


class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string doubled = s + s;
        // Remove first and last character
        string modified = doubled.substr(1, doubled.size() - 2);
        // Check if original string is inside modified string
        return modified.find(s) != string::npos;
    }
};






