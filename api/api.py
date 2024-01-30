from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Route de base
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World!'})

@app.route('/api/chat', methods=['POST'])
def hello_post():
    data = request.get_json()  # Récupère les données JSON de la requête POST
    if 'message' in data:
        message = data['message']
        return jsonify({'chatbot': f'Hello, {message}!'})
    else:
        return jsonify({'error': 'Missing "name" parameter in the request body'}), 400

# Exécute l'application si ce fichier est exécuté
if __name__ == '__main__':
    app.run(debug=True)
