# JAVA



class Solution {
    public char kthCharacter(int k) {
        List<Integer> word = new ArrayList<>();
        word.add(0);
        while (word.size() < k) {
            for (int i = 0, m = word.size(); i < m; ++i) {
                word.add((word.get(i) + 1) % 26);
            }
        }
        return (char) ('a' + word.get(k - 1));
    }
}




# PYTHON3



class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]
        while len(word) < k:
            word.extend([(x + 1) % 26 for x in word])
        return chr(ord("a") + word[k - 1])




# CPP



class Solution {
public:
    char kthCharacter(int k) {
        vector<int> word;
        word.push_back(0);
        while (word.size() < k) {
            int m = word.size();
            for (int i = 0; i < m; ++i) {
                word.push_back((word[i] + 1) % 26);
            }
        }
        return 'a' + word[k - 1];
    }
};
