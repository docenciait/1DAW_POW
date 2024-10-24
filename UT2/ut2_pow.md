# UT2. Auditoría Técnica SEO con Lenguaje Dinámico y HTML


### Etiquetas HTML para SEO Técnico 
 
1. **`<title>`: Título de la página** 
  - Esta etiqueta define el título que se muestra en los resultados de búsqueda y en la pestaña del navegador.

  - Debe ser único, relevante y contener las palabras clave principales.
 
  - Ejemplo: `<title>Guía de SEO Técnico en HTML y Python</title>`
 
2. **`<meta name="description">`: Descripción meta** 
  - Proporciona un resumen breve de la página. Aunque no influye directamente en el ranking, puede mejorar el CTR (Click Through Rate) si es atractiva.

  - Debe tener entre 150-160 caracteres e incluir la palabra clave.
 
  - Ejemplo: `<meta name="description" content="Aprende SEO técnico utilizando etiquetas HTML y Python para mejorar la optimización de tu sitio web.">`
 
3. **`<meta name="robots">`: Directivas para rastreo** 
  - Indica a los motores de búsqueda si pueden indexar o seguir los enlaces de la página.
 
  - Valores comunes: `index, follow` (permitir rastreo e indexación) o `noindex, nofollow` (bloquear rastreo e indexación).
 
  - Ejemplo: `<meta name="robots" content="index, follow">`
 
4. **`<h1>`, `<h2>`, `<h3>`: Encabezados jerárquicos**  
  - Las etiquetas de encabezado ayudan a estructurar el contenido de la página. El `<h1>` debería usarse para el título principal, mientras que los demás (`<h2>`, `<h3>`, etc.) para subtítulos.

  - Los encabezados deben reflejar la estructura lógica del contenido y contener palabras clave relevantes.
 
  - Ejemplo:

```html
<h1>SEO Técnico para Desarrolladores Web</h1>
<h2>Optimización del HTML</h2>
<h3>Uso de las etiquetas meta</h3>
```
 
5. **`<img alt="texto descriptivo">`: Atributo alt de imágenes** 
  - Ayuda a los motores de búsqueda a entender el contenido de las imágenes, ya que no pueden "verlas" como lo haría un humano.

  - Incluye palabras clave relacionadas con la imagen y el contenido.
 
  - Ejemplo: `<img src="seo-html-python.jpg" alt="Guía de SEO Técnico utilizando HTML y Python">`
 
6. **`<link rel="canonical">`: URL canónica** 
  - Evita problemas de contenido duplicado al indicar a los motores de búsqueda la URL preferida si hay múltiples páginas con contenido similar.
 
  - Ejemplo: `<link rel="canonical" href="https://www.miweb.com/seo-tecnico.html">`
 
7. **`<meta name="viewport">`: Adaptabilidad móvil** 
  - Indica que el diseño de la página es responsivo, lo cual es un factor importante en SEO técnico, ya que los motores de búsqueda como Google priorizan sitios optimizados para móviles.
 
  - Ejemplo: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
 
8. **`<script>`: Carga de scripts** 
  - Es recomendable diferir la carga de JavaScript cuando no sea crítico para la funcionalidad, para mejorar la velocidad de carga, que es un factor importante de SEO.
 
  - Ejemplo: `<script src="script.js" defer></script>`
 
9. **`<link rel="stylesheet">`: Carga de hojas de estilo**  
  - Para mejorar la velocidad de carga, usa hojas de estilo externas y optimiza su tamaño. Puedes utilizar el atributo `media="print"` para diferir la carga de CSS no crítico.
 
  - Ejemplo: `<link rel="stylesheet" href="styles.css" media="print">`
 
10. **`<meta charset="UTF-8">`: Codificación de caracteres** 
  - Es importante especificar la codificación de caracteres para asegurar que el contenido se muestra correctamente en todos los dispositivos.
 
  - Ejemplo: `<meta charset="UTF-8">`
 
11. **Enlaces internos (URLs limpias y accesibles)** 
  - Los enlaces dentro de tu página deben ser descriptivos, cortos y contener palabras clave. Usa URLs limpias y legibles tanto por humanos como por bots de búsqueda.
 
  - Ejemplo: `<a href="/guia-seo-tecnico">Guía de SEO Técnico</a>`

