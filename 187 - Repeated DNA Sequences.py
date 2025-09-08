###   PYTHON3



from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()          # To keep track of sequences we've seen once
        repeated = set()      # To keep track of sequences that repeat
        result = []

        for i in range(len(s) - 9):  # length 10 substrings
            substring = s[i:i+10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)




###    JAVA



import java.util.*;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> seen = new HashSet<>();
        Set<String> repeated = new HashSet<>();
        
        for (int i = 0; i <= s.length() - 10; i++) {
            String substring = s.substring(i, i + 10);
            if (seen.contains(substring)) {
                repeated.add(substring);
            } else {
                seen.add(substring);
            }
        }
        
        return new ArrayList<>(repeated);
    }
}




###    C++


#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> seen;
        unordered_set<string> repeated;
        
        int n = s.size();
        if (n < 10) return {};
        
        for (int i = 0; i <= n - 10; ++i) {
            string substring = s.substr(i, 10);
            if (seen.find(substring) != seen.end()) {
                repeated.insert(substring);
            } else {
                seen.insert(substring);
            }
        }
        
        return vector<string>(repeated.begin(), repeated.end());
    }
};







