class Solution {
public:
    bool isPalindrome(string s) {
    for (int left = 0, right = s.size() - 1; left < right;) {
        if (!isalnum(s[left])) { ++left; continue; }
        if (!isalnum(s[right])) { --right; continue; }

        if (tolower(s[left]) != tolower(s[right])) return false;

        ++left;
        --right;
    }
    return true;
}

};

