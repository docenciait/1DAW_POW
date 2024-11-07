# UT2. Auditoría Técnica SEO con Lenguaje Dinámico y HTML


### Etiquetas HTML para SEO Técnico 
 
Optimizar un documento HTML para SEO técnico requiere el uso adecuado de varias etiquetas y atributos. A continuación, te describo cada una de las principales etiquetas HTML para SEO técnico y las opciones recomendadas para maximizar la optimización:

1. `<title>` 

- **Descripción** : Define el título de la página web y aparece en los resultados de búsqueda como enlace principal.
 
- **Recomendaciones** : 
  - **Texto conciso y relevante** : Entre 50-60 caracteres.
 
  - **Palabras clave principales** : Colocar las palabras clave relevantes, especialmente al inicio.

2. `<meta name="description">` 
- **Descripción** : Resumen de la página mostrado en los resultados de búsqueda.
 
- **Atributos** : 
  - `name="description"`: Define que el contenido de este meta es la descripción.
 
  - `content="texto descriptivo"`: Contenido que describe la página.
 
- **Recomendaciones** : 
  - **Longitud** : Entre 150-160 caracteres.
 
  - **Contenido claro y atractivo** : Incluir palabras clave secundarias y evitar relleno innecesario.

3. `<meta name="robots">` 
- **Descripción** : Indica a los motores de búsqueda cómo indexar la página.
 
- **Atributos** : 
  - `content="index, follow"`: Permite la indexación y el rastreo de enlaces.
 
  - **Opciones adicionales** : 
    - `noindex`: Evita que la página sea indexada.
 
    - `nofollow`: No sigue los enlaces en la página.
 
    - `noarchive`: Impide que el motor de búsqueda guarde una copia en caché.
 
    - `nosnippet`: Evita que el motor de búsqueda muestre un fragmento en los resultados.

4. `<link rel="canonical" href="URL">` 
- **Descripción** : Previene el contenido duplicado al señalar la URL canónica.
 
- **Atributos** : 
  - `rel="canonical"`: Define la página canónica.
 
  - `href="URL"`: Especifica la URL preferida.
 
- **Recomendación** : Asegurarse de que todas las páginas tengan una URL canónica para evitar duplicación.

5. `<meta charset="UTF-8">` 
- **Descripción** : Define la codificación de caracteres de la página.
 
- **Recomendación** : Usar `UTF-8` para asegurar compatibilidad con caracteres especiales y símbolos.

6. `<meta name="viewport" content="width=device-width, initial-scale=1.0">` 
- **Descripción** : Optimiza la experiencia en dispositivos móviles.
 
- **Atributos** : 
  - `content="width=device-width"`: Ajusta el ancho al dispositivo.
 
  - `initial-scale=1.0`: Define el nivel de zoom inicial.
 
- **Recomendación** : Es esencial para hacer la página responsiva y mejorar el SEO móvil.

7. `<h1>`, `<h2>`, `<h3>`, … `<h6>` 
- **Descripción** : Define la jerarquía de encabezados en la página.
 
- **Recomendaciones** : 
  - **Encabezado principal (`<h1>`)** : Único en cada página, con la palabra clave principal.
 
  - **Subencabezados**  (`<h2>`, `<h3>`, …): Usar para organizar el contenido jerárquicamente y mejorar la lectura.

8. `<img src="URL" alt="descripción" title="título">` 
- **Descripción** : Define imágenes y les da contexto para SEO.
 
- **Atributos** : 
  - `src="URL"`: Ruta de la imagen.
 
  - `alt="descripción"`: Texto alternativo que describe la imagen; esencial para accesibilidad y SEO.
 
  - `title="título"`: Texto emergente que se muestra al pasar sobre la imagen.
 
- **Recomendaciones** : 
  - **Alt descriptivo** : Incluir palabras clave de manera natural.
 
  - **Title** : Opcional, útil para contexto adicional.
9. `<a href="URL" rel="atributo" title="texto">` 

- **Descripción** : Define enlaces y su contexto.
 
