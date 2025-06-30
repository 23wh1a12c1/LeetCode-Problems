# JAVA




class Solution {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        int ans = 0;
        for (int num : nums) {
            if (counter.containsKey(num + 1)) {
                ans = Math.max(ans, counter.get(num) + counter.get(num + 1));
            }
        }
        return ans;
    }
}




# PYTHON3





class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for num in nums:
            if num + 1 in counter:
                ans = max(ans, counter[num] + counter[num + 1])
        return ans



# CPP





class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> counter;
        for (int num : nums) {
            ++counter[num];
        }
        int ans = 0;
        for (int num : nums) {
            if (counter.count(num + 1)) {
                ans = max(ans, counter[num] + counter[num + 1]);
            }
        }
        return ans;
    }
};

