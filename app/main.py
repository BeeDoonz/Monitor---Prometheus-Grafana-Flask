from flask import Flask, Response
from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram
)
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Métricas Prometheus
REQUEST_COUNT = Counter(
    'app_http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_http_request_latency_seconds',
    'HTTP Request Latency',
    ['method', 'endpoint']
)

@app.route('/')
def hello():
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        REQUEST_COUNT.labels(method='GET', endpoint='/', http_status='200').inc()
        return "Hello, World! Monitoring Demo"

@app.route('/metrics')
def metrics():
    """Endpoint de métricas para o Prometheus"""
    try:
        return Response(
            generate_latest(),
            mimetype=CONTENT_TYPE_LATEST,
            headers={
                'Content-Type': CONTENT_TYPE_LATEST,
                'Cache-Control': 'no-cache, no-store, must-revalidate'
            }
        )
    except Exception as e:
        logger.error(f"Erro ao gerar métricas: {str(e)}")
        return Response(
            f"Erro ao gerar métricas: {str(e)}",
            status=500,
            content_type='text/plain'
        )
    
#@app.route('/health')
#def health():
    #"""Endpoint para healthcheck"""
    #return Response("OK", status=200, mimetype='text/plain')
    #Dando error, resolver nas próximas versões.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)