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
        print("get data", data)
        message = data['message']
        print("get message", message)
        response = bot_answer(message)
        print("ahha")
        print(response)
        print("ahha")
        return jsonify(response)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

# comment on avait récupéré avec projet Lil Bot (a suppr ensuite si pas besoin)
# # @app.route("/get")

# def get_box_response():
#     userText = request.args.get('msg')
#     if userText=='ping':
#         return str('pong')
#     if userText=='pong':
#         return str('ping')