from ..base_matcher import BaseMatcher

@BaseMatcher.decorate_matcher("simple")
class SimpleMatcher(BaseMatcher):
    def __init__(self, word_list: list[str]):
        super().__init__(word_list)

    def match_all(self, text: str) -> list[tuple[str, int]]:
        """返回所有匹配的单词及其索引"""
        matches = []
        for word in self._word_list:
            index = 0
            while True:
                index = text.find(word, index)
                if index == -1:
                    break
                matches.append((word, index))
                index += 1
        return matches

    def match_first(self, text: str) -> tuple[str, int] | None:
        """返回第一个匹配的单词及其索引"""
        earliest_index = len(text)
        earliest_word = None
        
        for word in self._word_list:
            index = text.find(word)
            if index != -1 and index < earliest_index:
                earliest_index = index
                earliest_word = word
        
        return (earliest_word, earliest_index) if earliest_word else None