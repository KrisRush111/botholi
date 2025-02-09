from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для взаимодействия с фронтендом

# Хранилище пользователей
users = {}

@app.route("/save_user", methods=["POST"])
def save_user():
    data = request.json
    user_id = data.get("id")
    user_name = data.get("name")

    if user_id and user_name:
        users[user_id] = user_name
        return jsonify({"message": "User saved!"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route("/get_user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    name = users.get(user_id, "Гость")  # Если нет данных, отдаем "Гость"
    return jsonify({"name": name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
