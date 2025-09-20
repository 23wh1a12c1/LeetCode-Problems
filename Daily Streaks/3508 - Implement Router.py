###     PYTHON3


from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False  # duplicate
        # If memory exceeds, remove the oldest packet
        if len(self.packets) == self.memoryLimit:
            old_packet = self.packets.popleft()
            self.packet_set.remove(tuple(old_packet))
            # remove from dest_map
            old_dest = old_packet[1]
            old_time = old_packet[2]
            idx = bisect_left(self.dest_map[old_dest], old_time)
            if idx < len(self.dest_map[old_dest]) and self.dest_map[old_dest][idx] == old_time:
                self.dest_map[old_dest].pop(idx)
            # Optionally remove key if list becomes empty
            if not self.dest_map[old_dest]:
                del self.dest_map[old_dest]
        self.packets.append([source, destination, timestamp])
        self.packet_set.add(key)
        # As timestamp always increases on addPacket, can just append
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        packet = self.packets.popleft()
        self.packet_set.remove(tuple(packet))
        dest = packet[1]
        time = packet[2]
        # remove from dest_map
        idx = bisect_left(self.dest_map[dest], time)
        if idx < len(self.dest_map[dest]) and self.dest_map[dest][idx] == time:
            self.dest_map[dest].pop(idx)
        if not self.dest_map[dest]:
            del self.dest_map[dest]
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.dest_map.get(destination, [])
        if not times:
            return 0
        left = bisect_left(times, startTime)
        right = bisect_right(times, endTime)
        return right - left



                      ############

from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:
    def __init__(self, m):
        self.m, self.q = m, deque()
        self.s = set()
        self.d = defaultdict(list)
    def addPacket(self, src, dst, t):
        k = (src, dst, t)
        if k in self.s: return False
        if len(self.q) == self.m:
            o = self.q.popleft(); self.s.remove(tuple(o))
            l, od, ot = self.d[o[1]], o[1], o[2]
            i = bisect_left(l, ot)
            if i < len(l) and l[i]==ot: l.pop(i)
            if not l: del self.d[od]
        self.q.append([src, dst, t]); self.s.add(k)
        self.d[dst].append(t)
        return True
    def forwardPacket(self):
        if not self.q: return []
        p = self.q.popleft(); self.s.remove(tuple(p))
        l, d, t = self.d[p[1]], p[1], p[2]
        i = bisect_left(l, t)
        if i < len(l) and l[i]==t: l.pop(i)
        if not l: del self.d[d]
        return p
    def getCount(self, d, s, e):
        l = self.d.get(d, [])
        return bisect_right(l, e) - bisect_left(l, s)




########   JAVA





















