#############          PYTHON3



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(start,curr_combi, curr_sum):
            if curr_sum == target:
                res.append(curr_combi[:])
                return

            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                curr_combi.append(candidates[i])
                backTrack(i,curr_combi, curr_sum + candidates[i])
                curr_combi.pop()
        backTrack(0,[],0)
        return res


                    ######################




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # i: start index for this recursion
        # s: sum
        def dfs(i, s):
            if s == target:
                ans.append(t.copy())
                return
            if s > target:
                return
            for j in range(i, len(candidates)):
                c = candidates[j]
                t.append(c)
                dfs(j, s + c)
                t.pop()

        ans = []
        t = []
        # candidates.sort() # diff from combinationSum-II, no need sorting it
        dfs(0, 0)
        return ans

############

# dp version
class Solution_dp:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # for each-target (from 1 to target), its dp[i][j]
        #   => so 3-D array dp[][][]
        dp = []
        candidates.sort()

        for i in range(1, target+1):
            cur = []
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                if candidates[j] == i:
                    one = [candidates[j]]
                    cur.append(one)
                    break
                for a in dp[i - candidates[j] - 1]:
                    if candidates[j] > a[0]:
                        continue
                    deepCopied = a.copy()
                    deepCopied.insert(0, candidates[j])
                    cur.append(deepCopied)
            dp.append(cur)

        return dp[-1]


############

class Solution(object):
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def dfs(candidates, start, target, path, res):
      if target == 0:
        return res.append(path + [])

      for i in range(start, len(candidates)):
        if target - candidates[i] >= 0:
          path.append(candidates[i])
          dfs(candidates, i, target - candidates[i], path, res)
          path.pop()

    res = []
    dfs(candidates, 0, target, [], res)
    return res

#########

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            dfs(i + 1, s)
            t.append(candidates[i])
            dfs(i, s - candidates[i])
            t.pop()

        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans









#########################  JAVA



class Solution {
    private List<List<Integer>> ans = new ArrayList<>();
    private List<Integer> t = new ArrayList<>();
    private int[] candidates;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        this.candidates = candidates;
        dfs(0, target);
        return ans;
    }

    private void dfs(int i, int s) {
        if (s == 0) {
            ans.add(new ArrayList(t));
            return;
        }
        if (i >= candidates.length || s < candidates[i]) {
            return;
        }
        dfs(i + 1, s);
        t.add(candidates[i]);
        dfs(i, s - candidates[i]);
        t.remove(t.size() - 1);
    }
}

//////

class Solution_dp {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // for each-target (from 1 to target), its dp[i][j] => so 3-D array dp[][][]
        List<List<List<Integer>>> dp = new ArrayList<>();
        Arrays.sort(candidates);

        for (int i = 1; i <= target; ++i) {
            List<List<Integer>> cur = new ArrayList<>();
            for (int j = 0; j < candidates.length; ++j) {
                if (candidates[j] > i) break;
                if (candidates[j] == i) {
                    ArrayList<Integer> one = new ArrayList<Integer>();
                    one.add(candidates[j]);
                    cur.add(one); // @note: one with proper <Integer>, or else unsupoorted operation error
                    break;
                }
                for (List<Integer> a : dp.get(i - candidates[j] - 1)) {
                    if (candidates[j] > a.get(0)) {
                        continue;
                    }

                    ArrayList<Integer> deepCopied = new ArrayList<>(a); // @note: must have
                    deepCopied.add(0, candidates[j]); // @note: largest at index=0 for the array
                    cur.add(deepCopied);
                }
            }
            dp.add(cur);
        }

        return dp.get(dp.size() - 1);
    }

}










############################     C++







class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int, int)> dfs = [&](int i, int s) {
            if (s == 0) {
                ans.emplace_back(t);
                return;
            }
            if (i >= candidates.size() || s < candidates[i]) {
                return;
            }
            dfs(i + 1, s);
            t.push_back(candidates[i]);
            dfs(i, s - candidates[i]);
            t.pop_back();
        };
        dfs(0, target);
        return ans;
    }
};






























