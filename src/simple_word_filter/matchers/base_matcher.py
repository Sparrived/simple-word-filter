from abc import abstractmethod


class BaseMatcher:
    def __init__(self, word_list: list[str]):
        self._word_list = word_list


    def contains(self, text: str) -> bool:
        """给定文本是否存在匹配的单词

        Args:
            text (str): 要查找的文本

        Returns:
            如果找到匹配的单词，则返回True；否则返回False
        """

        return False if self.match_first(text) else True

    @abstractmethod
    def match_all(self, text: str) -> list[tuple[str, int]]:
        """给定文本返回所有匹配的单词以及它们的索引

        Args:
            text (str): 要查找的文本

        Returns:
            所有匹配的单词及其在文本中的索引
        """
        raise NotImplementedError()
    
    @abstractmethod
    def match_first(self, text: str) -> tuple[str, int] | None:
        """给定文本返回第一个匹配到的单词及其索引

        Args:
            text (str): 要查找的文本

        Returns:
            第一个匹配的单词及其在文本中的索引，如果没有匹配，则返回None
        """
        raise NotImplementedError()