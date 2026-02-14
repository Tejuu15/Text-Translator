from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__, template_folder='templates', static_folder='static')
translator = Translator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json() or request.form
    text = data.get('text', '')
    dest = data.get('dest', '')
    if not text or not dest:
        return jsonify({'error': 'missing text or dest'}), 400
    res = translator.translate(text, dest=dest)
    return jsonify({'text': res.text})


if __name__ == '__main__':
    app.run(debug=True)
