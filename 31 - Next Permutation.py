######     PYTHON3



'''
>>> i = 3
>>> ~i
-4
>>> bool(~i)
True
#######################

>>> j = -1
>>> ~j
0
>>> bool(~j)
False
#######################

>>> a = (i for i in range (10, -1, -1) if i < 6)
>>> a
<generator object <genexpr> at 0x10a17eeb0>
>>> next(a)
5
>>>
>>>
>>> b = (i for i in range (10, -1, -1) if i < 0)
>>> next(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> next(b, -1)
-1
>>>
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # next(func, -1) => default value -1
        i = next((i for i in range(n - 2, -1, -1) if nums[i] < nums[i + 1]), -1)
        if i != -1:
            j = next((j for j in range(n - 1, i, -1) if nums[j] > nums[i]))
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        # wrong reverse: nums[i + 1:] = nums[i + 1::-1]

##############

'''
>>> a=[1,2,3]
>>> reversed(a)
<list_reverseiterator object at 0x108458be0>
>>> list(reversed(a))
[3, 2, 1]

# but, use reversed(a) to directly assign values is ok
>>> b=[4,5,6,7,8]
>>> b[:3] = reversed(a)
>>> b
[3, 2, 1, 7, 8]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return

        for i in range(len(nums)-2, -1, -1):  # 3, 4, 5, 2, 1
            if nums[i] < nums[i+1]:  
                j = next(j for j in range(len(nums)-1, i, -1) if nums[j] > nums[i])  
                nums[i], nums[j] = nums[j], nums[i]  # 3,5,4,2,1

               
                nums[i+1:] = reversed(nums[i+1:])  # [4,2,1] reverse to [1,2,4] => 3, 5, 1, 2, 4
                return

        nums.reverse()  

###########


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        to_left = [i for i in range(n - 2, -1, -1) if nums[i] < nums[i + 1]]

        if not to_left:
            nums = nums[::-1]
            return

        i = max(to_left)
        if i >= 0:
            to_right = [ j for j in range(n - 1, i, -1) if nums[j] > nums[i] ]
            j = to_right[0]
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1::-1]






######   JAVA






import java.util.Arrays;

public class Next_Permutation {

    // time: O(N^2)
    // space: O(1)
    public class Solution {

        public void nextPermutation(int[] nums) {

            if (nums == null || nums.length == 0) {
                return;
            }

            // 总体目标是，高位的小数字，换低位的大数字，才能得到next
            for (int i = nums.length - 2; i >= 0; --i) { // 3, 4, 5, 2, 1 // 注意. i < Len - 1. 也就是停在倒数第二个
                if (nums[i] < nums[i + 1]) { // 第一个波峰波谷 => 4
                    for (int j = nums.length - 1; j > i; --j) {
                        if (nums[j] > nums[i]) {
                            // 找到第一个比nums-i大的数 => 5
                            swap(nums, i, j); // 3,5,4,2,1

                            // reverse 因为剩下部分肯定是从大到小
                            // 找到第一个比nums-i大的数的一步，相当于是排序，找insert position
                            reverse(nums, i + 1, nums.length - 1); // [4,2,1] reverse to [1,2,4] => 3, 5, 1, 2, 4
                            return;
                        }
                    }

                }
            }

            reverse(nums, 0, nums.length - 1); // for没有return，就整个翻转
        }

        private void swap(int[] nums, int i, int j) {

            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;

        }

        private void reverse(int[] nums, int i, int j) {

            while (i < j) {

                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;

                i++;
                j--;
            }
        }
    }
}

//////

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;
        for (; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) {
                break;
            }
        }
        if (i >= 0) {
            for (int j = n - 1; j > i; --j) {
                if (nums[j] > nums[i]) {
                    swap(nums, i, j);
                    break;
                }
            }
        }

        for (int j = i + 1, k = n - 1; j < k; ++j, --k) {
            swap(nums, j, k);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[j];
        nums[j] = nums[i];
        nums[i] = t;
    }
}






#######    C++



class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        while (~i && nums[i] >= nums[i + 1]) {
            --i;
        }
        if (~i) {
            for (int j = n - 1; j > i; --j) {
                if (nums[j] > nums[i]) {
                    swap(nums[i], nums[j]);
                    break;
                }
            }
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};























