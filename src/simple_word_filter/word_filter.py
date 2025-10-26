from typing import Literal
from .matchers import *

class WordFilter:
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
        self._mode = mode
        
        # 从 BaseMatcher 的注册表获取匹配器类
        matcher_class = BaseMatcher._MATCHER_REGISTRY.get(mode)
        if matcher_class is None:
            available_modes = ', '.join(f"'{m}'" for m in BaseMatcher._MATCHER_REGISTRY.keys())
            raise ValueError(f"mode must be one of {available_modes}, got '{mode}'.")
        
        self._matcher : BaseMatcher = matcher_class(word_list)

    # ======== 属性方法 ========
    @property
    def mode(self) -> str:
        """返回当前使用的匹配模式"""
        return self._mode
    

    # ======== 功能实现 ========
    def replace(self, text: str, repl_char: str = '*') -> str:
        """替换文本中所有匹配的单词为指定字符

        Args:
            text (str): 要处理的文本
            repl_char (str): 用于替换的字符，默认为 '*'

        Returns:
            替换后的文本
        """
        matches = self.match_all(text)
        if not matches:
            return text
        
        # 按索引排序匹配项，防止替换时索引混乱
        matches.sort(key=lambda x: x[1])
        
        result = []
        last_index = 0
        
        for word, index in matches:
            result.append(text[last_index:index])
            result.append(repl_char * len(word))
            last_index = index + len(word)
        
        result.append(text[last_index:])
        
        return ''.join(result)


    # ======== 代理方法 ========
    def contains(self, text: str) -> bool:
        """检查文本中是否包含匹配的单词"""
        return self._matcher.contains(text)
    
    def match_all(self, text: str) -> list[tuple[str, int]]:
        """返回所有匹配的单词及其索引"""
        return self._matcher.match_all(text)
    
    def match_first(self, text: str) -> tuple[str, int] | None:
        """返回第一个匹配的单词及其索引"""
        return self._matcher.match_first(text)
    

    # ======== API 方法 ========
    @classmethod
    def matcher_speed_test(
        cls, 
        word_list: list[str], 
        sample_words: list[str], 
        max_k: int = 5
    ) -> "WordFilter":
        """快速测试不同匹配器的性能表现，并选出性能最高的匹配器
        Args:
            word_list (list[str]): 要匹配的单词列表
            sample_words (list[str]): 用于生成测试文本的样本单词列表
            max_k (int): 每段测试文本中包含的单词数量上限，默认为5
        Returns:
            使用最快匹配器的WordMatcher实例
        """
        import time
        test_text = ''
        k = min(max_k, len(sample_words))
        from random import choices
        for _ in range(1000):
            test_text += f'这是一段包含{"、".join(choices(sample_words, k=k))}和其他内容的测试文本，用于性能测试。'

        # 使用注册表动态获取所有匹配器
        matchers: list[WordFilter] = [
            cls(word_list, name)
            for name in BaseMatcher._MATCHER_REGISTRY.keys()
        ]

        best_matcher = None
        best_time = float('inf')

        for matcher in matchers:
            start_time = time.time()
            matcher.match_all(test_text)
            elapsed_time = time.time() - start_time
            if elapsed_time < best_time:
                best_time = elapsed_time
                best_matcher = matcher

        return best_matcher