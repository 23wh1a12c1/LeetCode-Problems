###################      PYTHON3



class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        ans = 0
        stk1, stk2 = [], []
        for c in s:
            if c != 'b':
                stk1.append(c)
            else:
                if stk1 and stk1[-1] == 'a':
                    stk1.pop()
                    ans += x
                else:
                    stk1.append(c)
        while stk1:
            c = stk1.pop()
            if c != 'b':
                stk2.append(c)
            else:
                if stk2 and stk2[-1] == 'a':
                    stk2.pop()
                    ans += y
                else:
                    stk2.append(c)
        return ans


############

# 1717. Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int):
        
        def remove(s, target, val):
            total = 0
            stack = []
            
            for c in s:
                stack.append(c)
                
                while len(stack) >= 2 and (stack[-2]+stack[-1]) == target:
                    stack.pop()
                    stack.pop()
                    total += val
            
            return stack, total
        
        if x > y:
            s, val1 = remove(s, "ab", x)
            s, val2 = remove(s, "ba", y)
            
            return val1 + val2
        else:
            s, val1 = remove(s, "ba", y)
            s, val2 = remove(s, "ab", x)
            
            return val1 + val2
        
    def maximumGain(self, s: str, x: int, y: int):
        a = b = res = 0
        
        if x == y:
            for i,c in enumerate(s):
                if c == "a": 
                    if b > 0:
                        res += y
                        b -= 1
                    else:
                        a += 1

                elif c == "b": 
                    if a > 0:
                        res += x
                        a -= 1
                    else:
                        b += 1

                else: 
                    a = b = 0
        else:
            checkAB = x > y
            used = set()
            adeq = deque()
            bdeq = deque()
            
            for i,c in enumerate(s):
                if c == "a":
                    if checkAB:
                        a += 1
                        adeq.append(i)
                    else:
                        if b > 0:
                            res += y
                            b -= 1
                            used.add(bdeq.pop())
                            used.add(i)
                        else:
                            a += 1
                            adeq.append(i)
                            
                elif c == "b":
                    if checkAB:
                        if a > 0:
                            res += x
                            a -= 1
                            used.add(adeq.pop())
                            used.add(i)
                        else:
                            b += 1
                            bdeq.append(i)
                    else:
                        b += 1
                        bdeq.append(i)
                            
                else:
                    a = b = 0
                    adeq.clear()
                    bdeq.clear()
                    
            a = b = 0
            
            for i,c in enumerate(s):
                if c != "a" and c != "b":
                    a = b = 0
                else:
                    if i in used: continue
                        
                    if c == "a": 
                        if b > 0:
                            res += y
                            b -= 1
                        else:
                            a += 1

                    else: 
                        if a > 0:
                            res += x
                            a -= 1
                        else:
                            b += 1
                    
                    
        
        return res















#############################                       JAVA






    class Solution {
        int points = 0;

        public int maximumGain(String s, int x, int y) {
            if (x >= y) {
                s = remove1(s, x);
                s = remove2(s, y);
            } else {
                s = remove2(s, y);
                s = remove1(s, x);
            }
            return points;
        }

        public String remove1(String s, int x) {
            StringBuffer sb = new StringBuffer();
            int length = s.length();
            int index = 0;
            for (int i = 0; i < length; i++) {
                char c = s.charAt(i);
                if (index > 0 && c == 'b' && sb.charAt(index - 1) == 'a') {
                    points += x;
                    sb.deleteCharAt(index - 1);
                    index--;
                } else {
                    sb.append(c);
                    index++;
                }
            }
            return sb.toString();
        }

        public String remove2(String s, int y) {
            StringBuffer sb = new StringBuffer();
            int length = s.length();
            int index = 0;
            for (int i = 0; i < length; i++) {
                char c = s.charAt(i);
                if (index > 0 && c == 'a' && sb.charAt(index - 1) == 'b') {
                    points += y;
                    sb.deleteCharAt(index - 1);
                    index--;
                } else {
                    sb.append(c);
                    index++;
                }
            }
            return sb.toString();
        }
    }

    ############

    class Solution {
        public int maximumGain(String s, int x, int y) {
            if (x < y) {
                return maximumGain(new StringBuilder(s).reverse().toString(), y, x);
            }
            int ans = 0;
            Deque<Character> stk1 = new ArrayDeque<>();
            Deque<Character> stk2 = new ArrayDeque<>();
            for (char c : s.toCharArray()) {
                if (c != 'b') {
                    stk1.push(c);
                } else {
                    if (!stk1.isEmpty() && stk1.peek() == 'a') {
                        stk1.pop();
                        ans += x;
                    } else {
                        stk1.push(c);
                    }
                }
            }
            while (!stk1.isEmpty()) {
                char c = stk1.pop();
                if (c != 'b') {
                    stk2.push(c);
                } else {
                    if (!stk2.isEmpty() && stk2.peek() == 'a') {
                        stk2.pop();
                        ans += y;
                    } else {
                        stk2.push(c);
                    }
                }
            }
            return ans;
        }
    }











####################################                  C++


class Solution {
public:
    int maximumGain(string s, int x, int y) {
        if (x < y) {
            reverse(s.begin(), s.end());
            return maximumGain(s, y, x);
        }
        int ans = 0;
        stack<char> stk1;
        stack<char> stk2;
        for (char c : s) {
            if (c != 'b')
                stk1.push(c);
            else {
                if (!stk1.empty() && stk1.top() == 'a') {
                    stk1.pop();
                    ans += x;
                } else
                    stk1.push(c);
            }
        }
        while (!stk1.empty()) {
            char c = stk1.top();
            stk1.pop();
            if (c != 'b')
                stk2.push(c);
            else {
                if (!stk2.empty() && stk2.top() == 'a') {
                    stk2.pop();
                    ans += y;
                } else
                    stk2.push(c);
            }
        }
        return ans;
    }
};
