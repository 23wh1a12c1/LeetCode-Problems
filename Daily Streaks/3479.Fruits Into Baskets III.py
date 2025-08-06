#####  PYTHON3


class SegmentTree:
    __slots__ = ["nums", "tr"]

    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [0] * (n << 2)
        self.build(1, 1, n)

    def build(self, u, l, r):
        if l == r:
            self.tr[u] = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, l, r, i, v):
        if l == r:
            self.tr[u] = v
            return
        mid = (l + r) >> 1
        if i <= mid:
            self.modify(u << 1, l, mid, i, v)
        else:
            self.modify(u << 1 | 1, mid + 1, r, i, v)
        self.pushup(u)

    def query(self, u, l, r, v):
        if self.tr[u] < v:
            return -1
        if l == r:
            return l
        mid = (l + r) >> 1
        if self.tr[u << 1] >= v:
            return self.query(u << 1, l, mid, v)
        return self.query(u << 1 | 1, mid + 1, r, v)

    def pushup(self, u):
        self.tr[u] = max(self.tr[u << 1], self.tr[u << 1 | 1])


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        n = len(baskets)
        ans = 0
        for x in fruits:
            i = tree.query(1, 1, n, x)
            if i < 0:
                ans += 1
            else:
                tree.modify(1, 1, n, i, 0)
        return ans





####    JAVA



class SegmentTree {
    int[] nums;
    int[] tr;

    public SegmentTree(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        this.tr = new int[n << 2];
        build(1, 1, n);
    }

    public void build(int u, int l, int r) {
        if (l == r) {
            tr[u] = nums[l - 1];
            return;
        }
        int mid = (l + r) >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
        pushup(u);
    }

    public void modify(int u, int l, int r, int i, int v) {
        if (l == r) {
            tr[u] = v;
            return;
        }
        int mid = (l + r) >> 1;
        if (i <= mid) {
            modify(u << 1, l, mid, i, v);
        } else {
            modify(u << 1 | 1, mid + 1, r, i, v);
        }
        pushup(u);
    }

    public int query(int u, int l, int r, int v) {
        if (tr[u] < v) {
            return -1;
        }
        if (l == r) {
            return l;
        }
        int mid = (l + r) >> 1;
        if (tr[u << 1] >= v) {
            return query(u << 1, l, mid, v);
        }
        return query(u << 1 | 1, mid + 1, r, v);
    }

    public void pushup(int u) {
        tr[u] = Math.max(tr[u << 1], tr[u << 1 | 1]);
    }
}

class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        SegmentTree tree = new SegmentTree(baskets);
        int n = baskets.length;
        int ans = 0;
        for (int x : fruits) {
            int i = tree.query(1, 1, n, x);
            if (i < 0) {
                ans++;
            } else {
                tree.modify(1, 1, n, i, 0);
            }
        }
        return ans;
    }
}



#####   C++


class SegmentTree {
public:
    vector<int> nums, tr;

    SegmentTree(vector<int>& nums) {
        this->nums = nums;
        int n = nums.size();
        tr.resize(n * 4);
        build(1, 1, n);
    }

    void build(int u, int l, int r) {
        if (l == r) {
            tr[u] = nums[l - 1];
            return;
        }
        int mid = (l + r) >> 1;
        build(u * 2, l, mid);
        build(u * 2 + 1, mid + 1, r);
        pushup(u);
    }

    void modify(int u, int l, int r, int i, int v) {
        if (l == r) {
            tr[u] = v;
            return;
        }
        int mid = (l + r) >> 1;
        if (i <= mid) {
            modify(u * 2, l, mid, i, v);
        } else {
            modify(u * 2 + 1, mid + 1, r, i, v);
        }
        pushup(u);
    }

    int query(int u, int l, int r, int v) {
        if (tr[u] < v) {
            return -1;
        }
        if (l == r) {
            return l;
        }
        int mid = (l + r) >> 1;
        if (tr[u * 2] >= v) {
            return query(u * 2, l, mid, v);
        }
        return query(u * 2 + 1, mid + 1, r, v);
    }

    void pushup(int u) {
        tr[u] = max(tr[u * 2], tr[u * 2 + 1]);
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        SegmentTree tree(baskets);
        int n = baskets.size();
        int ans = 0;
        for (int x : fruits) {
            int i = tree.query(1, 1, n, x);
            if (i < 0) {
                ans++;
            } else {
                tree.modify(1, 1, n, i, 0);
            }
        }
        return ans;
    }
};








