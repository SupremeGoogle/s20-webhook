from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/s20-hook", methods=["POST"])
def s20_hook():
    data = request.json
    print("Webhook received:", data)
    return "OK", 200
