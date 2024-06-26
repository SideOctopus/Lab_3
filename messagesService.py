from flask import Flask, jsonify, request

app = Flask(__name__)

messages = {}

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        # Обробка POST-запиту
        message = request.json['message']  # Отримання повідомлення з JSON-тіла запиту
        key = len(messages) + 1  # Генерація унікального ключа для повідомлення
        messages[key] = message  # Збереження повідомлення у словник
        return 'Message stored successfully'  # Повернення підтвердження успішного збереження

    elif request.method == 'GET':
        # Обробка GET-запиту
        return jsonify(messages)  # Повернення усіх збережених повідомлень у вигляді JSON

if __name__ == '__main__':
    app.run(port=5005, debug=True)
