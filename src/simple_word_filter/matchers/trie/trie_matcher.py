from .trie import TrieTree
from ..base_matcher import BaseMatcher

@BaseMatcher.matcher("trie")
class TrieMatcher(BaseMatcher):
    def __init__(self, word_list: list[str]):
        super().__init__(word_list)
        self.trie = TrieTree(word_list)

    def match_all(self, text: str) -> list[tuple[str, int]]:
        return self.trie.find_all_matching(text)

    def match_first(self, text: str) -> tuple[str, int] | None:
        return self.trie.find_first_matching(text)