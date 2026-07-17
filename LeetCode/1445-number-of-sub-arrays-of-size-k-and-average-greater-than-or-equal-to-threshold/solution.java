class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        long targetSum = (long) threshold * k;
        long windowSum = 0;
        int count = 0;

        // Build the first window
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        if (windowSum >= targetSum) count++;

        // Slide the window
        for (int i = k; i < arr.length; i++) {
            windowSum += arr[i] - arr[i - k];
            if (windowSum >= targetSum) count++;
        }

        return count;
    }
}
