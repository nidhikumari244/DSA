class Solution {
public:
    static constexpr int MOD = 1'000'000'007;

    int possibleStringCount(string word, int k) {
        int n = word.size();
        vector<int> runs(1, 1);
        for (int i = 1; i < n; ++i) {
            if (word[i] == word[i-1]) runs.back()++;
            else runs.push_back(1);
        }

        long long total = 1;
        for (int len : runs) {
            total = total * len % MOD;
        }

        int m = runs.size();
        if (m >= k) {
            return total; // each group gives at least one char => all combos are valid :contentReference[oaicite:1]{index=1}
        }

        vector<int> dp(k), ndp(k), ps(k);
        dp[0] = 1;

        for (int len : runs) {
            ps[0] = dp[0];
            for (int i = 1; i < k; ++i)
                ps[i] = (ps[i-1] + dp[i]) % MOD;

            for (int i = 1; i < k; ++i) {
                int right = ps[i-1];
                int left = (i - 1 - len >= 0) ? ps[i-1-len] : 0;
                ndp[i] = (right - left + MOD) % MOD;
            }
            swap(dp, ndp);
            fill(ndp.begin(), ndp.end(), 0);
        }

        long long invalid = 0;
        for (int i = 0; i < k; ++i) invalid = (invalid + dp[i]) % MOD;

        return (total - invalid + MOD) % MOD;
    }
};

