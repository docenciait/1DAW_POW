# LAB1: Utilizando esta página ejemplo

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

## Realizar la auditoría con pyseoanalyzer:

### Instalar pyseonalyzer

```bash
pip3 install pyseoanalyzer
```
### configurar ~/.bashrc

```bash

export PATH=$PATH:~/.local/bin

# Luego salir y realizar 
source ~/.bashrc
```

### Ejecutar el servidor
Dentro de tu directorio donde está el index.html
```bash
python -m http.server -b 127.0.0.1
Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...
```

Accedes a una url de Firefox con http://127.0.0.1:8000/

```bash
seoanalyze http://127.0.0.1:8000/


seoanalyze http://127.0.0.1:8000/ --sitemap path/to/sitemap.xml


seoanalyze http://127.0.0.1:8000/ --output-format html
```

--- 
### LAB2: Requisitos del Laboratorio 

1. Optimización de Etiquetas en `mysite.html`
Se parte de una página HTML simple que contiene:


```html
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Welcome to My Site</h1>
    <p>This is a basic HTML page.</p>
</body>
</html>
```
**Objetivos de Optimización:**  
- **Estructura HTML5** : Asegurarse de que el documento HTML cumpla con la estructura básica de HTML5.
 
- **Etiqueta `<title>`** : Mejorar la etiqueta `<title>` para que sea informativa y contenga las palabras clave principales.
 
- **Meta Tags** : 
  - Añadir `<meta charset="UTF-8">`.
 
  - Incluir `<meta name="description" content="Descripción optimizada con palabras clave">`.
 
  - Incluir `<meta name="viewport" content="width=device-width, initial-scale=1">` para optimización móvil.
 
  - Añadir `<meta name="robots" content="index, follow">`.
 
- **Encabezados y Jerarquía** :
  - Asegurarse de que se utilizan encabezados estructurados (h1, h2, h3) para organizar el contenido y mejorar la legibilidad.

  - Incluir encabezados secundarios para secciones de contenido importante.
 
- **Optimización de Imágenes** : 
  - Añadir al menos una imagen con una etiqueta `<img>`, especificando el atributo `alt` con palabras clave relevantes.

  - Optimizar el tamaño de la imagen para mejorar la velocidad de carga.
 
- **Enlaces Internos y Externos** :
  - Incluir al menos un enlace interno y un enlace externo relevante, usando texto ancla descriptivo.
 
- **Estructura de Contenido** : 
  - Añadir contenido adicional en formato de párrafos `<p>`, listas ordenadas `<ol>` o no ordenadas `<ul>`, y añadir al menos un enlace con texto enriquecido.
 

- **Etiquetas Open Graph y Twitter Cards** : 
  - Añadir etiquetas Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) para mejorar la visualización de enlaces en redes sociales.

  - Incluir meta etiquetas para Twitter Cards, asegurando que la página sea amigable para compartir en Twitter.

2. Creación de `sitemap.xml`Cree un archivo `sitemap.xml` que cumpla con las siguientes condiciones: 
- Debe incluir una lista de todas las páginas de `mysite.html`, especificando la URL completa de cada una.
 
- Añadir las siguientes etiquetas: 
  - `<lastmod>`: La última fecha de modificación para cada página.
 
  - `<changefreq>`: Indicar `monthly` para la frecuencia de actualización de cada página.
 
  - `<priority>`: Asignar una prioridad de `0.8` para la página principal y `0.5` para cualquier otra página secundaria.

3. Configuración de `robots.txt`Cree un archivo `robots.txt` con las siguientes condiciones: 

- Permitir que todos los motores de búsqueda indexen la página principal (`mysite.html`).
 
- Bloquear el acceso al directorio `/admin` para todos los bots.
 
- Permitir el acceso a todos los archivos de imágenes en el directorio `/images`.
 
- Añadir una referencia al `sitemap.xml` en el archivo `robots.txt`, utilizando la estructura:

```txt
Sitemap: http://www.yoursite.com/sitemap.xml
```

---


### Entregables 
 
1. **Archivo HTML optimizado**  (`mysite.html`) que cumpla con todas las optimizaciones de SEO técnico descritas.
 
2. **Archivo `sitemap.xml`**  que siga las especificaciones mencionadas.
 
3. **Archivo `robots.txt`**  con las configuraciones descritas.


### Auditoría
 
- Utilice `pySEOAnalyzer` o herramientas de Python adicionales para realizar auditorías sobre el código HTML y mejorar la estructura SEO.