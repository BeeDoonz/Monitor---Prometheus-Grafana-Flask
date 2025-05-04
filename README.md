# Documentação do Projeto Monitoring-demo

## Visão Geral
Projeto de monitoramento com:
- Aplicação Flask (Python)
- Prometheus (coleta de métricas)
- Grafana (visualização)
- Docker (containerização)
- CI/CD via GitHub Actions

## Tecnologias
- **Backend**: Python + Flask
- **Monitoramento**: Prometheus + Grafana
- **Infra**: Docker + Docker Compose
- **CI/CD**: GitHub Actions

## Comandos Principais
```bash
# Iniciar
docker-compose up -d

# Parar
docker-compose down

#Rebuild
docker-compose up -d --build

#Ver logs
docker-compose logs -f app
```

## Endpoints:

| Serviços | URL | 
|---|---|
| Aplicação | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000| 

## Métricas Monitoradas 

* Requisições HTTP
* Latência
* Uso de CPU/Memória
* Coleta de Lixo (GC)

## CI/CD
# Fluxo automatizado
 
 O GitHub Actions irá:

1. Build e testes
2. Scan de segurança (Trivy)
3. Deploy para Docker Hub


## Customização

* Adicionar métricas: Editar app/main.py
* Alertas: Configurar prometheus/alert.rules
* Dashboards: Adicionar JSON no Grafana

