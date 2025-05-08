public class Solution {
    public int RomanToInt(string s) {
        var dict = new Dictionary<string, int>(){
            {"I", 1},
            {"V", 5},
            {"X", 10},
            {"L", 50},
            {"C", 100},
            {"D", 500},
            {"M", 1000},
            {"IV", 4},
            {"IX", 9},
            {"XL", 40},
            {"XC", 90},
            {"CD", 400},
            {"CM", 900},
        };

        int total = 0;
        int i = 0;
        while (i < s.Length){
            if(i<s.Length -1 && dict[s[i].ToString()] < dict[s[i+1].ToString()]){
                var t = $"{s[i]}{s[i+1]}";
                total += dict[t];
                i += 2;
            }
            else {
                total += dict[s[i].ToString()];
                i += 1;
            }
        }
        return total;
    }
}