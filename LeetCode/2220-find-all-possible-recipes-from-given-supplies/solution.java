import java.util.*;

class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {

        Map<String, List<String>> graph = new HashMap<>();
        Map<String, Integer> indegree = new HashMap<>();

        // Initialize indegree for every recipe
        for (String recipe : recipes) {
            indegree.put(recipe, 0);
        }

        // Build graph and indegree
        for (int i = 0; i < recipes.length; i++) {
            for (String ingredient : ingredients.get(i)) {
                graph.computeIfAbsent(ingredient, k -> new ArrayList<>()).add(recipes[i]);
                indegree.put(recipes[i], indegree.get(recipes[i]) + 1);
            }
        }

        Queue<String> queue = new LinkedList<>();

        // Initial supplies
        for (String supply : supplies) {
            queue.offer(supply);
        }

        List<String> ans = new ArrayList<>();

        while (!queue.isEmpty()) {
            String item = queue.poll();

            if (!graph.containsKey(item))
                continue;

            for (String recipe : graph.get(item)) {
                indegree.put(recipe, indegree.get(recipe) - 1);

                if (indegree.get(recipe) == 0) {
                    ans.add(recipe);
                    queue.offer(recipe);
                }
            }
        }

        return ans;
    }
}
