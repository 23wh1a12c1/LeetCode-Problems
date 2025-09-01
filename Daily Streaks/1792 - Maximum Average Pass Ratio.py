####      PYTHON3


import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(passed: int, total: int) -> float:
            # Calculate how much adding one passing student increases pass ratio
            return (passed + 1) / (total + 1) - passed / total
        
        # Build a max-heap using negative gains because Python's heapq is a min-heap
        heap = []
        for passed, total in classes:
            heapq.heappush(heap, (-gain(passed, total), passed, total))

        # Allocate extra students greedily
        for _ in range(extraStudents):
            curr_gain, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            heapq.heappush(heap, (-gain(passed, total), passed, total))

        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passed, total in heap:
            total_ratio += passed / total

        return total_ratio / len(classes)



                  ###   OR


class Solution:
  def maxAverageRatio(
      self,
      classes: list[list[int]],
      extraStudents: int,
  ) -> float:
    def extraPassRatio(pas: int, total: int) -> float:
      """Returns the extra pass ratio if a brilliant student joins."""
      return (pas + 1) / (total + 1) - pas / total

    maxHeap = [(-extraPassRatio(pas, total), pas, total)
               for pas, total in classes]
    heapq.heapify(maxHeap)

    for _ in range(extraStudents):
      _, pas, total = heapq.heappop(maxHeap)
      heapq.heappush(
          maxHeap, (-extraPassRatio(pas + 1, total + 1), pas + 1, total + 1))

    return sum(pas / total for _, pas, total in maxHeap) / len(maxHeap)




####   JAVA



class Solution {
  public double maxAverageRatio(int[][] classes, int extraStudents) {
    // (extra pass ratio, pass, total)
    PriorityQueue<T> maxHeap =
        new PriorityQueue<>((a, b) -> Double.compare(b.extraPassRatio, a.extraPassRatio));

    for (int[] c : classes) {
      final int pass = c[0];
      final int total = c[1];
      maxHeap.offer(new T(getExtraPassRatio(pass, total), pass, total));
    }

    for (int i = 0; i < extraStudents; ++i) {
      final int pass = maxHeap.peek().pass;
      final int total = maxHeap.poll().total;
      maxHeap.offer(new T(getExtraPassRatio(pass + 1, total + 1), pass + 1, total + 1));
    }

    double ratioSum = 0;

    while (!maxHeap.isEmpty())
      ratioSum += maxHeap.peek().pass / (double) maxHeap.poll().total;

    return ratioSum / classes.length;
  }

  // Returns the extra pass ratio if a brilliant student joins.
  private double getExtraPassRatio(int pass, int total) {
    return (pass + 1) / (double) (total + 1) - pass / (double) total;
  }

  private record T(double extraPassRatio, int pass, int total){};
}





###    C++



class Solution {
 public:
  double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
    // (extra pass ratio, pass, total)
    priority_queue<tuple<double, int, int>> maxHeap;

    for (const vector<int>& c : classes) {
      const int pass = c[0];
      const int total = c[1];
      maxHeap.emplace(extraPassRatio(pass, total), pass, total);
    }

    for (int i = 0; i < extraStudents; ++i) {
      const auto [_, pass, total] = maxHeap.top();
      maxHeap.pop();
      maxHeap.emplace(extraPassRatio(pass + 1, total + 1), pass + 1, total + 1);
    }

    double ratioSum = 0;

    while (!maxHeap.empty()) {
      const auto [_, pass, total] = maxHeap.top();
      maxHeap.pop();
      ratioSum += pass / static_cast<double>(total);
    }

    return ratioSum / classes.size();
  }

 private:
  // Returns the extra pass ratio if a brilliant student joins.
  double extraPassRatio(int pass, int total) {
    return (pass + 1) / static_cast<double>(total + 1) -
           pass / static_cast<double>(total);
  }
};












