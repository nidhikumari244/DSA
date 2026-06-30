class Solution {
    public String frequencySort(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) {
            count[c]++;
        }

        Character[] chars = new Character[128];
        for (int i = 0; i < 128; i++) chars[i] = (char) i;

        Arrays.sort(chars, (a, b) -> count[b] - count[a]);

        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            for (int i = 0; i < count[c]; i++) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
