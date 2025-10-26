"""Simple Word Filter - 一个简单的Python词过滤库

这个库提供了多种词匹配算法,用于文本中的敏感词检测和过滤。

主要类:
    - WordMatcher: 词匹配器的高级封装
    - BaseMatcher: 所有匹配器的基类
    - TrieMatcher: 基于Trie树的高效匹配器
    - SimpleMatcher: 简单字符串匹配器
    - RegexMatcher: 基于正则表达式的匹配器

基本用法:
    >>> from simple_word_filter import WordMatcher
    >>> matcher = WordMatcher(['敏感词', '违禁词'])
    >>> matcher.contains('这是一段包含敏感词的文本')
    True
"""

__version__ = "1.0.1"
__author__ = "Sparrived"
__email__ = "sparrived@outlook.com"
__license__ = "MIT"

# 导出主要的公共API
from .word_filter import WordFilter
from .matchers.base_matcher import BaseMatcher
from .matchers.trie.trie_matcher import TrieMatcher
from .matchers.simple.simple_matcher import SimpleMatcher
from .matchers.regex.regex_matcher import RegexMatcher

__all__ = [
    # 版本信息
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    # 主要类
    "WordFilter",
    "BaseMatcher",
    "TrieMatcher",
    "SimpleMatcher",
    "RegexMatcher",
]

