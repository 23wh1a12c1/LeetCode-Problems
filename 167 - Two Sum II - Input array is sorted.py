###    PYTHON3



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers)
        while i < j:
            x = numbers[i - 1] + numbers[j - 1]
            if x == target:
                return [i, j]
            if x < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]

############

class Solution(object):
  def twoSum(self, nums, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start, end = 0, len(nums) - 1
    while start < end:
      s = nums[start] + nums[end]
      if s > target:
        end -= 1
      elif s < target:
        start += 1
      else:
        return (start + 1, end + 1)






####   JAVA



class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 1, j = numbers.length;
        while (i < j) {
            int x = numbers[i - 1] + numbers[j - 1];
            if (x == target) {
                return new int[] {i, j};
            }
            if (x < target) {
                ++i;
            } else {
                --j;
            }
        }
        return new int[] {-1, -1};
    }
}




################


public class Two_Sum_II_Input_array_is_sorted {

    // time: O(N)
    // space: O(1)
    class Solution {
        public int[] twoSum(int[] numbers, int target) {
            int i = 0, j = numbers.length-1;
            int sum;
            while (i < j) {
                sum = numbers[i] + numbers[j];
                if (sum == target)
                    return new int[]{i+1, j+1};
                else if (sum < target)
                    i++;
                else
                    j--;
            }

            return null;

        }
    }
}







###    C++

﻿class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 1, right = numbers.size();
        while (left < right) {
            int x = numbers[left - 1] + numbers[right - 1];
            if (x == target) return {left, right};
            if (x < target)
                ++left;
            else
                --right;
        }
        return {-1, -1};
    }
};











