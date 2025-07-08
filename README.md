# Flask API + PostgreSQL + Monitoring con Prometheus & Grafana

# Flask API + PostgreSQL + Monitoring con Prometheus & Grafana

![CI/CD](https://github.com/AxelPintos95cs/devops-demo-project/actions/workflows/ci-cd.yml/badge.svg)
[![Deploy on Fly.io](https://img.shields.io/badge/Deploy-Fly.io-0884FF?logo=flydotio&logoColor=white&style=flat-square)](https://devops-demo-project.fly.dev)

---

Este proyecto demuestra una API en Flask conectada a una base de datos PostgreSQL y monitoreada con Prometheus y Grafana. Todo está contenido en Docker y puede correr localmente o adaptarse fácilmente a producción (AWS, ECS, etc).

---

## Tecnologías utilizadas

- **Flask** – microframework para la API
- **PostgreSQL** – base de datos relacional
- **Docker & Docker Compose** – contenerización de la app y sus servicios
- **Prometheus** – recolección de métricas
- **Grafana** – visualización de métricas
- **prometheus_client** – integración de métricas en Flask

---

## Cómo levantar el proyecto localmente

### 1. Clonar el repo

```bash
git clone https://github.com/tu-usuario/flask-monitoring-app.git
cd flask-monitoring-app
```

### 2. Configurar Grafana 

- Iniciar sesión en Grafana (http://localhost:3000)

- Ir a Settings > Data Sources > Add data source

- Elegir Prometheus

- Usar esta URL: http://prometheus:9090

- Guardar y continuar

- Crear un nuevo Dashboard con la métrica:
```
flask_app_requests_total
```

### Despliegue AWS (Opcional)

- Crear una instancia EC2 o usar ECS/Fargate

- Instalar Docker + Docker Compose en el host

- Subir este repo al servidor (vía Git o SCP)

- Actualizar .env con valores seguros

- Asegurar que puertos 5000, 9090 y 3000 estén abiertos (en Security Groups)

- Ejecutar docker-compose up -d para dejarlo corriendo en segundo plano

## Endpoints Disponibles

| Endpoint     | Método | Descripción                            |
| ------------ | ------ | -------------------------------------- |
| `/health`    | GET    | Verifica si la app está viva           |
| `/db-status` | GET    | Verifica conexión a PostgreSQL         |
| `/users`     | GET    | Lista todos los usuarios               |
| `/users`     | POST   | Crea un usuario (requiere JSON)        |
| `/metrics`   | GET    | Exposición de métricas para Prometheus |


## Autor
- 🧠 Axel Pintos
- 💼 SysAdmin Jr. | Python | DevOps en formación
- 🌍 Buscando oportunidades remotas

