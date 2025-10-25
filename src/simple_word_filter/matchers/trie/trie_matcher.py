from .trie import TrieTree
from ..base_matcher import BaseMatcher


class TrieMatcher(BaseMatcher):
    def __init__(self, word_list: list[str]):
        super().__init__(word_list)
        self.trie = TrieTree(word_list)

    def contains(self, text):
        return self.trie.search(text)

    def match_all(self, text):
        return self.trie.find_all_matching(text)

    def match_first(self, text):
        return self.trie.find_first_matching(text)