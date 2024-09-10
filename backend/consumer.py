from kafka import KafkaConsumer
import json
import psycopg2
import os

db = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST', 'postgres'),
    user=os.environ.get('POSTGRES_USER', 'root'),
    password=os.environ.get('POSTGRES_PASSWORD', 'rootpassword'),
    dbname=os.environ.get('POSTGRES_DB', 'orders_db')
)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255),
    quantity INTEGER
)
""")
db.commit()

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=[os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order_processing_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_order(order):
    print(f"Processing order: {order}")
    product = order['product']
    quantity = order['quantity']
    cursor.execute("INSERT INTO orders (product, quantity) VALUES (%s, %s)", (product, quantity))
    db.commit()
    print(f"Order saved to database: {product}, {quantity}")

print("Starting consumer...")
for message in consumer:
    order = message.value
    process_order(order)