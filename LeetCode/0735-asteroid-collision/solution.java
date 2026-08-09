import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {

            boolean alive = true;

            // Collision is possible only:
            // stack top > 0 and current asteroid < 0
            while (alive && !stack.isEmpty()
                    && stack.peek() > 0
                    && asteroid < 0) {

                if (stack.peek() < -asteroid) {
                    // Stack asteroid is smaller, so it explodes
                    stack.pop();

                } else if (stack.peek() == -asteroid) {
                    // Both are equal, so both explode
                    stack.pop();
                    alive = false;

                } else {
                    // Current asteroid is smaller, so it explodes
                    alive = false;
                }
            }

            if (alive) {
                stack.push(asteroid);
            }
        }

        // Convert stack to array
        int[] result = new int[stack.size()];

        for (int i = stack.size() - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
}
