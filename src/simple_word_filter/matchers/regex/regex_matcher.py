import re
from ..base_matcher import BaseMatcher

@BaseMatcher.matcher("regex")
class RegexMatcher(BaseMatcher):
    def __init__(self, word_list: list[str]):
        super().__init__(word_list)
        # 转义特殊字符并构建正则表达式
        escaped_words = [re.escape(word) for word in word_list]
        self.pattern = re.compile('|'.join(escaped_words))
    
    def match_all(self, text: str) -> list[tuple[str, int]]:
        """返回所有匹配的单词及其索引"""
        return [(match.group(), match.start()) for match in self.pattern.finditer(text)]
    
    def match_first(self, text: str) -> tuple[str, int] | None:
        """返回第一个匹配的单词及其索引"""
        match = self.pattern.search(text)
        return (match.group(), match.start()) if match else None