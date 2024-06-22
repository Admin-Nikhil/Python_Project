# Python_Project

### Installation

1. **Clone the repository:**
	```bash
    	git clone https://github.com/Admin-Nikhil/Python_Project.git
	cd Python_Project/MQTT_Mongo
    ```
	
2. **Install the required Python packages:**
	pip install paho-mqtt pika pymongo flask


### Running the Scripts
1. **Start RabbitMQ**:

    Ensure RabbitMQ is running and the MQTT plugin is enabled.

2. **Start MongoDB**:

    Ensure MongoDB is running.

3. **Run the MQTT Client**:

    ```bash
    python client.py
    ```

    This will start emitting messages every second.

4. **Run the MQTT Server**:

    ```bash
    python server.py
    ```

    This will start processing and storing messages. 
	AND
    This will start the API server on `http://localhost:5000`.

### Testing the API Endpoint

You can test the endpoint using curl or Postman. Replace the timestamps with appropriate Unix timestamps.

```bash
curl "http://127.0.0.1:5000/status_count?start=1719063445&end=1719063460"

