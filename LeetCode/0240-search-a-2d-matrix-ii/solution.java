class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int col = matrix[0].length - 1;  // Start at top-right corner
        
        while (row < matrix.length && col >= 0) {
            int curr = matrix[row][col];
            
            if (curr == target) {
                return true;
            } else if (curr > target) {
                col--;  // Too big → go left
            } else {
                row++;  // Too small → go down
            }
        }
        
        return false;
    }
}
