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


```

## 6. Endpoints de la API

La API contiene los siguientes endpoints:

### 6.1 Endpoint principal

**GET /**

Este endpoint muestra información general de la API.

**Ejemplo de respuesta:**

```json
{
  "mensaje": "API de monitoreo funcionando correctamente",
  "descripcion": "Esta API expone métricas para Prometheus y Grafana"
}
```

---

### 6.2 Endpoint de datos

**GET /api/datos**

Este endpoint retorna datos simulados de forma rápida.

**Ejemplo de respuesta:**

```json
{
  "producto": "Servicio de monitoreo",
  "estado": "activo",
  "valor": 73,
  "tiempo_respuesta": "rapido"
}
```

Este endpoint ayuda a observar solicitudes rápidas dentro del monitoreo.

---

### 6.3 Endpoint lento

**GET /api/lento**

Este endpoint simula un proceso lento que tarda entre **2 y 3 segundos**.

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Proceso lento finalizado",
  "tiempo_segundos": 2.54
}
```

Este endpoint fue creado para observar cómo cambia la latencia en Prometheus y Grafana.

---

### 6.4 Endpoint de saludo

**GET /api/saludo/Alejandra**

Este endpoint recibe un nombre y devuelve un saludo personalizado.

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Hola Alejandra, bienvenido al sistema de monitoreo"
}
```

---

### 6.5 Endpoint de error

**GET /api/error**

Este endpoint genera errores de forma aleatoria.

Algunas veces responde correctamente y otras veces responde con error HTTP 500.

**Ejemplo de respuesta exitosa:**

```json
{
  "mensaje": "Request exitoso",
  "detalle": "No ocurrió error en esta ejecución"
}
```

**Ejemplo de respuesta con error:**

```json
{
  "error": "Error simulado para pruebas de monitoreo"
}
```

Este endpoint permite analizar la tasa de errores en Grafana.

---

### 6.6 Endpoint de salud

**GET /health**

Este endpoint permite validar si la API está activa.

**Ejemplo de respuesta:**

```json
{
  "status": "UP",
  "servicio": "api-monitoreo"
}
```

---

### 6.7 Endpoint de métricas

**GET /metrics**

Este endpoint expone las métricas en formato Prometheus.

**Ejemplo de salida:**

```text
# HELP http_requests_total Total de requests HTTP recibidos
# TYPE http_requests_total counter
http_requests_total{endpoint="/api/datos",method="GET",status="200"} 5.0

# HELP http_request_duration_seconds Duración de los requests HTTP en segundos
# TYPE http_request_duration_seconds histogram

# HELP http_requests_active Número de requests activos en este momento
# TYPE http_requests_active gauge
```

Este endpoint es obligatorio porque Prometheus necesita leer las métricas desde allí.

---

## 7. Métricas implementadas

La actividad solicita implementar métricas básicas como contador de requests, latencia y requests activos. También se recomienda incluir métricas del sistema si es posible.

En este proyecto se implementaron las siguientes métricas:

### 7.1 Contador de requests totales

**http_requests_total**

Esta métrica cuenta cuántas peticiones recibe la API.

Se clasifica por:

- Método HTTP.
- Endpoint.
- Código de estado HTTP.

**Ejemplo:**

```text
http_requests_total{endpoint="/api/datos",method="GET",status="200"} 10
```

---

### 7.2 Duración de requests

**http_request_duration_seconds**

Esta métrica mide cuánto se demora cada request.

Permite identificar qué endpoints son más lentos.

---

### 7.3 Requests activos

**http_requests_active**

Esta métrica muestra cuántos requests están activos en un momento determinado.

---

### 7.4 Usuarios activos simulados

**usuarios_activos**

Esta es una métrica personalizada que simula la cantidad de usuarios activos.

---

### 7.5 Métricas del proceso de Python

También se exponen métricas propias del proceso de Python, por ejemplo:

- `process_virtual_memory_bytes`
- `process_resident_memory_bytes`
- `process_cpu_seconds_total`

Estas métricas ayudan a observar memoria y CPU del proceso.

---

## 8. Archivo docker-compose.yml

El archivo `docker-compose.yml` es el encargado de levantar los tres servicios principales del proyecto.

```yaml
services:
  api:
    build: ./Api
    container_name: api_monitoreo
    ports:
      - "3000:3000"
    networks:
      - monitoring

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus_monitoreo
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    networks:
      - monitoring
    depends_on:
      - api

  grafana:
    image: grafana/grafana:latest
    container_name: grafana_monitoreo
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana
    networks:
      - monitoring
    depends_on:
      - prometheus

