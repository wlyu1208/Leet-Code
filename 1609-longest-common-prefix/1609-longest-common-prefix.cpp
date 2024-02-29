class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        int len;
        
        if (strs.size() == 0) {
            return ""
        }
        
        for (len = 0; len < strs[0].size(); len++) {
            for (int i = 1; i < strs.size(); i++) {
                if (len >= strs[i].size() || strs[i][len] != strs[0][len]) 
                    break;
            }
            
            if (i != strs.size()) {
                break;
            }
        }
        
        return strs[0].substr(0, len);
    }
};