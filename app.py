from flask import Flask, request
import requests
import os

app = Flask(__name__)

S20_API_KEY = os.environ.get("S20_API_KEY")
BASE_URL = "https://kiberonekaliningrad.s20.online/api/v2"

HEADERS = {
    "X-APP-KEY": S20_API_KEY,
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return "Server is running"

@app.route("/s20-hook", methods=["POST"])
def s20_hook():
    data = request.json
    print("Webhook received:", data)

    # Проверяем, что это обновление урока
    if data.get("entity") != "Lesson":
        return "Not a lesson", 200

    lesson_id = data.get("entity_id")

    # 1️⃣ Получаем данные урока
    lesson_response = requests.get(
        f"{BASE_URL}/lesson/{lesson_id}",
        headers=HEADERS
    )

    print("Lesson API status:", lesson_response.status_code)

    if lesson_response.status_code != 200:
        print("Lesson API error:", lesson_response.text)
        return "Lesson fetch error", 200

    lesson = lesson_response.json()
    print("Lesson data:", lesson)

    return "OK", 200