networks:
  monitoring:
    driver: bridge

volumes:
  prometheus-data:
  grafana-data:
```

---

## 9. Archivo prometheus.yml

El archivo `prometheus.yml` permite configurar Prometheus para que consulte la API.

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'api-monitoreo'
    static_configs:
      - targets: ['api:3000']
```

### Explicación

#### scrape_interval: 15s

Indica que Prometheus va a consultar las métricas cada **15 segundos**.

#### targets: ['api:3000']

Indica que Prometheus debe conectarse al servicio `api` en el puerto `3000`.

Es importante usar:

```text
api:3000
```

Y no:

```text
localhost:3000
```

Porque Prometheus está dentro de un contenedor Docker.

---

## 10. Dockerfile de la API

El archivo `Dockerfile` permite construir la imagen de la API.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD ["python", "app.py"]
```

### Explicación

#### FROM python:3.11-slim

Indica que la imagen se basa en Python 3.11.

#### WORKDIR /app

Define la carpeta de trabajo dentro del contenedor.

#### COPY requirements.txt .

Copia las dependencias.

#### RUN pip install --no-cache-dir -r requirements.txt

Instala las librerías necesarias.

#### COPY app.py .

Copia el código de la API.

#### EXPOSE 3000

Expone el puerto 3000.

#### CMD ["python", "app.py"]

Ejecuta la aplicación.

---

## 11. Archivo requirements.txt

Este archivo contiene las librerías necesarias para ejecutar la API.

```txt
Flask==3.0.3
prometheus-client==0.20.0
```

---

## 12. Script de tráfico sintético

El archivo `generate_traffic.py` genera requests automáticos a los endpoints de la API.

Esto permite que Prometheus recolecte datos y que Grafana pueda mostrar gráficas con movimiento.

```python
import requests
import time
import random

BASE_URL = "http://localhost:3000"

endpoints = [
    "/",
    "/api/datos",
    "/api/lento",
    "/api/saludo/Alejandra",
    "/api/error",
    "/health"
]

print("Generando tráfico sintético hacia la API...")
print("Presiona CTRL + C para detener el script.")

try:
    while True:
        endpoint = random.choice(endpoints)
        url = BASE_URL + endpoint

        try:
            inicio = time.time()
            response = requests.get(url, timeout=5)
            duracion = round(time.time() - inicio, 3)

            print(
                f"GET {endpoint} | "
                f"Status: {response.status_code} | "
                f"Tiempo: {duracion}s"
            )

        except requests.exceptions.RequestException as error:
            print(f"Error llamando a {endpoint}: {error}")

        time.sleep(random.uniform(0.5, 2))

except KeyboardInterrupt:
    print("\nScript detenido por el usuario.")