- **Atributos** : 
  - `href="URL"`: Ruta de destino.
 
  - `rel="atributo"`: Controla cómo los motores de búsqueda rastrean el enlace. 
    - **Opciones** : `nofollow`, `noopener`, `noreferrer`, `sponsored`, `ugc`.
 
  - `title="texto"`: Texto emergente que aparece al pasar sobre el enlace.
 
- **Recomendaciones** : 
  - **Texto ancla relevante** : Añadir palabras clave en el texto del enlace.
 
  - **Atributo `rel`** : Usar `nofollow` para enlaces no de confianza.

10. `<strong>` y `<em>` 
- **Descripción** : Aumenta la importancia de ciertas palabras.
 
- **Uso SEO** : Resalta palabras clave específicas para que los motores de búsqueda las consideren más relevantes.

11. `<meta name="keywords" content="palabras, clave">` 
- **Descripción** : Permite listar palabras clave de la página (poco usado).
 
- **Recomendación** : Aunque su impacto en SEO ha disminuido, algunas herramientas internas pueden aprovecharlo.

12. `<meta property="og:*">` (Open Graph) 
- **Descripción** : Mejora la apariencia de la página en redes sociales.
 
- **Atributos** : 
  - `og:title`: Título de la página.
 
  - `og:description`: Descripción para compartir en redes.
 
  - `og:image`: URL de la imagen representativa.
 
  - `og:url`: URL canónica de la página.
 
  - **Otros** : `og:type`, `og:site_name`, `og:locale`.
 
- **Recomendación** : Implementar para asegurar que la página se comparte correctamente en redes sociales.

13. `<meta name="twitter:*">` 
- **Descripción** : Similar a Open Graph, optimiza la presentación en Twitter.
 
- **Atributos** : 
  - `twitter:card`: Tipo de tarjeta (ej. `summary`, `summary_large_image`).
 
  - `twitter:title`, `twitter:description`, `twitter:image`: Información específica para Twitter.
 
- **Recomendación** : Asegurar que la página se comparte bien en Twitter.

14. `<meta http-equiv="Content-Security-Policy" content="policy">` 
- **Descripción** : Controla cómo se cargan los recursos en la página.
 
- **Uso SEO** : Mejora la seguridad y protege de ataques como el XSS, lo cual es positivo para la experiencia del usuario y SEO técnico.

15. `<html lang="es">` 
- **Descripción** : Define el idioma principal de la página.
 
- **Recomendación** : Usar correctamente para mejorar la accesibilidad y SEO en búsquedas locales.

16. `<script type="application/ld+json">` (JSON-LD para datos estructurados) 
- **Descripción** : Añade datos estructurados para mejorar el entendimiento del contenido.
 
- **Recomendación** : Usar datos estructurados para marcar elementos específicos, como artículos, productos, eventos, personas, etc.

17. `<meta name="author" content="nombre del autor">` 
- **Descripción** : Define el autor del contenido.
 
- **Uso SEO** : Aunque es menos común, puede ayudar en la identificación de contenido original en ciertos contextos.

18. `<footer>`, `<header>`, `<nav>`, `<aside>`, `<section>`, `<article>`, `<main>` 
- **Descripción** : Mejoran la semántica de la página, estructurando correctamente el contenido.
 
- **Recomendación** : Usar estas etiquetas semánticas para mejorar la comprensión del contenido y accesibilidad, lo cual indirectamente beneficia al SEO.

19. `<base href="URL">` 
- **Descripción** : Establece una URL base para todos los enlaces relativos en el documento.
 
- **Uso SEO** : Facilita la administración de enlaces internos, especialmente en sitios grandes con muchas URLs relativas.

20. `<meta name="theme-color" content="#000000">` 
- **Descripción** : Cambia el color de la barra de navegador en dispositivos móviles.
 
- **Uso SEO** : Mejora la apariencia de la página en dispositivos móviles, aunque su impacto en SEO directo es mínimo.

21. `<meta name="referrer" content="no-referrer">` 
- **Descripción** : Controla el comportamiento de referencia de enlaces salientes.
 
- **Opciones** : 
  - `no-referrer`: No envía información de referencia.
 
  - `origin`: Solo envía la URL base.
 
  - `unsafe-url`: Envía toda la URL.
 
