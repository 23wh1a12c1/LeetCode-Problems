###    PYTHON3


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        stk = []
        for v in nums2:
            while stk and stk[-1] < v:
                m[stk.pop()] = v
            stk.append(v)
        return [m.get(v, -1) for v in nums1]



###   JAVA


class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> stk = new ArrayDeque<>();
        Map<Integer, Integer> mp = new HashMap<>();
        for (int num : nums2) {
            while (!stk.isEmpty() && stk.peek() < num) {
                mp.put(stk.pop(), num);
            }
            stk.push(num);
        }
        int n = nums1.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; ++i) {
            ans[i] = mp.getOrDefault(nums1[i], -1);
        }
        return ans;
    }
}



#####     C++


class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stk;
        unordered_map<int, int> m;
        for (int& v : nums2) {
            while (!stk.empty() && stk.top() < v) {
                m[stk.top()] = v;
                stk.pop();
            }
            stk.push(v);
        }
        vector<int> ans;
        for (int& v : nums1) ans.push_back(m.count(v) ? m[v] : -1);
        return ans;
    }
};




