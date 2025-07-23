# ELK Logging Stack with Python Application

This project demonstrates a simple logging pipeline using the ELK stack (Elasticsearch, Logstash, Kibana) and a Python application that sends logs to Logstash over TCP. The stack is orchestrated using Docker Compose for easy setup and management.

## Project Structure

```
ELK-Logging stack/
├── app/
│   ├── Dockerfile
│   ├── logger.py
│   └── requirements.txt
├── logstash/
│   └── logstash.conf
└── docker-composer.yml
```

## Components

### 1. Python Application (`app/logger.py`)
- Periodically sends JSON-formatted log messages to Logstash over TCP (port 5000).
- Configurable Logstash host and port via environment variables (`LOGSTASH_HOST`, `LOGSTASH_PORT`).
- Includes error handling for DNS and connection issues.

### 2. Logstash (`logstash/logstash.conf`)
- Listens for TCP input on port 5000 with the `json` codec.
- Forwards logs to Elasticsearch, creating daily indices (`app-logs-YYYY.MM.dd`).

### 3. Elasticsearch
- Stores logs received from Logstash.
- Runs as a single-node cluster with security disabled for development.

### 4. Kibana
- Provides a web UI for searching and visualizing logs stored in Elasticsearch.

### 5. Docker Compose (`docker-composer.yml`)
- Orchestrates all services: Elasticsearch, Logstash, Kibana, and the Python app.
- Ensures correct service dependencies and networking.

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup & Usage

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd ELK-Logging stack
   ```

2. **Ensure folder names match**
   - The folder for Logstash config should be `logstash` (not `logstach`).

3. **Start the stack**
   ```sh
   docker-compose -f docker-composer.yml up --build
   ```
   This will build the Python app image and start all services.

4. **Access Kibana**
   - Open [http://localhost:5601](http://localhost:5601) in your browser.
   - (screenshot/ img width="1898" height="1014" alt="image" src="https://github.com/user-attachments/assets/c2990ab0-8384-4a5b-bbfb-4d03749964ea")
   - Configure an index pattern (e.g., `app-logs-*`) to view logs.

5. **Logs**
   - The Python app sends a log every 5 seconds to Logstash.
   - Logstash forwards logs to Elasticsearch.
   - View logs in Kibana's Discover tab.

## Configuration

- **Python App Environment Variables:**
  - `LOGSTASH_HOST`: Hostname of the Logstash service (default: `logstash`)
  - `LOGSTASH_PORT`: Port for Logstash TCP input (default: `5000`)

- **Logstash Config (`logstash/logstash.conf`):**
  - Listens on TCP port 5000 for JSON logs.
  - Forwards to Elasticsearch at `elasticsearch:9200`.

- **Elasticsearch & Kibana:**
  - Default ports: 9200 (Elasticsearch), 5601 (Kibana)
  - (screenshot2/ img width="834" height="515" alt="image" src="https://github.com/user-attachments/assets/f4a7cb52-4e0e-4685-9b51-a0392ce8a8a7")
  - Security is disabled for development.
## Docker Containers.
   (screenshot3/ img width="1547" height="334" alt="image" src="https://github.com/user-attachments/assets/7e0cceed-3255-4fb4-a681-015b4b2a2cff")

## Troubleshooting

- **Connection Refused / Name or Service Not Known:**
  - Ensure all services are running and on the same Docker network.
  - Check that the Logstash service is named correctly and listening on port 5000.
  - The Python app will retry connections and fall back to `localhost` if DNS fails.

- **Kibana Not Showing Logs:**
  - Make sure the index pattern matches (`app-logs-*`).
  - Check Logstash and Elasticsearch logs for errors.

## License
This project is for educational and demonstration purposes.


