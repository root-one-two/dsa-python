import java.util.*;

/** Stack & Queue — Core Data Structure Implementations. */
public class Solutions {

    /** LIFO stack with O(1) push/pop/peek. */
    public static class Stack {
        private final Deque<Integer> items = new ArrayDeque<>();

        public void push(int val) { items.push(val); }
        public int pop() { return items.pop(); }
        public int peek() { return items.peek(); }
        public boolean isEmpty() { return items.isEmpty(); }
    }

    /** FIFO queue with O(1) enqueue/dequeue. */
    public static class Queue {
        private final Deque<Integer> items = new ArrayDeque<>();

        public void enqueue(int val) { items.addLast(val); }
        public int dequeue() { return items.removeFirst(); }
        public boolean isEmpty() { return items.isEmpty(); }
    }

    /** Balanced parenthesis parsing using a stack. O(n) time. */
    public static boolean isValidParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else if (pairs.containsKey(ch)) {
                if (stack.isEmpty() || stack.pop() != pairs.get(ch)) return false;
            }
        }
        return stack.isEmpty();
    }

    /** Stack supporting O(1) push, pop, top, and getMin. */
    public static class MinStack {
        private final Deque<Integer> stack = new ArrayDeque<>();
        private final Deque<Integer> mins = new ArrayDeque<>();

        public void push(int val) {
            stack.push(val);
            if (mins.isEmpty() || val <= mins.peek()) mins.push(val);
        }

        public void pop() {
            if (stack.pop().equals(mins.peek())) mins.pop();
        }

        public int top() { return stack.peek(); }
        public int getMin() { return mins.peek(); }
    }

    /** Implement queue using two stacks. Amortized O(1) enqueue/dequeue. */
    public static class MyQueue {
        private final Deque<Integer> inStack = new ArrayDeque<>();
        private final Deque<Integer> outStack = new ArrayDeque<>();

        public void push(int x) { inStack.push(x); }

        public int pop() {
            transfer();
            return outStack.pop();
        }

        public int peek() {
            transfer();
            return outStack.peek();
        }

        public boolean empty() { return inStack.isEmpty() && outStack.isEmpty(); }

        private void transfer() {
            if (outStack.isEmpty()) {
                while (!inStack.isEmpty()) outStack.push(inStack.pop());
            }
        }
    }
}
