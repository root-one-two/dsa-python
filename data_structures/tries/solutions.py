"""Tries — prefix tree insert, search, and root replacement."""

from typing import Dict, List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    """Prefix tree. Insert/search/starts_with are O(length of the query)."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


def replace_words(dictionary: List[str], sentence: str) -> str:
    """Replace each word with the shortest dictionary root. O(total chars)."""
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    def shortest_root(word: str) -> str:
        node = trie.root
        prefix: List[str] = []
        for ch in word:
            if ch not in node.children:
                return word
            node = node.children[ch]
            prefix.append(ch)
            if node.is_word:
                return "".join(prefix)
        return word

    return " ".join(shortest_root(word) for word in sentence.split())
