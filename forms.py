from typing import List


class Document():
    def __init__(self, book: str, words: List[str], min_sentence: int, max_sentence: int, count: int):
        self.book = book
        self.words = words
        self.min_sentence = min_sentence
        self.max_sentence = max_sentence
        self.count = count
