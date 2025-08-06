class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        for (char r : ransomNote){
        int pos = magazine.find(r);
            if ( pos == string::npos){
                return false;
            }
            else{
                magazine[pos] = ' ';
            }
        }                
        return true;
    }
};
