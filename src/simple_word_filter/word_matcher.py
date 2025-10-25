from typing import Literal
from .matchers import *


class WordMatcher:
    def __init__(
            self, word_list: list[str],
            mode: Literal['regex', 'trie', 'simple'] = 'simple',
    ):
        """初始化WordMatcher

        Args:
            word_list (list[str]): 要匹配的单词列表.
            mode (Literal['regex', 'trie', 'simple']): 使用的匹配模式，默认为'simple'。
                可选值包括：
                - 'regex': 使用正则表达式匹配器
                - 'trie': 使用Trie树匹配器
                - 'simple': 使用简单字符串匹配器
        """
        self._word_list = word_list
        if mode not in ('regex', 'trie', 'simple'):
            raise ValueError("mode must be one of 'regex', 'trie', or 'simple'.")
        if mode == 'regex':
            self._matcher = RegexMatcher(word_list)
        elif mode == 'trie':
            self._matcher = TrieMatcher(word_list)
        else:
            self._matcher = SimpleMatcher(word_list)
