import java.util.*;

class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {

        if (hand.length % groupSize != 0) {
            return false;
        }

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int card : hand) {
            map.put(card, map.getOrDefault(card, 0) + 1);
        }

        Arrays.sort(hand);

        for (int card : hand) {

            if (map.get(card) == 0) {
                continue;
            }

            for (int i = 0; i < groupSize; i++) {

                int current = card + i;

                if (map.getOrDefault(current, 0) == 0) {
                    return false;
                }

                map.put(current, map.get(current) - 1);
            }
        }

        return true;
    }
}
