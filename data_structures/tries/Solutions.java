import java.util.*;

/** Tries — prefix tree insert, search, and root replacement. */
public class Solutions {

    static class TrieNode {
        final Map<Character, TrieNode> children = new HashMap<>();
        boolean isWord;
    }

    /** Prefix tree. Insert/search/startsWith are O(length of the query). */
    public static class Trie {
        private final TrieNode root = new TrieNode();

        public void insert(String word) {
            TrieNode node = root;
            for (char ch : word.toCharArray()) {
                node = node.children.computeIfAbsent(ch, k -> new TrieNode());
            }
            node.isWord = true;
        }

        public boolean search(String word) {
            TrieNode node = walk(word);
            return node != null && node.isWord;
        }

        public boolean startsWith(String prefix) {
            return walk(prefix) != null;
        }

        String shortestRoot(String word) {
            TrieNode node = root;
            StringBuilder prefix = new StringBuilder();
            for (char ch : word.toCharArray()) {
                node = node.children.get(ch);
                if (node == null) return word;
                prefix.append(ch);
                if (node.isWord) return prefix.toString();
            }
            return word;
        }

        private TrieNode walk(String s) {
            TrieNode node = root;
            for (char ch : s.toCharArray()) {
                node = node.children.get(ch);
                if (node == null) return null;
            }
            return node;
        }
    }

    /** Replace each word with the shortest dictionary root. O(total chars). */
    public static String replaceWords(List<String> dictionary, String sentence) {
        Trie trie = new Trie();
        for (String word : dictionary) trie.insert(word);
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            words[i] = trie.shortestRoot(words[i]);
        }
        return String.join(" ", words);
    }
}
