from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/chat', methods=['GET'])
def chat():
    return render_template("index.html")

@app.route('/api/chat', methods=['POST'])
def hello_post():
    print("ahha")
    print(request.get_json())
    data = request.get_json()
    if 'message' in data:
        message = data['message']
        return render_template("index.html")
       # ici il faudra retourner la vraie reponse du chatbot et la donner au front (faire une nouvelle requete qui va donner)
       # return jsonify({'chatbot': f'Hello, {message}!'})

    else:
        return render_template("index.html")

        # return jsonify({'error': 'Missing "message" parameter in the request body'}), 400


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
