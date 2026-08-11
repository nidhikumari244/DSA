import java.util.*;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> {
                if (a[0] != b[0]) {
                    return a[0] - b[0];
                }
                return a[1] - b[1];
            }
        );

        // Add every row to the min heap
        for (int i = 0; i < mat.length; i++) {

            int soldiers = 0;

            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 1) {
                    soldiers++;
                }
            }

            pq.offer(new int[]{soldiers, i});
        }

        int[] result = new int[k];

        // Get k weakest rows
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll()[1];
        }

        return result;
    }
}
