# JAVA




class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        int[] ans = new int[k];
        List<Integer> idx = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            idx.add(i);
        }
        idx.sort(Comparator.comparingInt(i -> - nums[i]));
        int[] t = new int[k];
        for (int i = 0; i < k; ++i) {
            t[i] = idx.get(i);
        }
        Arrays.sort(t);
        for (int i = 0; i < k; ++i) {
            ans[i] = nums[t[i]];
        }
        return ans;
    }
}





#  PYTHON3





class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = list(range(len(nums)))
        idx.sort(key=lambda i: nums[i])
        return [nums[i] for i in sorted(idx[-k:])]




# CPP




class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int n = nums.size();
        vector<pair<int, int>> vals;
        for (int i = 0; i < n; ++i) vals.push_back({i, nums[i]});
        sort(vals.begin(), vals.end(), [&](auto x1, auto x2) {
            return x1.second > x2.second;
        });
        sort(vals.begin(), vals.begin() + k);
        vector<int> ans;
        for (int i = 0; i < k; ++i) ans.push_back(vals[i].second);
        return ans;
    }
};

