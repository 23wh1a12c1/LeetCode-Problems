######   JAVA


class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0, right = Arrays.stream(nums).sum();
        for(int i=0;i<nums.length;i++) {
            right -= nums[i];
            if(left == right) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
}


                              #################

class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for(int num : nums) {
            totalSum += num;
        }

        int left =0;
        for (int i=0; i<nums.length; i++) {
            int right = totalSum - left - nums[i];
            if (left == right) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
}




#############################         PYTHON3



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, x in enumerate(nums):
            right -= x
            if left == right:
                return i
            left += x
        return -1



####################            C++


class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0, right = accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            right -= nums[i];
            if (left == right) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};








