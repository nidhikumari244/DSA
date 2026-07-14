class Solution {
    public boolean isPalindrome(String s) {

        StringBuilder cleaned = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                cleaned.append(Character.toLowerCase(ch));
            }
        }

        String str = cleaned.toString();

        return str.equals(new StringBuilder(str).reverse().toString());
    }
}
