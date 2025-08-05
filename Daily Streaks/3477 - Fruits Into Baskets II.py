####   PYTHON3


from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n  # Track if a basket has been used
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # Mark basket as used
                    placed = True
                    break
            if not placed:
                unplaced += 1  # Could not find a suitable basket

        return unplaced




#####    JAVA


class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.length;
        boolean[] used = new boolean[n];  // Track if a basket is used
        int unplaced = 0;

        for (int fruit : fruits) {
            boolean placed = false;
            for (int i = 0; i < n; i++) {
                if (!used[i] && baskets[i] >= fruit) {
                    used[i] = true;  // Mark this basket as used
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                unplaced++;  // Could not place this fruit
            }
        }

        return unplaced;
    }
}




#####     C++

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        vector<bool> used(n, false); // Tracks if a basket is already used
        int unplaced = 0;

        for (int i = 0; i < n; ++i) {
            bool placed = false;
            for (int j = 0; j < n; ++j) {
                if (!used[j] && baskets[j] >= fruits[i]) {
                    used[j] = true; // Mark basket as used
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                ++unplaced; // Could not place the fruit
            }
        }

        return unplaced;
    }
};

