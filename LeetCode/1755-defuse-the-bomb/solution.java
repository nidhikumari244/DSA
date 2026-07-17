class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] result = new int[n];

        if (k == 0) return result; // all zeros

        // Determine window start and length depending on sign of k
        int start = k > 0 ? 1 : n + k;
        int absK = Math.abs(k);

        // Build the initial window sum for index 0
        int windowSum = 0;
        for (int i = 0; i < absK; i++) {
            windowSum += code[(start + i) % n];
        }

        for (int i = 0; i < n; i++) {
            result[i] = windowSum;
            // Slide the window: remove the element leaving, add the one entering
            windowSum -= code[(start + i) % n];
            windowSum += code[(start + i + absK) % n];
        }

        return result;
    }
}
