
import logging
import time
import socket
import json
import os
from datetime import datetime

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_socket(logstash_host, logstash_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((logstash_host, logstash_port))
    except socket.gaierror:
        logger.warning(f"Could not resolve host '{logstash_host}', trying 'localhost' as fallback.")
        sock.connect(('localhost', logstash_port))
    return sock

def send_log_to_logstash():
    logstash_host = os.environ.get('LOGSTASH_HOST', 'logstash')
    logstash_port = int(os.environ.get('LOGSTASH_PORT', 5000))
    logger.info(f"Using Logstash host: {logstash_host}, port: {logstash_port}")
    while True:
        try:
            sock = create_socket(logstash_host, logstash_port)
            log_data = {
                "timestamp": datetime.now().isoformat(),
                "level": "INFO",
                "message": f"Sample log at {datetime.now()}",
                "service": "python-app"
            }
            sock.sendall((json.dumps(log_data) + "\\n").encode())
            logger.info(f"Sent log: {log_data}")
            sock.close()
            time.sleep(5)
        except Exception as e:
            logger.error(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    send_log_to_logstash()
