from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# Список URL-адрес, які вказують на сервіси журналювання
logging_services = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

@app.route('/data', methods=['POST', 'GET'])
def handle_data():
    if request.method == 'POST':
        # Обробка POST-запиту
        message = request.data.decode('utf-8')  # Отримання повідомлення з тіла запиту
        target_service = random.choice(logging_services)  # Вибір випадкового сервісу журналювання
        response = requests.post(f'{target_service}/data', json={'message': message})  # Відправка POST-запиту до вибраного сервісу
        return response.text  # Повернення текстової відповіді від сервісу журналювання

    elif request.method == 'GET':
        # Обробка GET-запиту
        target_service = random.choice(logging_services)  # Вибір випадкового сервісу журналювання
        response = requests.get(f'{target_service}/data')  # Відправка GET-запиту до вибраного сервісу
        return jsonify(response.json())  # Повернення JSON-відповіді від сервісу журналювання

if __name__ == '__main__':
    app.run(port=5000, debug=True)

