import pytest
from simple_word_filter import WordFilter, BaseMatcher

@pytest.fixture
def word_list() -> list[str]:
    return ["badword1", "badword2", "badword3"]

def test_matchers_decorator() -> None:
    available_matchers = BaseMatcher.available_matchers()
    assert "simple" in available_matchers
    assert "regex" in available_matchers
    assert "trie" in available_matchers
