import re
import json


class Document:
    def __init__(self, file_name, target_words, example_minimum_length, example_maximum_length, number_of_examples):
        self.file_name = file_name
        self.target_words = target_words
        self.example_minimum_length = example_minimum_length
        self.example_maximum_length = example_maximum_length
        self.number_of_examples = number_of_examples


# Функция, которая считывает параметры поиска из файла "request.json"
def read_json(filename):
    with open(filename, "r") as request_file:
        return json.load(request_file)


# Функция, которая конфигурирует параметры
def config_document(request_data):
    return Document(**request_data)


# Функция, которая читает текст с файла книги
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as book:
        return book.read()


# Функция, которая записывает реузльтат в response.json
def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as response:
        json.dump(data, response, ensure_ascii=False, indent=4)

    print("Примеры использовани найдены и сохранены в файле 'response.json!")


# Функция, которая ищет слова представленные с json
def find_words(text, document, filename):
    examples = []
    paragraph_pattern = r"(.*?)[.!?]\s+"

    for word in document.target_words:
        word_examples = re.findall(paragraph_pattern, text, re.DOTALL)
        word_examples = [example.strip() for example in word_examples
                         if document.example_minimum_length <= len(
                example) <= document.example_maximum_length and word in example]
        examples.extend(word_examples[:document.number_of_examples])

    response_data = {
        "examples": examples
    }

    write_json(filename, response_data)


r_filename = "request.json"
w_filename = "response.json"

document = config_document(read_json(r_filename))
book = read_text(document.file_name)
find_words(book, document, w_filename)
