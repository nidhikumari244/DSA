class Solution {
    //  remove the duplicates 

    public String removeDuplicateLetters(String s) {

        int[] last = new int[26];

        // Store the last occurrence of each character
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }

        Stack<Character> stack = new Stack<>();
        boolean[] visited = new boolean[26];

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            // Skip if already present in stack
            if (visited[ch - 'a'])
                continue;

            // Remove larger characters that appear later
            while (!stack.isEmpty()
                    && stack.peek() > ch
                    && last[stack.peek() - 'a'] > i) {

                visited[stack.pop() - 'a'] = false;
            }

            stack.push(ch);
            visited[ch - 'a'] = true;
        }

        // Build answer
        StringBuilder ans = new StringBuilder();

        for (char c : stack) {
            ans.append(c);
        }

        return ans.toString();
    }
}
