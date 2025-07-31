###    JAVA

import java.util.*;

class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> ans = new HashSet<>();        // To store all unique OR values
        Set<Integer> prev = new HashSet<>();       // OR values of subarrays ending at previous index

        for (int num : arr) {
            Set<Integer> curr = new HashSet<>();   // OR values of subarrays ending at current index
            
            // Each new subarray starts with the current number
            curr.add(num);

            // Extend previous subarrays by OR-ing with current number
            for (int val : prev) {
                curr.add(val | num);
            }

            // Update answer and prepare for next iteration
            ans.addAll(curr);
            prev = curr;
        }

        return ans.size();
    }
}

                    #####
class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> s = new HashSet<>();
        s.add(0);
        Set<Integer> ans = new HashSet<>();
        for (int x : arr) {
            Set<Integer> t = new HashSet<>();
            for (int y : s) {
                t.add(x | y);
            }
            t.add(x);
            s = t;
            ans.addAll(s);
        }
        return ans.size();
    }
}




##############  PYTHON3



class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s = {0}
        ans = set()
        for x in arr:
            s = {x | y for y in s} | {x}
            ans |= s
        return len(ans)




#############   C++



class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> s{ {0} };
        unordered_set<int> ans;
        for (int& x : arr) {
            unordered_set<int> t{ {x} };
            for (int y : s) {
                t.insert(x | y);
            }
            s = move(t);
            ans.insert(s.begin(), s.end());
        }
        return ans.size();
    }
};
