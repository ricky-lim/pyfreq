from pyfreq.lib import count


def test_count_word():
    word = "python"
    content = """
Why python developers don't get bitten?
Because python has no fangs, just indentation errors.
Life is short, use python!
"""

    assert {"python": 2} == count(word, content)


def test_count_non_existent_word():
    word = "rust"
    content = """
Why Python developers don't get bitten?
Because python has no fangs, just indentation errors.
Life is short, use Python!
"""
    assert {"rust": 0} == count(word, content)
