from main import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """Testa se a rota principal retorna 'Hello, World!'"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_metrics_route(client):
    """Testa se o endpoint de métricas retorna dados"""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'python_gc_objects_collected_total' in response.data