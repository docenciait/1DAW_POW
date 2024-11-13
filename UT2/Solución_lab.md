## Solución Laboratorio

---

1. **mysite.html** 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Título optimizado con palabras clave -->
    <title>My Site - Optimized for SEO | Learn, Explore, Discover</title>

    <!-- Meta Tags esenciales -->
    <meta charset="UTF-8">
    <meta name="description" content="Welcome to My Site, a hub for learning and exploration. Discover articles, tutorials, and more.">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="index, follow">

    <!-- Etiquetas Open Graph para redes sociales -->
    <meta property="og:title" content="My Site - Learn, Explore, Discover">
    <meta property="og:description" content="A hub for learning and discovery. Discover new articles and resources.">
    <meta property="og:image" content="http://127.0.0.1:8000/images/featured-image.jpg">
    <meta property="og:url" content="http://127.0.0.1:8000/mysite.html">

    <!-- Etiquetas Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="My Site - Learn, Explore, Discover">
    <meta name="twitter:description" content="Welcome to My Site, where knowledge meets discovery.">
    <meta name="twitter:image" content="http://127.0.0.1:8000/images/featured-image.jpg">
</head>
<body>
    <!-- Encabezado principal -->
    <header>
        <h1>Welcome to My Site</h1>
        <p>This is a basic HTML page optimized for SEO and user engagement.</p>
    </header>

    <!-- Sección principal de contenido con encabezados y listas -->
    <section>
        <h2>About Us</h2>
        <p>Explore articles, tutorials, and resources on a variety of topics to enhance your knowledge and skills.</p>
        
        <h3>Our Services</h3>
        <ul>
            <li>Web Development</li>
            <li>SEO Optimization</li>
            <li>Digital Marketing</li>
        </ul>
    </section>

    <!-- Optimización de Imagen -->
    <section>
        <h2>Our Vision</h2>
        <p>We aim to provide accessible knowledge and promote lifelong learning.</p>
        <img src="http://127.0.0.1:8000/images/vision.jpg" alt="Our Vision for a Better Future">
    </section>

    <!-- Enlaces Internos y Externos -->
    <footer>
        <p>Learn more on our <a href="http://127.0.0.1:8000/about.html">About Us</a> page.</p>
        <p>Visit our partner site: <a href="https://www.partnerwebsite.com" target="_blank">Partner Website</a>.</p>
    </footer>
</body>
</html>
```


---

2. **sitemap.xml** 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://127.0.0.1:8000/mysite.html</loc>
        <lastmod>2024-11-13</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8000/about.html</loc>
        <lastmod>2024-11-13</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>
```


---

3. **robots.txt** 

```plaintext
User-agent: *
Disallow: /admin
Allow: /images/
Allow: /mysite.html

Sitemap: http://127.0.0.1:8000/sitemap.xml
```


---

4. **Aquí tienes la solución reescrita siguiendo el nuevo método de auditoría usando `seoanalyze` y sirviendo el HTML desde un servidor local:

---

1. **mysite.html** 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Título optimizado con palabras clave -->
    <title>My Site - Optimized for SEO | Learn, Explore, Discover</title>

    <!-- Meta Tags esenciales -->
    <meta charset="UTF-8">
    <meta name="description" content="Welcome to My Site, a hub for learning and exploration. Discover articles, tutorials, and more.">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="index, follow">

    <!-- Etiquetas Open Graph para redes sociales -->
    <meta property="og:title" content="My Site - Learn, Explore, Discover">
    <meta property="og:description" content="A hub for learning and discovery. Discover new articles and resources.">
    <meta property="og:image" content="http://127.0.0.1:8000/images/featured-image.jpg">
    <meta property="og:url" content="http://127.0.0.1:8000/mysite.html">

    <!-- Etiquetas Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="My Site - Learn, Explore, Discover">
    <meta name="twitter:description" content="Welcome to My Site, where knowledge meets discovery.">
    <meta name="twitter:image" content="http://127.0.0.1:8000/images/featured-image.jpg">
</head>
<body>
    <!-- Encabezado principal -->
    <header>
        <h1>Welcome to My Site</h1>
        <p>This is a basic HTML page optimized for SEO and user engagement.</p>
    </header>

    <!-- Sección principal de contenido con encabezados y listas -->
    <section>
        <h2>About Us</h2>
        <p>Explore articles, tutorials, and resources on a variety of topics to enhance your knowledge and skills.</p>
        
        <h3>Our Services</h3>
        <ul>
            <li>Web Development</li>
            <li>SEO Optimization</li>
            <li>Digital Marketing</li>
        </ul>
    </section>

    <!-- Optimización de Imagen -->
    <section>
        <h2>Our Vision</h2>
        <p>We aim to provide accessible knowledge and promote lifelong learning.</p>
        <img src="http://127.0.0.1:8000/images/vision.jpg" alt="Our Vision for a Better Future">
    </section>

    <!-- Enlaces Internos y Externos -->
    <footer>
        <p>Learn more on our <a href="http://127.0.0.1:8000/about.html">About Us</a> page.</p>
        <p>Visit our partner site: <a href="https://www.partnerwebsite.com" target="_blank">Partner Website</a>.</p>
    </footer>
</body>
</html>
```


---

2. **sitemap.xml** 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://127.0.0.1:8000/mysite.html</loc>
        <lastmod>2024-11-13</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>http://127.0.0.1:8000/about.html</loc>
        <lastmod>2024-11-13</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>
```


---

3. **robots.txt** 

```plaintext
User-agent: *
Disallow: /admin
Allow: /images/
Allow: /mysite.html

Sitemap: http://127.0.0.1:8000/sitemap.xml
```


---

4. Auditoría con `seoanalyze` en el Servidor Local**  
1. **Servir el archivo HTML en un servidor local:** Desde la terminal, navega al directorio donde se encuentra `mysite.html` y ejecuta el servidor:

```bash
python -m http.server -b 127.0.0.1
```
Verás un mensaje indicando que el servidor está funcionando en `http://127.0.0.1:8000/`.
 
2. **Acceso al sitio en Firefox:** Abre Firefox e ingresa la URL: `http://127.0.0.1:8000/` para verificar la estructura y visualización.
 
3. **Ejecutar `seoanalyze` para realizar la auditoría inicial:** 

```bash
seoanalyze http://127.0.0.1:8000/
```
 
4. **Ejecutar `seoanalyze` con el archivo `sitemap.xml` para la auditoría extendida:** 

```bash
seoanalyze http://127.0.0.1:8000/ --sitemap sitemap.xml
```
 
5. **Generar un informe en formato HTML:** 

```bash
seoanalyze http://127.0.0.1:8000/ --output-format html
```
Este comando generará un archivo HTML con el reporte de la auditoría, que puedes abrir en tu navegador para revisar recomendaciones adicionales y realizar ajustes en `mysite.html`.


---


### Explicación de las Mejores Prácticas Aplicadas 
 
- **Estructura HTML5** : Cumplimos con los estándares HTML5.
 
- **Meta Tags** : Añadimos `charset`, `viewport`, y `robots` para SEO y adaptación a móviles.
 
- **Encabezados** : Empleamos una jerarquía estructurada (`h1`, `h2`, `h3`) para mejorar la legibilidad y accesibilidad.
 
- **Imágenes y Enlaces** : Incluimos imágenes optimizadas y enlaces internos y externos con texto ancla descriptivo.
 
- **Etiquetas Open Graph y Twitter Cards** : Mejora la visualización al compartir en redes sociales.
La auditoría final confirmará que se han optimizado todas las áreas clave de SEO técnico para mejorar la estructura de `mysite.html`.