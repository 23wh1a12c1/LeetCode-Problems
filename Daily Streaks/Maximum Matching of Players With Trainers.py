# JAVA



  

class Solution {
    public int matchPlayersAndTrainers(int[] player, int[] train) {
        Arrays.sort(player);
        Arrays.sort(train);
        int i = 0, j = 0, res = 0;
        while(j<train.length && i<player.length) {
            if(player[i]>train[j])
                while(j<train.length && train[j]<player[i]) // find trainer
                    j++;
            else { res++; i++; j++; } // can train.
        }
        return res;
    }
}

############

class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int ans = 0;
        int j = 0;
        for (int p : players) {
            while (j < trainers.length && trainers[j] < p) {
                ++j;
            }
            if (j < trainers.length) {
                ++ans;
                ++j;
            }
        }
        return ans;
    }
}






# PYTHON3




  class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = j = 0
        for p in players:
            while j < len(trainers) and trainers[j] < p:
                j += 1
            if j < len(trainers):
                ans += 1
                j += 1
        return ans

############

# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        N, M = len(players), len(trainers)
        players.sort()
        trainers.sort()
        res = 0
        firstPlayer = players[0]
        j = bisect_left(trainers, firstPlayer)
        
        if j == M: return 0
        
        for player in players:
            while j < M and player > trainers[j]:
                j += 1
                
            if j == M: break
                
            if player <= trainers[j]:
                res += 1
                j += 1

        return res





  # CPP





  class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());
        int ans = 0, j = 0;
        for (int p : players) {
            while (j < trainers.size() && trainers[j] < p) {
                ++j;
            }
            if (j < trainers.size()) {
                ++ans;
                ++j;
            }
        }
        return ans;
    }
};
