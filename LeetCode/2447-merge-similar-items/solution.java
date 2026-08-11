import java.util.*;

class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {

        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Add items from items1
        for (int[] item : items1) {
            map.put(item[0], map.getOrDefault(item[0], 0) + item[1]);
        }

        // Add items from items2
        for (int[] item : items2) {
            map.put(item[0], map.getOrDefault(item[0], 0) + item[1]);
        }

        // Create result
        List<List<Integer>> result = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            result.add(Arrays.asList(entry.getKey(), entry.getValue()));
        }

        return result;
    }
}
