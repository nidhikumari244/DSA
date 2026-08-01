class Solution {

    Map<List<Integer>, Integer> memo = new HashMap<>();

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        return dfs(price, special, needs);
    }

    private int dfs(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {

        if (memo.containsKey(needs)) {
            return memo.get(needs);
        }

        // Buy everything individually
        int minCost = 0;
        for (int i = 0; i < needs.size(); i++) {
            minCost += needs.get(i) * price.get(i);
        }

        // Try every special offer
        for (List<Integer> offer : special) {

            List<Integer> remain = new ArrayList<>();
            boolean valid = true;

            for (int i = 0; i < needs.size(); i++) {
                if (offer.get(i) > needs.get(i)) {
                    valid = false;
                    break;
                }
                remain.add(needs.get(i) - offer.get(i));
            }

            if (valid) {
                minCost = Math.min(minCost,
                        offer.get(needs.size()) + dfs(price, special, remain));
            }
        }

        memo.put(needs, minCost);
        return minCost;
    }
}
