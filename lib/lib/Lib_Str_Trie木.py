#title#
# Trie木
#subtitle#
# Trie: 複数の文字列の共通接頭辞を検索する O(？)

#name#
# Trie木
#description#
# Trie木クラス
#body#
# https://atcoder.jp/contests/abc353/tasks/abc353_e

import sys
sys.setrecursionlimit(10001000)

class TrieNode:
    def __init__(self) -> None:
        self.parent: TrieNode | None = None
        self.children: set = {}
        self.is_end_of_word: bool = False
        self.child_count: int = 0
        """以下追加"""
        self.count: int = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        """以下追加"""
        self.ans = 0

    def insert(self, word: str, *args: tuple) -> TrieNode:
        node = self._insert(word)
        self._insert_extra_ope(node, *args)
        return node

    def exists_word(self, word: str) -> bool:
        rsearch = self.find(word)
        if rsearch is None:
            return False
        return rsearch.is_end_of_word

    def exists_prefix(self, prefix: str) -> bool:
        rsearch = self.find(prefix)
        if rsearch is None:
            return False
        return True

    def _insert(self, word: str) -> TrieNode:
        node = self.root
        node.child_count += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node.children[char].parent = node
            node = node.children[char]
            self.ans += node.child_count
            node.child_count += 1
        node.is_end_of_word = True
        return node

    def find(self, word: str) -> TrieNode | None:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    """以下追加"""

    def _insert_extra_ope(self, node: TrieNode, *args: tuple) -> None:
        # somethig to operate inserted node
        return

tree = Trie()
N = int(input())
for s in input().split():
    tree.insert(s)

    print(tree.ans)

#prefix#
# Lib_Str_共通接頭辞_Trie木
#end#