- **Uso SEO** : Aunque su impacto en SEO es indirecto, puede mejorar la privacidad y control del tráfico referencial.

22. `<meta http-equiv="refresh" content="time; URL">` 
- **Descripción** : Redirige automáticamente a otra página después de un cierto tiempo.
 
- **Uso SEO** : Las redirecciones automáticas se deben usar con cuidado; si es necesario redirigir, es mejor hacerlo en el servidor (redirección 301 o 302).

23. `<link rel="alternate" hreflang="es" href="URL">` 

- **Descripción** : Indica versiones alternas del contenido en diferentes idiomas y regiones.
 
- **Atributos** : 
  - `hreflang="código de idioma"`: Define el idioma y la región (ej. `es`, `es-ES`, `en-US`).
 
  - `href="URL"`: La URL de la versión alterna.
 
- **Uso SEO** : Importante para SEO multilingüe, permite a los motores de búsqueda identificar las versiones regionales y lingüísticas de la página.

24. `<meta http-equiv="x-ua-compatible" content="IE=edge">` 

- **Descripción** : Obliga a los navegadores antiguos de Internet Explorer a renderizar con el último motor.
 
- **Uso SEO** : No afecta directamente el SEO, pero ayuda a mejorar la compatibilidad y experiencia en navegadores obsoletos.

25. `<noscript>` 

- **Descripción** : Proporciona contenido alternativo si el navegador tiene JavaScript deshabilitado.
 
- **Uso SEO** : Útil en páginas que dependen mucho de JavaScript, ya que garantiza que el contenido principal sigue siendo accesible para los rastreadores.

26. `<meta property="article:*">` 

- **Descripción** : Parte de Open Graph, específica para contenido de tipo artículo.
 
- **Atributos** : 
  - `article:author`: URL del perfil del autor.
 
  - `article:published_time`: Fecha de publicación.
 
  - `article:modified_time`: Fecha de modificación.
 
  - `article:section`: Sección o categoría del artículo.
 
  - `article:tag`: Etiquetas del artículo.
 
- **Uso SEO** : Mejora la presentación en redes sociales y ayuda a categorizar artículos en plataformas que lo soportan.

27. `<figure>` y `<figcaption>` 

- **Descripción** : Agrupa contenido visual como imágenes y proporciona subtítulos descriptivos.
 
- **Uso SEO** : Permite describir mejor los contenidos visuales y optimiza la accesibilidad.

28. `<data>` y `<time>` 

- **Descripción** : Etiquetas que representan datos específicos (como fechas y tiempos).
 
- **Uso SEO** : Estandariza la representación de datos en la página, útil para ciertos tipos de resultados enriquecidos.

29. `<address>` 

- **Descripción** : Define información de contacto (como dirección y datos de la empresa).
 
- **Uso SEO** : Proporciona información estructurada para motores de búsqueda y ayuda en SEO local.

30. `<input type="search" />` y `<label>` 

- **Descripción** : Elementos para formularios de búsqueda y etiquetado.
 
- **Uso SEO** : Permite a los motores de búsqueda identificar funciones de búsqueda internas en un sitio web, lo cual puede mejorar la indexación y la experiencia de usuario.

> Cada etiqueta y atributo bien configurado contribuye a una optimización SEO técnica sólida y ayuda a los motores de búsqueda a comprender el contenido y estructura de la página, mejorando la relevancia y visibilidad en los resultados de búsqueda.

> Las etiquetas anteriores cubren la mayoría de las prácticas de SEO técnico. Sin embargo, existen algunas etiquetas y atributos adicionales menos comunes o específicos que pueden ser útiles para ciertos tipos de contenido y mejoras adicionales en SEO técnico.

> Estas etiquetas y atributos adicionales complementan las prácticas de SEO técnico, sobre todo cuando se trata de mejorar la accesibilidad, la experiencia del usuario y la compatibilidad en sitios multilingües o con elementos multimedia complejos. Implementarlos depende del tipo de contenido y de las necesidades específicas de la página web.

---




```bash
pip install seo-analyzer
```
Uso básico de `seo-analyzer`El `seo-analyzer` puede analizar tanto sitios web completos como archivos HTML individuales para identificar problemas de SEO técnico, como la falta de etiquetas importantes, el rendimiento, y los enlaces rotos.

