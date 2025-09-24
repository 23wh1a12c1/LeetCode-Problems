####    PYTHON3


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        neg = (numerator > 0) ^ (denominator > 0)
        if neg:
            res.append('-')
        num, d = abs(numerator), abs(denominator)
        res.append(str(num // d))
        num %= d
        if num == 0:
            return ''.join(res)
        res.append('.')
        mp = {}
        while num != 0:
            mp[num] = len(res)
            num *= 10
            res.append(str(num // d))
            num %= d
            if num in mp:
                idx = mp[num]
                res.insert(idx, '(')
                res.append(')')
                break
        return ''.join(res)



#####   JAVA


class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        boolean neg = (numerator > 0) ^ (denominator > 0);
        sb.append(neg ? "-" : "");
        long num = Math.abs((long) numerator);
        long d = Math.abs((long) denominator);
        sb.append(num / d);
        num %= d;
        if (num == 0) {
            return sb.toString();
        }
        sb.append(".");
        Map<Long, Integer> mp = new HashMap<>();
        while (num != 0) {
            mp.put(num, sb.length());
            num *= 10;
            sb.append(num / d);
            num %= d;
            if (mp.containsKey(num)) {
                int idx = mp.get(num);
                sb.insert(idx, "(");
                sb.append(")");
                break;
            }
        }
        return sb.toString();
    }
}




####     C++



using LL = long long;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        string res = "";
        bool neg = (numerator > 0) ^ (denominator > 0);
        if (neg) res += "-";
        LL num = abs(numerator);
        LL d = abs(denominator);
        res += to_string(num / d);
        num %= d;
        if (num == 0) return res;
        res += ".";
        unordered_map<LL, int> mp;
        while (num) {
            mp[num] = res.size();
            num *= 10;
            res += to_string(num / d);
            num %= d;
            if (mp.count(num)) {
                int idx = mp[num];
                res.insert(idx, "(");
                res += ")";
                break;
            }
        }
        return res;
    }
};















