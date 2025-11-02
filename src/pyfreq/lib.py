def count(word: str, content: str) -> dict[str, int]:
    word_count = sum(1 for w in content.split() if w == word)
    return {word: word_count}