### Práctica: Optimización SEO Técnica de una Página HTML 

#### Objetivo 

El objetivo de esta práctica es que los estudiantes aprendan a aplicar las mejores prácticas de SEO técnico utilizando etiquetas HTML apropiadas y, posteriormente, analizar la página utilizando una herramienta en Python para detectar mejoras y errores.


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
 
### Análisis de la página HTML 
 
1. **Declaración básica del documento**  
  - ✔️ **Correcto** : La declaración `<!DOCTYPE html>` está presente y es correcta.
 
2. **Idioma de la página**  
  - ✔️ **Correcto** : La declaración `lang="es"` especifica el idioma español.
 
3. **Meta etiquetas principales**  
  - **Meta charset**  (`UTF-8`): ✔️ Correcto.
 
  - **Meta viewport**  (`width=device-width, initial-scale=1.0`): ✔️ Correcto para mejorar la experiencia en dispositivos móviles.
 
  - **Meta description** : ✔️ Correcta, con una descripción relevante.
 
  - **Meta robots**  (`index, follow`): ✔️ Correcto, permite la indexación y el seguimiento de enlaces.
 
  - **Canonical** : ✔️ Correcto, la URL canónica está configurada.
 
4. **Etiqueta `<title>`**  
  - ✔️ **Correcto** : La etiqueta `title` es relevante y contiene palabras clave.
 
5. **Encabezados estructurados**  
  - **H1** : ✔️ `Guía SEO Técnico` está presente y es adecuado.
 
  - **Subencabezados (H2)** : ✔️ Correctos, describen bien cada sección.
 
6. **Enlaces de navegación**  
  - ✔️ **Correcto** : Los enlaces internos funcionan bien y llevan a las secciones dentro de la misma página.
 
7. **Imágenes**  
  - ✔️ **Correcto** : La imagen tiene un atributo `alt`, que es una buena práctica para la accesibilidad y SEO.
 
8. **Contenido estructurado**  
  - ❌ **Faltante** : Datos estructurados en JSON-LD o Schema.org para ayudar a los motores de búsqueda a entender mejor la estructura de la página.
 
9. **Metadatos para redes sociales**  
  - ❌ **Faltante** : Open Graph y Twitter Cards para una mejor presentación en redes sociales.

### Recomendaciones para mejorar la optimización SEO técnico 

Para optimizar aún más esta página HTML, considera agregar lo siguiente:
 
1. **Datos estructurados (JSON-LD)** : Puedes añadir un script JSON-LD para especificar que es una guía o un artículo. Esto mejora cómo se muestra el contenido en los resultados de búsqueda.
 
2. **Metadatos para redes sociales (Open Graph y Twitter Cards)** : Agregar etiquetas Open Graph (`og:*`) y Twitter Cards para mejorar la presentación al compartir el enlace en redes sociales.
 
3. **Atributo `lang` en `<html>`** 
  - Ya está presente y correcto para definir el idioma del documento.
 
4. **Sitemap y Robots.txt** : Asegúrate de tener un `robots.txt` y un `sitemap.xml` bien configurados en tu servidor para guiar a los bots.

### Ejemplo de optimización adicional para la página 


```html
<!-- Datos estructurados JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Guía SEO Técnico",
  "description": "Guía completa sobre cómo aplicar SEO técnico a una página web",
  "url": "https://www.miweb.com/seo-tecnico",
  "inLanguage": "es"
}
</script>

<!-- Open Graph Metadata -->
<meta property="og:type" content="website">
<meta property="og:title" content="SEO Técnico - Mejora la visibilidad de tu web">
<meta property="og:description" content="Guía completa sobre cómo aplicar SEO técnico a una página web">
<meta property="og:image" content="https://www.miweb.com/img/seo.jpg">
<meta property="og:url" content="https://www.miweb.com/seo-tecnico">

<!-- Twitter Cards Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="SEO Técnico - Mejora la visibilidad de tu web">
<meta name="twitter:description" content="Guía completa sobre cómo aplicar SEO técnico a una página web">
<meta name="twitter:image" content="https://www.miweb.com/img/seo.jpg">
```

---


