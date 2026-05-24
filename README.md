# Actividad: Monitoreo y Observabilidad con Docker, Prometheus y Grafana

## Información del estudiante

**Nombre:** Alejandra  
**Código:** [Escribe aquí tu código de estudiante]  
**Repositorio GitHub:** [Pega aquí el enlace del repositorio]  
**Video demostrativo:** [Pega aquí el enlace del video]  

---

# 1. Introducción

Este proyecto corresponde a la actividad de **Monitoreo y Observabilidad**, en la cual se debía construir una solución completa usando Docker, Prometheus y Grafana.

La actividad solicita implementar una API REST con mínimo 3 endpoints, exponer métricas en formato Prometheus, configurar Prometheus para recolectar esas métricas, crear un dashboard en Grafana y generar tráfico sintético para analizar el comportamiento de la aplicación. Además, la entrega debe incluir un repositorio en GitHub y un video demostrativo de máximo 5 minutos. :contentReference[oaicite:0]{index=0}

Para este proyecto se desarrolló una API REST en Python usando Flask. Esta API expone diferentes endpoints y un endpoint especial llamado `/metrics`, que permite que Prometheus lea las métricas del sistema.

Posteriormente, Prometheus recolecta esas métricas y Grafana las muestra gráficamente en un dashboard.

---

# 2. Objetivo del proyecto

El objetivo principal de este proyecto es aprender cómo se monitorea una aplicación en tiempo real.

Con este proyecto se busca entender:

- Cómo crear una API REST básica.
- Cómo ejecutar servicios usando Docker.
- Cómo usar Docker Compose para levantar varios contenedores.
- Cómo exponer métricas desde una API.
- Cómo configurar Prometheus para recolectar métricas.
- Cómo crear dashboards en Grafana.
- Cómo generar tráfico sintético para observar el comportamiento de la aplicación.
- Cómo interpretar métricas como requests por segundo, latencia y errores.

---

# 3. Herramientas utilizadas

Para el desarrollo de esta actividad se utilizaron las siguientes herramientas:

## 3.1 Python

Se utilizó Python como lenguaje de programación principal para construir la API REST.

## 3.2 Flask

Flask es un framework ligero de Python que permite crear APIs de forma sencilla.

En este proyecto se usó Flask para crear endpoints como:

- `/`
- `/api/datos`
- `/api/lento`
- `/api/error`
- `/health`
- `/metrics`

## 3.3 Prometheus Client

Se usó la librería `prometheus-client` para crear y exponer métricas en formato compatible con Prometheus.

## 3.4 Docker

Docker permite ejecutar aplicaciones en contenedores. En este proyecto se usó para ejecutar la API, Prometheus y Grafana.

## 3.5 Docker Compose

Docker Compose permite levantar varios servicios al mismo tiempo mediante un archivo llamado `docker-compose.yml`.

En este proyecto se levantan tres servicios:

- API
- Prometheus
- Grafana

## 3.6 Prometheus

Prometheus es una herramienta de monitoreo que recolecta métricas de las aplicaciones.

En este proyecto Prometheus consulta el endpoint `/metrics` de la API cada 15 segundos.

## 3.7 Grafana

Grafana es una herramienta de visualización que permite crear dashboards.

En este proyecto se creó un dashboard con tres paneles principales:

- Requests por segundo por endpoint.
- Latencia promedio de la API.
- Tasa de errores 500.

---

# 4. Estructura del proyecto

La estructura final del proyecto es la siguiente:

```text
data-monitoreo/
├── docker-compose.yml
├── README.md
├── Api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── prometheus/
│   └── prometheus.yml
└── generate_traffic.py
