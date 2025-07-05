class Solution {
public:
    char nextChar(char ch) {
        return ch == 'z' ? 'a' : ch + 1;
    }

    char kthCharacter(int k) {
        string s = "a";

        while (s.length() < k) {
            string temp;
            for (char c : s) {
                temp += nextChar(c);
            }
            s += temp;
        }

        return s[k - 1];  // k is 1-based
    }
};

