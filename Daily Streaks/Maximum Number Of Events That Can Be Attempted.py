from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # Sort events by start day
        min_heap = []
        i = 0
        n = len(events)
        res = 0
        day = 1

        # Find the last day when any event ends
        last_day = max(e[1] for e in events)

        # Iterate from day 1 to the last possible day
        while day <= last_day:
            # Add events that start today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])  # Push end day
                i += 1

            # Remove all events that have already expired
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends the earliest
            if min_heap:
                heapq.heappop(min_heap)
                res += 1

            day += 1

        return res
