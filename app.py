from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from test import bot_answer

app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


@app.route('/api/chat', methods=['GET'])
def chat():
    return render_template("index.html")


@app.route('/api/chat', methods=['POST'])
def hello_post():
    data = request.get_json()
    if 'message' in data:
        message = data['message']
        response = bot_answer(message)

        return jsonify(response)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
