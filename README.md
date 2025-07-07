# DevOps Demo Project

Este es un proyecto de demostración que integra:
- Aplicación Python Flask
- Docker
- CI/CD con GitHub Actions
- Despliegue con Terraform en AWS EC2

## Cómo correr localmente

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
