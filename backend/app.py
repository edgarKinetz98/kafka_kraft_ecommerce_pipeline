from flask import Flask, request, jsonify
from kafka import KafkaProducer
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/order', methods=['POST'])
def place_order():
    order = request.json
    producer.send('orders', order)
    return jsonify({"message": "Order placed successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)