class Solution {

    public List<Integer> findClosestElements(int[] arr, int k, int x) {

        int left = 0;
        int right = arr.length - k;

        // Binary search to find the starting index of the window
        while (left < right) {

            int mid = left + (right - left) / 2;

            // Compare the distances of the two possible windows
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Collect the k closest elements
        List<Integer> ans = new ArrayList<>();

        for (int i = left; i < left + k; i++) {
            ans.add(arr[i]);
        }

        return ans;
    }
}
