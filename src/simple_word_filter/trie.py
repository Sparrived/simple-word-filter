class TrieTree:
    """Trie树结构"""
    def __init__(self, word_list: list[str]):
        """初始化Trie树"""
        self.root = TrieNode()
        for word in word_list:
            self.insert(word)

    def insert(self, word: str):
        """在Trie树中插入单词

        Args:
            word (str): 要插入的单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word: str) -> bool:
        """在Trie树中查找单词

        Args:
            word (str): 要查找的单词

        Returns:
            bool: 如果找到单词，则返回True；否则返回False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """在Trie树中查找前缀

        Args:
            prefix (str): 要查找的前缀

        Returns:
            bool: 如果找到前缀，则返回True；否则返回False
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def find_matching(self, text: str):
        """
        在给定文本中查找所有匹配的单词

        Args:
            text (str): 要查找的文本

        Returns:
            list[str]: 所有匹配的单词列表
        """
        results = []
        for i in range(len(text)):
            node = self.root
            for j in range(i, len(text)):
                char = text[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end_of_word:
                    results.append(node.word)
        return results

class TrieNode:
    """Trie树节点"""
    def __init__(self):
        """初始化Trie树节点"""
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word = False
        self.word = "" # 存储完整单词，减少重建时间