# Ficheros `robots.txt` y `sitemap.xml`:

En la optimización SEO, los archivos `robots.txt` y `sitemap.xml` son dos elementos esenciales que ayudan a los motores de búsqueda a rastrear y comprender mejor el contenido de un sitio web. Vamos a detallar cada uno de ellos:1. Archivo `robots.txt`El archivo `robots.txt` es un archivo de texto plano que se coloca en la raíz del dominio de un sitio web (por ejemplo, `https://tu-dominio.com/robots.txt`). Su principal función es proporcionar instrucciones a los robots de los motores de búsqueda sobre qué páginas o secciones del sitio web deben rastrear y cuáles no. Esto permite tener control sobre el contenido que se desea indexar y el que no es relevante para el SEO.Sintaxis del archivo `robots.txt`El `robots.txt` está compuesto por reglas que los robots interpretan en una estructura sencilla. Los elementos clave son: 
- **User-agent** : Especifica a qué bot de rastreo va dirigida la regla (por ejemplo, Googlebot para Google, Bingbot para Bing). Se pueden establecer reglas para todos los robots con `User-agent: *`.
 
- **Disallow** : Define las páginas o directorios que no se deben rastrear.
 
- **Allow** : Permite el rastreo de un archivo específico dentro de un directorio restringido por `Disallow`.
 
- **Sitemap** : Indica la ubicación del archivo `sitemap.xml`.
Ejemplo de archivo `robots.txt`

```plaintext
User-agent: *
Disallow: /admin/        # Prohíbe el acceso a la carpeta de administración
Disallow: /login/        # Prohíbe el acceso a la página de inicio de sesión
Allow: /public/allowed-file.html  # Permite el rastreo de un archivo específico
Sitemap: https://tu-dominio.com/sitemap.xml  # Ubicación del archivo sitemap.xml
```
Consideraciones SEO para `robots.txt` 
- **Evitar el rastreo de contenido irrelevante** : Es útil para bloquear secciones del sitio que no aportan valor en los resultados de búsqueda (e.g., `/admin/`).
 
- **Optimizar el crawl budget** : En sitios grandes, el `robots.txt` ayuda a ahorrar el presupuesto de rastreo de los robots, concentrándolos en las páginas relevantes.
 
- **Bloquear recursos no deseados** : Si se detectan errores por parte de los bots (como rastrear recursos pesados sin importancia, como archivos `.js` o `.css` específicos), se pueden bloquear para mejorar la eficiencia.
Herramientas para probar `robots.txt`Es recomendable probar el archivo `robots.txt` usando herramientas como **Google Search Console** , que permite verificar si el archivo cumple con las directrices y si los robots pueden acceder a las secciones relevantes.

---

2. Archivo `sitemap.xml`El archivo `sitemap.xml` es un archivo en formato XML que lista todas las páginas importantes de un sitio web que se desean rastrear y, eventualmente, indexar. Este archivo es una especie de “mapa” para los motores de búsqueda, ayudándoles a comprender la estructura del sitio y encontrar nuevas páginas de manera rápida.Estructura del archivo `sitemap.xml`El archivo `sitemap.xml` tiene una estructura jerárquica, donde cada URL que se quiera indexar se coloca en una entrada `<url>`. Los elementos importantes en un `sitemap.xml` son: 
- **loc** : Contiene la URL de la página.
 
- **lastmod** : Indica la última fecha de modificación de la página, lo que permite a los motores saber si ha habido actualizaciones.
 
- **changefreq** : Sugerencia sobre la frecuencia con la que la página cambia (por ejemplo, `daily`, `weekly`, `monthly`).
 
- **priority** : Indica la prioridad de la URL dentro del sitio (rango de 0.0 a 1.0).
Ejemplo de archivo `sitemap.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://tu-dominio.com/</loc>
      <lastmod>2024-10-30</lastmod>
      <changefreq>daily</changefreq>
      <priority>1.0</priority>
   </url>
   <url>
      <loc>https://tu-dominio.com/blog</loc>
      <lastmod>2024-10-29</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
   <url>
      <loc>https://tu-dominio.com/contacto</loc>
      <lastmod>2024-10-15</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.5</priority>
   </url>
</urlset>
```
Consideraciones SEO para `sitemap.xml` 

