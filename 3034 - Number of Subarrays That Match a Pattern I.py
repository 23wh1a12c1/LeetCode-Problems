###    PYTHON3




class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0
        for i in range(n - m):
            flag = True
            for j in range(m):
                if (
                    (pattern[j] == 1 and nums[i + j + 1] <= nums[i + j])
                    or (pattern[j] == 0 and nums[i + j + 1] != nums[i + j])
                    or (pattern[j] == -1 and nums[i + j + 1] >= nums[i + j])
                ):
                    flag = False
                    break
            if flag:
                count += 1
        return count




##   JAVA


class Solution {
    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int n = nums.length;
        int m = pattern.length;
        int count = 0;
        for (int i = 0; i <= n - m - 1; i++) {
            boolean flag = true;
            for (int j = 0; j < m; j++) {
                if ((pattern[j] == 1 && nums[i + j + 1] <= nums[i + j])
                    || (pattern[j] == 0 && nums[i + j + 1] != nums[i + j])
                    || (pattern[j] == -1 && nums[i + j + 1] >= nums[i + j])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                count++;
            }
        }
        return count;
    }
}




###   C++



class Solution {
public:
    int countMatchingSubarrays(vector<int>& nums, vector<int>& pattern) {
        int n = nums.size();
        int m = pattern.size();
        int c = 0;
        for (int i = 0; i <= n - m - 1; i++) {
            bool flag = true;
            for (int j = 0; j < m; j++) {
                if ((pattern[j] == 1 && nums[i + j + 1] <= nums[i + j]) || (pattern[j] == 0 && nums[i + j + 1] != nums[i + j]) || (pattern[j] == -1 && nums[i + j + 1] >= nums[i + j])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                c++;
            }
        }
        return c;
    }
};