### Cómo Python puede ayudar en el SEO Técnico 

Python es muy útil en SEO técnico para automatizar procesos de análisis y optimización. Aquí algunos ejemplos:
 
1. **Análisis del contenido HTML:** 
Python puede analizar el código fuente HTML de un sitio web y extraer datos clave como títulos, descripciones, encabezados y otras etiquetas para asegurarse de que cumplen con las mejores prácticas de SEO.

```python
from bs4 import BeautifulSoup
import requests

# Cargar el contenido de una página
url = 'https://www.miweb.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer el título
title = soup.title.string
print(f"Título: {title}")

# Extraer meta description
description = soup.find('meta', attrs={'name': 'description'})['content']
print(f"Descripción: {description}")
```
 
2. **Detección de enlaces rotos:** 
Python puede ayudarte a detectar enlaces rotos en tu sitio, los cuales afectan negativamente al SEO.

```python
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def check_broken_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener todos los enlaces
    for link in soup.find_all('a'):
        href = link.get('href')
        full_url = urljoin(url, href)

        try:
            link_response = requests.get(full_url)
            if link_response.status_code != 200:
                print(f"Enlace roto: {full_url} - Código: {link_response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error en enlace: {full_url} - {e}")

# Ejemplo
check_broken_links('https://www.miweb.com')
```
 
3. **Análisis de la velocidad de carga:** 
Python también puede analizar la velocidad de carga utilizando herramientas como `Google Lighthouse` a través de su API, lo que te permitirá optimizar elementos como scripts, imágenes, etc.
 
4. **Sitemaps y robots.txt:**  
  - Python puede generar automáticamente archivos `robots.txt` y `sitemaps.xml` para mejorar el rastreo y la indexación de tu sitio.

Ejemplo de generación de un sitemap:


```python
from xml.etree.ElementTree import Element, SubElement, tostring

def generate_sitemap(url_list):
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in url_list:
        url_tag = SubElement(urlset, 'url')
        loc = SubElement(url_tag, 'loc')
        loc.text = url

    sitemap = tostring(urlset, encoding='utf8', method='xml').decode('utf8')
    with open('sitemap.xml', 'w') as f:
        f.write(sitemap)

# Ejemplo
urls = ['https://www.miweb.com/', 'https://www.miweb.com/seo-tecnico']
generate_sitemap(urls)
```

### Conclusión 

El SEO técnico requiere un enfoque tanto en la estructura HTML como en la optimización del rendimiento y la accesibilidad de tu sitio web. Python es una excelente herramienta para automatizar procesos repetitivos como el análisis de contenido, la detección de errores y la generación de archivos importantes como sitemaps, ayudando a optimizar el rendimiento de tu página en los motores de búsqueda.


El uso de Python para analizar el SEO de un sitio web a través de herramientas como `SEO Analyzer` automatiza el proceso de identificación de mejoras técnicas y de contenido. A continuación, te explicaré cómo usar `seo-analyzer`, una librería de Python diseñada para analizar varios aspectos del SEO de una página web, y te mostraré ejemplos para su uso.Instalación del paquete `seo-analyzer`
Primero, debes instalar la librería utilizando pip. Si aún no la tienes, puedes instalarla con el siguiente comando:


```bash
pip install seo-analyzer
```
Uso básico de `seo-analyzer`El `seo-analyzer` puede analizar tanto sitios web completos como archivos HTML individuales para identificar problemas de SEO técnico, como la falta de etiquetas importantes, el rendimiento, y los enlaces rotos.
#### Ejemplo 1: Análisis básico de una URL 

En este ejemplo, haremos un análisis SEO básico de un sitio web.


```python
from seoanalyzer import analyze

# Analizar una página web por URL
url = 'https://www.miweb.com'
results = analyze(url)

# Imprimir los resultados del análisis
print(results)
```
Este script descargará el contenido de la URL proporcionada, revisará aspectos clave como etiquetas de encabezado (`<h1>`, `<h2>`, etc.), descripciones, títulos y otros aspectos técnicos importantes para el SEO. Los resultados incluirán información sobre:
- Enlaces rotos.
 
