######################   PYTHON3



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(st = 0):
            if st == len(nums):
                res.append(nums[:])
                return
            for i in range(st, len(nums)):
                nums[st], nums[i] = nums[i], nums[st]
                backTrack(st+1)
                nums[st], nums[i] = nums[i], nums[st]

        backTrack()
        return




            ##################

'''
remove an element by its value from a set

>>> my_set = {1, 2, 3, 4, 5}
>>> my_set.remove(3)
>>> print(my_set)
{1, 2, 4, 5}

------

cannot remove an element by index from a set in Python3
need to convert the set to a list

>>> my_set = {1, 2, 3, 4, 5}
>>> my_list = list(my_set)
>>> del my_list[2] # remove the element at index 2
>>> my_set = set(my_list)
>>> print(my_set)
{1, 2, 4, 5}
'''


class Solution: # iterative
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        if nums is None or len(nums) == 0:
            return ans

        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    new_res.append(new_perm)

            res = new_res

        return res

##############

class Solution: # iterative, single_perm.insert(index, num)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        if nums is None or len(nums) == 0:
            return ans

        for num in nums:
            tmp_list = []

            for single_perm in ans:
                for index in range(len(single_perm) + 1):
                    single_perm.insert(index, num)
                    tmp_list.append(single_perm.copy())
                    single_perm.pop(index)

            ans = tmp_list

        return ans

##############





'''
In Python 3, both the discard() and remove() methods of a set object are used to remove an element from the set, but there is one key difference:

* discard() removes the specified element from the set if it is present, but does nothing if the element is not present.
* remove() removes the specified element from the set if it is present, but raises a KeyError exception if the element is not present.


>>> a
{33, 66, 11, 44, 22, 55}
>>> a.discard(22)
>>> a
{33, 66, 11, 44, 55}

>>> a.discard(200)
>>>
>>> a.remove(200)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 200
'''

'''
>>> v1 = set([])
>>> v2 = set()
>>>
>>> v1

set()
>>> v2
set()
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set([])

        def dfs(nums, path, res, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return

            for i in range(0, len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(nums, path, res, visited)
                    path.pop()
                    visited.discard(i) # remove(i) will throw exception if i not existing

        dfs(nums, [], res, visited)
        return res

############


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == n:
                ans.append(t[:])
                return
            for j in range(n):
                if not vis[j]:
                    vis[j] = True
                    t[i] = nums[j]
                    dfs(i + 1)
                    vis[j] = False

        n = len(nums)
        vis = [False] * n
        t = [0] * n
        ans = []
        dfs(0)
        return ans









#######################################          JAVA



class Solution {
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> t = new ArrayList<>();
    private boolean[] vis;
    private int[] nums;

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        vis = new boolean[nums.length];
        dfs(0);
        return ans;
    }

    private void dfs(int i) {
        if (i == nums.length) {
            ans.add(new ArrayList<>(t));
            return;
        }
        for (int j = 0; j < nums.length; ++j) {
            if (!vis[j]) {
                vis[j] = true;
                t.add(nums[j]);
                dfs(i + 1);
                t.remove(t.size() - 1);
                vis[j] = false;
            }
        }
    }
}






##########################    C++



class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        vector<int> t(n);
        vector<bool> vis(n);
        function<void(int)> dfs = [&](int i) {
            if (i == n) {
                ans.emplace_back(t);
                return;
            }
            for (int j = 0; j < n; ++j) {
                if (!vis[j]) {
                    vis[j] = true;
                    t[i] = nums[j];
                    dfs(i + 1);
                    vis[j] = false;
                }
            }
        };
        dfs(0);
        return ans;
    }
};










