public class Solution {
    public bool IsPalindrome(int x) {
        var y = x.ToString().ToCharArray();
        Array.Reverse(y);
        return x.ToString() == new string(y);
    }
}