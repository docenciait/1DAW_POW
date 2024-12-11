# Unidad 3: Lenguaje de Scripting para SEO:

Comenzaremos con una seria de recursos libres para poder aprender Python de forma rápida y sencilla. Después de esto aprenderemos el framework Django, muy sencillo porque incluye ORM, Autenticación y otros componentes para comenzar el desarrollo de Python y Django:

1. [Aprende Python desde cero a experto](https://github.com/jvadillo/aprende-python-desde-cero-a-experto)
2. [Curso de Python Udemy](https://github.com/hektorprofe/curso-python-udemy)
3. [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python)

https://www.jcchouinard.com/python-for-seo/

# Python para SEO


## Script de medición de segundos de acceso a la web:"

```python
import time
import requests

def get_response_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    print(f"Tiempo de respuesta para {url}: {end_time - start_time:.2f} segundos")

URL = "https://vite-react-kappa-self.vercel.app/"
get_response_time(URL)
```


### Script velocidad dns

```python
import socket
import time

def dns_resolution_time(domain):
    start_time = time.time()
    try:
        socket.gethostbyname(domain)
        end_time = time.time()
        print(f"Tiempo de resolución DNS para {domain}: {end_time - start_time:.4f} segundos")
    except socket.error:
        print(f"No se pudo resolver {domain}")

dns_resolution_time("https://vite-react-kappa-self.vercel.app/")

```