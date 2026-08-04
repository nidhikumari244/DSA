class Solution {
    public int numTeams(int[] rating) {

        int n = rating.length;
        int teams = 0;

        for (int j = 0; j < n; j++) {

            int leftSmaller = 0;
            int leftGreater = 0;
            int rightSmaller = 0;
            int rightGreater = 0;

            // Count left side
            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j])
                    leftSmaller++;
                else
                    leftGreater++;
            }

            // Count right side
            for (int k = j + 1; k < n; k++) {
                if (rating[k] > rating[j])
                    rightGreater++;
                else
                    rightSmaller++;
            }

            teams += leftSmaller * rightGreater;
            teams += leftGreater * rightSmaller;
        }

        return teams;
    }
}
