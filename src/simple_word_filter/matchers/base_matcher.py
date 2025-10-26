from abc import abstractmethod


class BaseMatcher:

    _MATCHER_REGISTRY = {}

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
    

    # ======== 注册匹配器 ========
    @classmethod
    def register_matcher(cls, name: str, matcher_class: type["BaseMatcher"]) -> None:
        """注册自定义匹配器

        Args:
            name (str): 匹配器名称
            matcher_class (type[BaseMatcher]): 匹配器类，必须继承自BaseMatcher
        """
        if not issubclass(matcher_class, BaseMatcher):
            raise TypeError(f"{matcher_class} must be a subclass of BaseMatcher")
        cls._MATCHER_REGISTRY[name] = matcher_class
    
    @classmethod
    def decorate_matcher(cls, name: str):
        """装饰器方式注册自定义匹配器

        Args:
            name (str): 匹配器名称

        Returns:
            装饰器函数
        """
        def decorator(matcher_class: type[BaseMatcher]) -> type[BaseMatcher]:
            cls.register_matcher(name, matcher_class)
            return matcher_class
        return decorator
    
    @classmethod
    def available_matchers(cls) -> list[str]:
        """返回所有可用的匹配器名称"""
        return list(cls._MATCHER_REGISTRY.keys())