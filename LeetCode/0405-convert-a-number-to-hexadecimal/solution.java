class Solution {
    public String toHex(int num) {

        if (num == 0) {
            return "0";
        }

        String hex = "0123456789abcdef";
        StringBuilder ans = new StringBuilder();

        while (num != 0) {

            ans.append(hex.charAt(num & 15));

            num >>>= 4;
        }

        return ans.reverse().toString();
    }
}