```

---

## 13. Comandos para ejecutar el proyecto

### 13.1 Entrar a la carpeta del proyecto

```bash
cd "C:\Users\Alejandra\Desktop\Universidad\visualizacion de datos\data-monitoreo"
```

Se usan comillas porque la ruta contiene espacios.

---

### 13.2 Levantar los servicios

```bash
docker compose up -d --build
```

Este comando construye la imagen de la API y levanta los servicios.

**Resultado esperado:**

```text
api_monitoreo          Up
prometheus_monitoreo   Up
grafana_monitoreo      Up
```

---

### 13.3 Levantar sin reconstruir

Si la imagen ya está construida y hay problemas de conexión con Docker Hub, se puede usar:

```bash
docker compose up -d --no-build
```

---

### 13.4 Verificar los contenedores

```bash
docker compose ps
```

**Resultado esperado:**

```text
NAME                   STATUS
api_monitoreo          Up
prometheus_monitoreo   Up
grafana_monitoreo      Up
```

---

### 13.5 Detener los servicios

```bash
docker compose down
```

---

### 13.6 Limpiar servicios y volúmenes

```bash
docker compose down -v
```

Este comando elimina contenedores, red y volúmenes.

---

## 14. URLs del proyecto

Después de levantar los servicios, se accede a las siguientes URLs:

### API

```text
http://localhost:3000
```

### Métricas de la API

```text
http://localhost:3000/metrics
```

### Prometheus

```text
http://localhost:9090
```

### Grafana

```text
http://localhost:3001
```

### Credenciales de Grafana

**Usuario:**

```text
admin
```

**Contraseña:**

```text
admin
```

---

## 15. Consultas PromQL utilizadas

La actividad solicita abrir Prometheus y ejecutar al menos dos consultas PromQL durante la demostración.

En este proyecto se usaron las siguientes consultas:

### 15.1 Verificar si Prometheus está leyendo la API

```promql
up
```

**Resultado esperado:**

```text
up{instance="api:3000", job="api-monitoreo"} 1
```

Si el resultado es `1`, significa que Prometheus está conectado correctamente a la API.

---

### 15.2 Requests por segundo por endpoint

```promql
sum by (endpoint) (rate(http_requests_total[1m]))
```

Esta consulta muestra la cantidad de requests por segundo agrupados por endpoint.

---

### 15.3 Latencia promedio

```promql
rate(http_request_duration_seconds_sum[1m])
/
rate(http_request_duration_seconds_count[1m])
```

Esta consulta muestra el tiempo promedio de respuesta de la API.

---

### 15.4 Errores 500

```promql
sum(rate(http_requests_total{status=~"5.."}[1m]))
```

Esta consulta muestra la tasa de errores HTTP 500.

---

## 16. Dashboard en Grafana

Se creó un dashboard llamado:

```text
Dashboard Monitoreo API
```

El dashboard contiene tres paneles principales.

---

### 16.1 Panel 1: Requests por segundo por endpoint

**Consulta usada:**

```promql
sum by (endpoint) (rate(http_requests_total[1m]))
```

Este panel permite ver qué endpoints reciben más tráfico.

---

### 16.2 Panel 2: Latencia promedio de la API

**Consulta usada:**

```promql
rate(http_request_duration_seconds_sum[1m])
/
rate(http_request_duration_seconds_count[1m])
```

Este panel permite observar el tiempo promedio de respuesta de la API.

Durante la prueba se evidenció que el endpoint `/api/lento` tiene mayor latencia porque fue diseñado para demorarse entre **2 y 3 segundos**.

---

### 16.3 Panel 3: Tasa de errores 500

**Consulta usada:**

```promql
sum(rate(http_requests_total{status=~"5.."}[1m]))
```

Este panel permite observar errores del servidor.

El endpoint `/api/error` fue creado para generar algunos errores de forma aleatoria y así poder monitorearlos.

---

## 17. Proceso realizado paso a paso

### 17.1 Creación de la estructura del proyecto

Primero se creó la carpeta principal `data-monitoreo`.

Dentro de esta carpeta se crearon los archivos y carpetas necesarios:

```text
docker-compose.yml
Api
prometheus
generate_traffic.py
README.md
```

---

### 17.2 Desarrollo de la API

Se creó una API usando Flask.

La API contiene diferentes endpoints para simular una aplicación real.

También se agregó el endpoint `/metrics`, que es el que usa Prometheus para recolectar información.

---

### 17.3 Instrumentación de métricas

Se implementaron métricas usando `prometheus-client`.

Las métricas principales fueron:

- Contador de requests.
- Histograma de duración de requests.
- Gauge de requests activos.
- Gauge de usuarios activos simulados.
- Métricas del proceso de Python.

---

### 17.4 Configuración de Docker

Se creó un `Dockerfile` para empaquetar la API dentro de un contenedor.

Luego se creó `docker-compose.yml` para levantar la API, Prometheus y Grafana al mismo tiempo.

---

### 17.5 Configuración de Prometheus

Se creó el archivo `prometheus.yml`.

Este archivo le indica a Prometheus que debe leer las métricas desde:

```text
api:3000
```

---

### 17.6 Configuración de Grafana

Se accedió a Grafana desde:

```text
http://localhost:3001
```

Luego se configuró Prometheus como fuente de datos usando la URL:

```text
http://prometheus:9090
```

Después se creó el dashboard con tres paneles.

---

### 17.7 Generación de tráfico sintético

Se creó el script `generate_traffic.py`.

Este script llama automáticamente a diferentes endpoints de la API.

Gracias a este tráfico, Prometheus puede recolectar datos y Grafana puede mostrar gráficas.

---

## 18. Errores encontrados durante el desarrollo y solución aplicada

Durante el desarrollo del proyecto se presentaron varios errores. A continuación se documentan los más importantes.

---

### 18.1 Error: ModuleNotFoundError: No module named 'requests'

**Error presentado:**

```text
ModuleNotFoundError: No module named 'requests'
```

**Causa:**

Este error apareció al ejecutar el script `generate_traffic.py`.

La causa fue que la librería `requests` no estaba instalada en el Python local de Windows.

**Solución:**

Se instaló la librería usando:

```bash
python -m pip install requests
```

Después de instalarla, el script se pudo ejecutar correctamente.

---

### 18.2 Error: empty compose file

**Error presentado:**

```text
empty compose file
```

**Causa:**

Este error ocurrió porque el archivo `docker-compose.yml` estaba vacío o no tenía el contenido correcto.

**Solución:**

Se revisó el archivo `docker-compose.yml` y se pegó la configuración correcta de los servicios:

- API.
- Prometheus.
- Grafana.

Después de guardar correctamente el archivo, Docker Compose pudo leerlo.

## 19. Validación final del funcionamiento

Para validar el proyecto se ejecutó el siguiente comando:

```bash
docker compose ps
```

**Resultado esperado:**

```text
api_monitoreo          Up
prometheus_monitoreo   Up
grafana_monitoreo      Up
```

También se validaron las siguientes URLs:

```text
http://localhost:3000
http://localhost:3000/metrics
http://localhost:9090
http://localhost:3001
```

---

## 20. Resultado final en Prometheus

En Prometheus se ejecutó la siguiente consulta:

```promql
up
```

El resultado esperado fue:

```text
up{instance="api:3000", job="api-monitoreo"} 1
```

Esto confirmó que Prometheus estaba conectado correctamente con la API.

También se ejecutó la siguiente consulta:

```promql
sum by (endpoint) (rate(http_requests_total[1m]))
```

Esta consulta permitió ver las peticiones por segundo agrupadas por endpoint.

---

## 21. Resultado final en Grafana

En Grafana se creó un dashboard con tres paneles principales:

- Requests por segundo por endpoint.
- Latencia promedio de la API.
- Tasa de errores 500.

Con estos paneles se pudo observar el comportamiento de la API en tiempo real.

El panel de **requests** muestra qué endpoints reciben más tráfico.

El panel de **latencia** permite identificar qué endpoint tarda más en responder.

El panel de **errores** permite identificar fallos simulados de la API.

---

## 22. Análisis de resultados

Durante la ejecución del proyecto se observó que el endpoint `/api/lento` genera mayor latencia que los demás endpoints.

Esto es esperado porque este endpoint fue diseñado para simular un proceso lento de **2 a 3 segundos**.

También se observó que el endpoint `/api/error` puede generar errores HTTP 500 de forma aleatoria.

Esto permitió visualizar una tasa de errores dentro del dashboard de Grafana.

Gracias al monitoreo, fue posible identificar:

- Qué endpoints reciben más tráfico.
- Qué endpoints tienen mayor tiempo de respuesta.
- Cuándo se generan errores.
- Si la API está activa.
- Si Prometheus está recolectando métricas correctamente.

## 23. Conclusión final

Este proyecto permitió construir desde cero una solución básica de monitoreo.

Se creó una **API REST**, se instrumentaron métricas, se configuró **Prometheus** para recolectarlas y se creó un dashboard en **Grafana** para visualizarlas.

Además, durante el proceso se solucionaron varios errores reales relacionados con:

- Dependencias de Python.
- Docker.
- Prometheus.
- Archivos YAML.
- Conectividad entre contenedores.

Esto permitió comprender no solo el resultado final, sino también el proceso técnico necesario para hacer funcionar una arquitectura de monitoreo completa.

En conclusión, el proyecto permitió aplicar de forma práctica conceptos importantes de monitoreo, observabilidad, contenedores y visualización de métricas, logrando una solución funcional donde la API genera información, Prometheus la recolecta y Grafana la presenta de manera gráfica para facilitar el análisis del comportamiento del sistema.
