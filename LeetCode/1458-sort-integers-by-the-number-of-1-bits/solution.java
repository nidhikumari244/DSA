class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];
        
        Arrays.sort(boxed, (a, b) -> {
            int bitsA = Integer.bitCount(a);
            int bitsB = Integer.bitCount(b);
            return bitsA != bitsB ? bitsA - bitsB : a - b;
        });
        
        for (int i = 0; i < arr.length; i++) arr[i] = boxed[i];
        return arr;
    }
}
