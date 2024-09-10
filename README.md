# E-Commerce Kafka Pipeline with KRaft Mode

This project demonstrates the usage of Apache Kafka in KRaft mode (without Zookeeper) in an e-commerce context. It showcases a simple order processing system using Kafka's new KRaft consensus protocol, providing a practical example of Kafka's latest features in a microservices architecture.

## Project Overview

The application consists of:
- A React frontend for placing orders
- A Flask backend that acts as a Kafka producer
- A Kafka broker running in KRaft mode
- A Python consumer that processes orders and stores them in PostgreSQL
- A PostgreSQL database for order storage

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Start the application:
   ```
   docker-compose up --build
   ```

   This command will build and start all necessary containers. The first run may take several minutes as it downloads and builds the required images.

3. Once all services are up and running, you can access the frontend at:
   ```
   http://localhost:3000
   ```

4. To stop the application, use:
   ```
   docker-compose down
   ```

## Using the Application

1. Open your web browser and navigate to `http://localhost:3000`.
2. You'll see a simple interface where you can select a product and enter a quantity.
3. Click "Place Order" to submit an order.
4. The order will be sent to the Kafka topic and then processed by the consumer, which will store it in the PostgreSQL database.

## Viewing the Data

To view the processed orders in the PostgreSQL database:

1. Connect to the PostgreSQL container:
   ```
   docker-compose exec postgres psql -U root -d orders_db
   ```

2. Once in the PostgreSQL shell, you can query the orders table:
   ```sql
   SELECT * FROM orders;
   ```

## Architecture Details

- **Frontend (React)**: Provides a user interface for placing orders.
- **Backend (Flask)**: Receives orders from the frontend and produces messages to Kafka.
- **Kafka**: Runs in KRaft mode, demonstrating Kafka's ability to operate without Zookeeper.
- **Consumer (Python)**: Consumes messages from Kafka and stores them in PostgreSQL.
- **PostgreSQL**: Stores the processed orders.

## Key Features

- Demonstration of Kafka's KRaft mode, showcasing Kafka's latest capabilities for consensus management without Zookeeper.
- Microservices architecture with clear separation of concerns.
- Docker-based setup for easy deployment and scaling.
- Real-time order processing pipeline.

## Troubleshooting

If you encounter any issues:
1. Ensure all required ports are free (3000, 5000, 9092, 5432).
2. Check container logs using `docker-compose logs <service-name>`.
3. Ensure your Docker installation is up-to-date.
