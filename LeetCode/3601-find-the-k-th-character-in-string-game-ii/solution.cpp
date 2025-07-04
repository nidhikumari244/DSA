class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int n = operations.size();
        vector<long long> lengths(n + 1);
        lengths[0] = 1;

        // Step 1: Precompute length after each operation
        for (int i = 0; i < n; ++i) {
            if (lengths[i] > k) {
                lengths[i + 1] = k + 1;
            } else {
                lengths[i + 1] = min(k + 1, lengths[i] * 2);
            }
        }

        // Step 2: Reverse simulate
        for (int i = n - 1; i >= 0; --i) {
            if (k <= lengths[i]) continue;

            k -= lengths[i];

            if (operations[i] == 1) {
                char ch = kthCharacter(k, operations);
                return (ch == 'z') ? 'a' : ch + 1;
            }
        }

        return 'a'; // Base case
    }
};