- Problemas con las etiquetas HTML (`<title>`, `<meta>`, etc.).
 
- Imágenes sin atributo `alt`.

- Análisis de palabras clave.

#### Ejemplo 2: Análisis de un archivo HTML local 
Puedes usar `seo-analyzer` para analizar un archivo HTML local. Esto es útil si estás trabajando en un sitio que aún no ha sido publicado.

```python
from seoanalyzer import analyze_file

# Analizar un archivo HTML local
file_path = 'ruta/a/archivo.html'
results = analyze_file(file_path)

# Imprimir los resultados del análisis
print(results)
```

Este método realiza el mismo tipo de análisis que el anterior, pero en un archivo HTML local. La salida incluye los mismos detalles de SEO: etiquetas, enlaces rotos, imágenes, etc.

#### Ejemplo 3: Análisis con resultados detallados y palabras clave 
`seo-analyzer` también permite realizar un análisis de las palabras clave que aparecen en el contenido de una página, identificando la densidad de las palabras clave y la relevancia del contenido.

```python
from seoanalyzer import analyze

# Analizar una página web por URL y mostrar más detalles
url = 'https://www.miweb.com'
results = analyze(url, with_content=True, with_anchors=True, with_metas=True)

# Imprimir los resultados del análisis
print(results)

# Extraer y mostrar las palabras clave
for keyword, count in results['keywords'].items():
    print(f"Palabra clave: {keyword} - Frecuencia: {count}")
```
En este análisis detallado, `with_content=True`, `with_anchors=True`, y `with_metas=True` indican que quieres extraer y analizar el contenido, los enlaces (anchors) y las meta etiquetas (descripciones, títulos, etc.).
#### Ejemplo 4: Generación de un informe SEO en formato JSON 

En caso de que desees guardar los resultados del análisis en un archivo JSON para un análisis posterior o para compartir el informe, puedes hacerlo de la siguiente manera:


```python
import json
from seoanalyzer import analyze

# Analizar la página web
url = 'https://www.miweb.com'
results = analyze(url)

# Guardar los resultados en un archivo JSON
with open('seo_report.json', 'w') as json_file:
    json.dump(results, json_file)

print("Informe SEO guardado en 'seo_report.json'")
```

Este ejemplo guardará los resultados del análisis SEO en un archivo JSON que puede ser fácilmente compartido o procesado posteriormente.

### Resultados obtenidos 

Los resultados del análisis incluyen varios aspectos relacionados con el SEO técnico y de contenido:
 
- **Palabras clave** : Análisis de las palabras clave más comunes en la página.
 
- **Enlaces rotos** : Listado de enlaces que están rotos o devuelven códigos de error.
 
- **Imágenes** : Verificación de que todas las imágenes tengan etiquetas `alt`.
 
- **Estructura del sitio** : Análisis de la estructura del contenido, como el uso de encabezados (`<h1>`, `<h2>`, etc.).
 
- **Meta información** : Verificación de la presencia y relevancia de las meta etiquetas, como el título y la descripción.

### Otras alternativas en Python 
Además de `seo-analyzer`, existen otras herramientas o librerías en Python que pueden ayudarte a analizar el SEO de una página: 
1. **BeautifulSoup**  y **requests** : Utilizados para realizar análisis SEO personalizado, extrayendo y analizando etiquetas específicas, como se mostró en la primera parte.
 
2. **Lighthouse (a través de Puppeteer)** : Lighthouse es una herramienta de auditoría de sitios web, y puedes integrarla en Python utilizando Puppeteer para evaluar aspectos como SEO, accesibilidad y rendimiento.
 
3. **Screaming Frog SEO Spider API** : Aunque es una herramienta externa, puedes interactuar con la API de Screaming Frog desde Python para realizar análisis SEO masivos.

### Conclusión 
`seo-analyzer` es una herramienta sencilla pero poderosa para realizar análisis SEO técnico y de contenido en Python. Aunque no es tan robusta como algunas soluciones comerciales, te permite automatizar el análisis SEO de tus páginas y generar informes detallados.

