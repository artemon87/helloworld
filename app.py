from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    print("'os' module added")
    return jsonify({"message": "Hello, World Back to Old!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
