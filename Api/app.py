from flask import Flask, jsonify, request, Response
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    ProcessCollector,
    PlatformCollector
)
import time
import random

app = Flask(__name__)

# Registro personalizado de métricas
registry = CollectorRegistry()

# Métricas del proceso de Python, como CPU y memoria
ProcessCollector(registry=registry)
PlatformCollector(registry=registry)

# Contador de requests totales
http_requests_total = Counter(
    "http_requests_total",
    "Total de requests HTTP recibidos",
    ["method", "endpoint", "status"],
    registry=registry
)

# Histograma para medir duración de requests
http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "Duración de los requests HTTP en segundos",
    ["method", "endpoint"],
    registry=registry
)

# Gauge para saber cuántos requests están activos
http_requests_active = Gauge(
    "http_requests_active",
    "Número de requests activos en este momento",
    registry=registry
)

# Gauge personalizado para simular usuarios activos
usuarios_activos = Gauge(
    "usuarios_activos",
    "Cantidad simulada de usuarios activos",
    registry=registry
)


@app.before_request
def before_request():
    """
    Esta función se ejecuta antes de cada request.
    Guarda el tiempo inicial y aumenta el contador de requests activos.
    """
    request.start_time = time.time()
    http_requests_active.inc()


@app.after_request
def after_request(response):
    """
    Esta función se ejecuta después de cada request.
    Calcula cuánto se demoró la petición y guarda las métricas.
    """
    request_latency = time.time() - request.start_time
    endpoint = request.path

    http_request_duration_seconds.labels(
        method=request.method,
        endpoint=endpoint
    ).observe(request_latency)

    http_requests_total.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code
    ).inc()

    http_requests_active.dec()

    return response


@app.route("/")
def home():
    """
    Endpoint principal de la API.
    """
    return jsonify({
        "mensaje": "API de monitoreo funcionando correctamente",
        "descripcion": "Esta API expone métricas para Prometheus y Grafana",
        "endpoints": [
            "/",
            "/api/datos",
            "/api/lento",
            "/api/saludo/<nombre>",
            "/api/error",
            "/health",
            "/metrics"
        ]
    })


@app.route("/api/datos")
def obtener_datos():
    """
    Endpoint rápido que retorna datos simulados.
    """
    datos = {
        "producto": "Servicio de monitoreo",
        "estado": "activo",
        "valor": random.randint(1, 100),
        "tiempo_respuesta": "rapido"
    }

    usuarios_activos.set(random.randint(5, 50))

    return jsonify(datos)


@app.route("/api/lento")
def endpoint_lento():
    """
    Endpoint que simula un proceso lento.
    Se demora entre 2 y 3 segundos.
    """
    tiempo_espera = random.uniform(2, 3)
    time.sleep(tiempo_espera)

    return jsonify({
        "mensaje": "Proceso lento finalizado",
        "tiempo_segundos": round(tiempo_espera, 2)
    })


@app.route("/api/saludo/<nombre>")
def saludo(nombre):
    """
    Endpoint que recibe un nombre y responde con un saludo.
    """
    return jsonify({
        "mensaje": f"Hola {nombre}, bienvenido al sistema de monitoreo"
    })


@app.route("/api/error")
def simular_error():
    """
    Endpoint que a veces genera error.
    Sirve para probar métricas de errores.
    """
    numero = random.randint(1, 10)

    if numero <= 3:
        return jsonify({
            "error": "Error simulado para pruebas de monitoreo"
        }), 500

    return jsonify({
        "mensaje": "Request exitoso",
        "detalle": "No ocurrió error en esta ejecución"
    })


@app.route("/health")
def health():
    """
    Endpoint para revisar si la API está viva.
    """
    return jsonify({
        "status": "UP",
        "servicio": "api-monitoreo"
    })


@app.route("/metrics")
def metrics():
    """
    Endpoint obligatorio para Prometheus.
    Aquí se exponen todas las métricas.
    """
    return Response(
        generate_latest(registry),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)