You: 

haz una práctica de una página y cómo aplicar seo técnico

ChatGPT: 

Voy a crear una práctica completa sobre cómo aplicar SEO técnico en una página HTML utilizando buenas prácticas en el código, junto con un ejemplo en Python para analizar el SEO de la página. Esta práctica guiará al estudiante para que comprenda y aplique conceptos clave del SEO técnico a nivel de HTML y realice un análisis automatizado con Python.

### Práctica: Optimización SEO Técnica de una Página HTML 

#### Objetivo 

El objetivo de esta práctica es que los estudiantes aprendan a aplicar las mejores prácticas de SEO técnico utilizando etiquetas HTML apropiadas y, posteriormente, analizar la página utilizando una herramienta en Python para detectar mejoras y errores.


---


### Parte 1: Creación de la página HTML 

#### Paso 1: Crear la estructura básica de la página 
Crea un archivo HTML llamado `index.html` con la siguiente estructura básica:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Guía completa sobre cómo aplicar SEO técnico a una página web">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.miweb.com/seo-tecnico">
    <title>SEO Técnico - Mejora la visibilidad de tu web</title>
</head>
<body>
    <header>
        <h1>Guía SEO Técnico</h1>
        <nav>
            <ul>
                <li><a href="#optimizacion-html">Optimización de HTML</a></li>
                <li><a href="#velocidad-carga">Mejorar la Velocidad de Carga</a></li>
                <li><a href="#moviles">Optimización para Móviles</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="optimizacion-html">
            <h2>Optimización de HTML</h2>
            <p>El SEO técnico se centra en el código de la página, la estructura del contenido, y cómo los motores de búsqueda la entienden.</p>
        </section>

        <section id="velocidad-carga">
            <h2>Mejorar la Velocidad de Carga</h2>
            <p>La velocidad de carga es crucial para el SEO. Optimiza imágenes, minimiza archivos CSS y JavaScript, y utiliza almacenamiento en caché.</p>
            <img src="velocidad.png" alt="Icono de velocidad de carga optimizada">
        </section>

        <section id="moviles">
            <h2>Optimización para Móviles</h2>
            <p>Los sitios deben ser responsivos y adaptarse a diferentes tamaños de pantalla para mejorar el SEO.</p>
        </section>
    </main>

    <footer>
        <p>© 2024 Guía SEO Técnico - Mejora la visibilidad de tu web</p>
    </footer>
</body>
</html>
```

#### Explicación del HTML optimizado para SEO técnico: 
 
1. **Meta etiquetas** : 
  - La etiqueta `<meta charset="UTF-8">` asegura que la página soporte todos los caracteres correctamente.
 
  - La etiqueta `<meta name="viewport">` es importante para la optimización móvil.
 
  - `<meta name="description">` proporciona una descripción clara y optimizada con palabras clave relevantes.
 
  - `<meta name="robots">` permite que los motores de búsqueda indexen y sigan los enlaces.
 
  - La etiqueta `<link rel="canonical">` se utiliza para evitar contenido duplicado y asegurar que se indexe la URL preferida.
 
2. **Encabezados** : 
  - `<h1>` se usa solo una vez para el título principal, y los demás encabezados (`<h2>`) jerarquizan el contenido.
 
3. **Enlaces internos y navegación** :
  - Los enlaces en la navegación tienen un texto descriptivo y relevante, lo que ayuda tanto a los usuarios como a los motores de búsqueda.
 
4. **Imágenes con texto alternativo** : 
  - El atributo `alt` en las imágenes es fundamental para que los motores de búsqueda comprendan el contenido visual.
 
5. **URL canónica** :
  - La URL canónica ayuda a prevenir contenido duplicado, indicando la URL preferida para indexar.


---


### Parte 2: Análisis SEO de la página HTML utilizando Python 

En esta parte, vamos a usar Python para analizar la página creada y verificar su optimización SEO.

#### Paso 1: Instalar el paquete necesario 
Instala el paquete `seo-analyzer` si no lo tienes ya instalado:

```bash
pip install seo-analyzer
```

#### Paso 2: Escribir el script Python para analizar el SEO 

Crea