- **Mejor indexación** : Los sitemaps aseguran que todas las URLs relevantes estén disponibles para los motores de búsqueda, especialmente aquellas que están más profundas en la estructura del sitio.
 
- **Actualización de contenido** : Con `lastmod`, los motores de búsqueda son alertados sobre qué páginas han cambiado, lo cual es fundamental para sitios de noticias o blogs.
 
- **Control de prioridad** : Aunque no garantiza una posición en el ranking, ayuda a los motores a entender qué páginas son prioritarias en el sitio.
Herramientas para verificar `sitemap.xml`Google Search Console y Bing Webmaster Tools permiten subir el `sitemap.xml` y verificar su correcto funcionamiento. Además, se pueden detectar errores o páginas que no están siendo indexadas.

---

Relación entre `robots.txt` y `sitemap.xml`Ambos archivos se complementan. Mientras el `robots.txt` limita el acceso a ciertas áreas del sitio, el `sitemap.xml` indica qué contenido debe ser rastreado. Una configuración adecuada ayuda a los motores de búsqueda a indexar el contenido relevante de manera eficiente y a no desperdiciar recursos en contenido innecesario.


---

## Ejemplo completo

Ejemplo completo de una página index.html optimizada para SEO técnico, junto con un ejemplo de robots.txt y sitemap.xml.

**`robots.txt`**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <!-- Meta Datos Básicos -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Optimización SEO en Ejemplo Completo</title>
    <meta name="description" content="Guía completa de optimización SEO técnico en HTML. Aprende a usar etiquetas clave para mejorar tu SEO.">
    <meta name="robots" content="index, follow">
    <meta name="keywords" content="SEO técnico, etiquetas HTML, optimización SEO, HTML5">
    <meta name="author" content="Tu Nombre">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://www.tusitio.com/">
    
    <!-- Open Graph Metadata -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Optimización SEO en Ejemplo Completo">
    <meta property="og:description" content="Guía completa de optimización SEO técnico en HTML.">
    <meta property="og:image" content="https://www.tusitio.com/img/seo.jpg">
    <meta property="og:url" content="https://www.tusitio.com/">
    
    <!-- Twitter Cards Metadata -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Optimización SEO en Ejemplo Completo">
    <meta name="twitter:description" content="Guía completa de optimización SEO técnico en HTML.">
    <meta name="twitter:image" content="https://www.tusitio.com/img/seo.jpg">
    
    <!-- Estilos -->
    <link rel="stylesheet" href="css/styles.css">
    
    <!-- Datos Estructurados con JSON-LD -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Optimización SEO en Ejemplo Completo",
        "url": "https://www.tusitio.com/",
        "image": "https://www.tusitio.com/img/seo.jpg",
        "description": "Guía completa de optimización SEO técnico en HTML. Aprende a usar etiquetas clave para mejorar tu SEO."
    }
    </script>
</head>
<body>

    <!-- Encabezado Principal -->
    <header>
        <h1>Guía Completa de Optimización SEO en HTML</h1>
    </header>

    <!-- Navegación -->
    <nav>
        <ul>
            <li><a href="#seccion1" title="Ir a la Sección 1">Sección 1</a></li>
            <li><a href="#seccion2" title="Ir a la Sección 2">Sección 2</a></li>
            <li><a href="#seccion3" title="Ir a la Sección 3">Sección 3</a></li>
        </ul>
    </nav>

    <!-- Contenido Principal -->
    <main>
        <section id="seccion1">
            <h2>Sección 1: Importancia de las Etiquetas HTML en SEO</h2>
            <p>Las etiquetas HTML ayudan a mejorar la estructura y el rendimiento SEO de una página web.</p>
        </section>

        <section id="seccion2">
            <h2>Sección 2: Open Graph y Twitter Cards</h2>
            <figure>
                <img src="https://www.tusitio.com/img/seo.jpg" alt="Optimización SEO" title="Imagen de Optimización SEO">
                <figcaption>Ejemplo de imagen optimizada para SEO.</figcaption>
            </figure>
        </section>

        <section id="seccion3">
            <h2>Sección 3: Robots y Sitemap</h2>
            <p>Con un archivo `robots.txt` y `sitemap.xml`, se puede controlar el rastreo e indexación del sitio.</p>
        </section>
    </main>

    <!-- Pie de Página -->
    <footer>
        <address>
            Contacto: <a href="mailto:contacto@tusitio.com">contacto@tusitio.com</a>
        </address>
    </footer>

    <!-- Script Externo -->
    <script src="js/scripts.js"></script>

