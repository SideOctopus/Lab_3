from flask import Flask, request, jsonify
import hazelcast
import sys

app = Flask(__name__)

# Підключення до кластера Hazelcast з вказаними учасниками
hz = hazelcast.HazelcastClient(cluster_members=[
    "127.0.0.1:5701",
    "127.0.0.1:5702",
    "127.0.0.1:5703"
])

# Отримання розподіленої мапи з назвою "messages"
distributed_map = hz.get_map("messages").blocking()

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        # Обробка POST-запиту
        message = request.json['message']  # Витягнення повідомлення з JSON-тіла запиту
        key = str(len(distributed_map.key_set()) + 1)  # Генерація унікального ключа для повідомлення
        distributed_map.put(key, message)  # Збереження повідомлення у розподілену мапу
        return 'Message stored successfully'  # Повернення підтвердження успішного збереження

    elif request.method == 'GET':
        # Обробка GET-запиту
        # Отримання всіх повідомлень з розподіленої мапи
        messages = {key: distributed_map.get(key) for key in distributed_map.key_set()}
        return jsonify(messages)  # Повернення повідомлень у вигляді JSON-відповіді

if __name__ == '__main__':
    port = int(sys.argv[1])  # Отримання номера порту з аргументу командного рядка
    app.run(port=port, debug=True)  # Запуск додатка Flask на вказаному порту у режимі налагодження
