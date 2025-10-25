from ..base_matcher import BaseMatcher

class SimpleMatcher(BaseMatcher):
    def __init__(self, word_list: list[str]):
        super().__init__(word_list)

    def contains(self, text: str) -> bool:
        return any(word in text for word in self._word_list)

    def match_all(self, text: str) -> list[str]:
        return [word for word in self._word_list if word in text]

    def match_first(self, text: str) -> str | None:
        for word in self._word_list:
            if word in text:
                return word
        return None