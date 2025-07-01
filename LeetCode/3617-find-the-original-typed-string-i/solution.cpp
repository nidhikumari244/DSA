class Solution {
public:
    int possibleStringCount(std::string word) {
        int total = 1;
        for (int i = 0; word[i]; ) {
            int j = i;
            while (word[j] == word[i]) j++;
            int len = j - i;
            if (len > 1) {
                total += (len - 1);
            }
            i = j;
        }
        return total;
    }
};

