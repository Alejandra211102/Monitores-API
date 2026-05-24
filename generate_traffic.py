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