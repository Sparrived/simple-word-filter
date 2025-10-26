
# simple-word-filter

`simple-word-filter` 是一个轻量、可扩展的 Python 敏感词过滤库，内置多种匹配算法，可快速集成到文本审核或内容过滤场景中。

## 主要特性

- **多种匹配模式**：内置 `simple`、`regex`、`trie` 三种匹配器，按需取舍准确性与性能。
- **可扩展架构**：通过装饰器即可注册自定义匹配器，满足特殊匹配策略。
- **统一 API**：`contains`、`match_all`、`match_first`、`replace` 等方法在各匹配器间保持一致。
- **性能自测**：提供 `WordFilter.matcher_speed_test`，快速评估不同匹配器的运行效率。
- **现代 Python**：基于 3.10+ 类型注解，易读、易维护。

## 环境要求

- Python 3.10 及以上

## 安装

```bash
pip install simple-word-filter
```

## 快速上手

```python
from simple_word_filter import WordFilter

blocked = ["敏感词", "违禁品", "badword"]
wf = WordFilter(blocked, mode="trie")

text = "这是一段包含敏感词的文本"

wf.contains(text)
# True

wf.match_all(text)
# [('敏感词', 4)]

wf.replace(text, repl_char="*")
# '这是一段包含***的文本'
```

### 选择匹配模式

| 模式     | 适用场景 | 特点 |
|----------|----------|------|
| `simple` | 词库较小、实现最简洁 | 顺序扫描文本，易理解，性能中等 |
| `regex`  | 需要正则表达式能力 | 支持复杂模式匹配，灵活但构造成本较高 |
| `trie`   | 词库较大、追求性能 | 基于 Trie 树，查询效率高 |

可调用 `BaseMatcher.available_matchers()` 查看当前可用模式。

```python
from simple_word_filter import BaseMatcher

print(BaseMatcher.available_matchers())
# ['simple', 'regex', 'trie']
```

### 自定义匹配器

```python
from simple_word_filter import BaseMatcher

@BaseMatcher.matcher("suffix")
class SuffixMatcher(BaseMatcher):
	def match_all(self, text: str):
		matches = []
		for word in self._word_list:
			if text.endswith(word):
				matches.append((word, len(text) - len(word)))
		return matches

	def match_first(self, text: str):
		return self.match_all(text)[0] if self.match_all(text) else None

# 注册后即可像内置模式一样使用
```

### 性能快速评估

```python
from simple_word_filter import WordFilter

best_filter = WordFilter.matcher_speed_test(
	word_list=["foo", "bar", "baz"],
	sample_words=["foo", "bar", "baz", "qux"],
)

print(best_filter.mode)
# 依据测试结果输出运行最快的模式
```

## 开发者指南

```bash
git clone https://github.com/Sparrived/simple-word-filter.git
cd simple-word-filter
uv sync --dev  # 或使用 pip 安装开发依赖
```

运行测试：

```bash
pytest
```

## 发布流程

仓库已配置 GitHub Actions。向 `master` 推送包含 `src/simple_word_filter/__init__.py` 中 `__version__` 变更的提交后，将自动：

1. 构建发布包并上传到 GitHub Release（标签 `v<version>`）。
2. 将同一制品上传到 PyPI。

也可在 GitHub 上手动触发 `Upload Python Package` workflow。

## 许可证

MIT License © [Sparrived](https://github.com/Sparrived)

