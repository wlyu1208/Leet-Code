class Solution {
    public boolean backspaceCompare(String s, String t) {
        return getString(s).equals(getString(t));
    }
    
    public String getString(String input) {
        StringBuilder result = new StringBuilder();
        int skip = 0;
        for (int i=input.length()-1; i >= 0; i--) {
            char c = input.charAt(i);

            if (c=='#') {
                skip++;
            }
            else{
                if (skip > 0) {
                    skip--; 
                }
                else {
                    result.append(c);
                }
            }
        }
        return result.toString();
    }
}