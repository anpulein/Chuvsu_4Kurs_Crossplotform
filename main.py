from forms import *
from mixin import *
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('search'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/result', methods=["GET", "POST"])
def result():
    # Обработка полей формы
    document = get_document(request.form)

    # Выполнение поиска
    result = search_in_doc(document)
    return render_template('result.html', result=result, count=document.count)


@app.route('/request', methods=['POST'])
def json_request():
    # Обработка JSON-запроса и поиск примеров
    document = get_document(request.json)

    # Выполнение поиска
    result = search_in_doc(document)
    if result:
        response_data = {
            'sentences': result['sentences'],
            'word': document.words,
            'count': document.count,
            'from': document.min_sentence,
            'to': document.max_sentence
        }
        return jsonify(response_data)


if __name__ == '__main__':
    app.run()
