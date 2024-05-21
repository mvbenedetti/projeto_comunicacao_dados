from flask import Flask, request
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:9092')

@app.route('/message', methods=['POST'])
def send_message():
    message = request.json
    producer.send('test', str(message).encode('utf-8'))
    return 'Message sent to Kafka', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
