from forms import *
from typing import List, Dict
from nltk import sent_tokenize


def get_document(data) -> Document:
    return Document(
        book=data['book'],
        words=data['words'].split(',') if ',' in data['words'] else [data['words']],
        min_sentence=int(data['from']) if 'from' in data else 1,
        max_sentence=int(data['to']) if 'to' in data else 50,
        count=int(data['count'])
    )


def is_sentence(sentence: str, document: Document) -> bool:
    if (document.min_sentence < len(sentence) < document.max_sentence) and all(
            word.lower() in sentence.lower() for word in document.words):
        return True
    return False


def search_in_doc(document: Document) -> Dict[str, List[str]]:
    sentences = []

    with open(document.book + '.txt') as file:
        text = sent_tokenize(file.read())
        for sentence in text:
            if (is_sentence(sentence, document)) and len(sentences) < document.count:
                sentences.append(sentence)

        return {'sentences': sentences }