</body>
</html>

```

*`robots.txt`*:
El archivo robots.txt estará ubicado en la raíz del sitio (https://www.tusitio.com/robots.txt) y contendrá instrucciones para los bots de los motores de búsqueda.

```bash
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/
Crawl-delay: 5

# Excluir específicamente a Googlebot de una sección
User-agent: Googlebot
Disallow: /no-google/

# Enlace al sitemap
Sitemap: https://www.tusitio.com/sitemap.xml

```

*`sitemap.xml`*:

El archivo sitemap.xml también estará en la raíz del sitio (https://www.tusitio.com/sitemap.xml) y tendrá la lista de URLs que deseas que los motores de búsqueda rastreen e indexen.

```bash
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://www.tusitio.com/</loc>
      <lastmod>2024-10-30</lastmod>
      <changefreq>daily</changefreq>
      <priority>1.0</priority>
   </url>
   <url>
      <loc>https://www.tusitio.com/seccion1</loc>
      <lastmod>2024-10-29</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
   <url>
      <loc>https://www.tusitio.com/seccion2</loc>
      <lastmod>2024-10-29</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.7</priority>
   </url>
   <url>
      <loc>https://www.tusitio.com/seccion3</loc>
      <lastmod>2024-10-29</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.6</priority>
   </url>
</urlset>

```

Explicación de cada componente:

- index.html: Utiliza todas las etiquetas recomendadas para SEO técnico, incluyendo title, meta description, etiquetas de Open Graph y Twitter Cards, así como un script JSON-LD para datos estructurados.

- robots.txt: Controla el acceso de los rastreadores a diferentes partes del sitio y señala la ubicación del sitemap.xml.

- sitemap.xml: Enumera las URLs importantes de la página, con información sobre la frecuencia de actualización y prioridad, ayudando a los motores de búsqueda a entender la estructura y relevancia de cada página.

Este conjunto proporciona una base optimizada para SEO técnico que debería ser eficaz en la mayoría de los escenarios.

ejemplo básico de cómo implementar un bloque de datos estructurados en formato `JSON-LD`, que ayuda a los motores de búsqueda a comprender mejor el contenido de tu página web. Este ejemplo es para un tipo de contenido común, como un negocio local.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Nombre del Negocio",
  "image": "https://ejemplo.com/logo.jpg",
  "url": "https://ejemplo.com",
  "telephone": "+34 123 456 789",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Ejemplo, 123",
    "addressLocality": "Ciudad",
    "addressRegion": "Provincia",
    "postalCode": "28001",
    "addressCountry": "ES"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "opens": "09:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "14:00"
    }
  ],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.416775,
    "longitude": -3.703790
  },
  "sameAs": [
    "https://www.facebook.com/negocio",
    "https://www.instagram.com/negocio",
    "https://twitter.com/negocio"
  ]
}
</script>
```

### Explicación de cada elemento: 
 
- **@context** : Define el contexto de Schema.org.
 
- **@type** : Especifica el tipo de entidad (aquí, un `LocalBusiness`).
 
- **name** : Nombre del negocio.
 
- **image** : URL de una imagen representativa (generalmente el logotipo).
 
- **url** : URL del sitio web del negocio.
 
- **telephone** : Número de teléfono de contacto.
 
- **address** : Información de dirección del negocio.
 
- **openingHoursSpecification** : Horario de apertura y cierre del negocio.
 
- **geo** : Coordenadas geográficas (latitud y longitud) de la ubicación.
 
- **sameAs** : URLs de las redes sociales del negocio (opcional).

Este formato permite que motores de búsqueda como Google comprendan mejor la estructura de la página, lo que puede mejorar su visibilidad y presentación en los resultados de búsqueda.
