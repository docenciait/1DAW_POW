| Información General            | Detalles de la Prueba                    | Otros Detalles                     |
| :----------------------------- | :--------------------------------------- | :--------------------------------- |
| **Examen:** Final (Módulo SEO) | **Formato:** Test 40 preg. (4 alt, 1 corr.) | **Puntos:** Correcta:+0.25, Incorrecta:-1/12 (-0.0833), Nula/NC: 0 |
| **Fecha:** 15 Mayo 2025 - 8:15H| **Curso:** 1º DAW        | **Calificación:** 0-10             |
| **Duración:** 1H                 | **Lugar:** Salón Actos, Ed. Albéniz      | **RA:** RA5                        |
| **ALUMNO/A:**                 |   |  **CALIF:.**                      |


---

**1. Después de ejecutar `resultado = requests.get(url)`, ¿cómo obtienes el código de estado HTTP de la respuesta?**

   - a) `resultado.status`
   - b) `resultado.code`
   - c) `resultado.status_code`
   - d) `resultado.get_status()`

**2. Para parsear el contenido HTML (`html_content`) con BeautifulSoup usando el parser 'html.parser', ¿cuál es la sintaxis correcta?**

   - a) `BeautifulSoup(html_content, using='html.parser')`
   - b) `BeautifulSoup(html_content, 'html.parser')`
   - c) `BeautifulSoup.parse(html_content, 'html.parser')`
   - d) `BeautifulSoup.read(html_content, 'html.parser')`

**3. Si deseas obtener el contenido textual de la etiqueta `<title>` y estás seguro de que existe, pero quieres evitar `AttributeError` si estuviera vacía (ej. `<title></title>`), ¿cuál es una forma robusta de obtener su contenido o una cadena vacía?**

   - a) `soup.title.text if soup.title else ""`
   - b) `soup.title.string or ""`
   - c) `str(soup.title)`
   - d) `soup.find('title').get_text(strip=True)`

**4. ¿Cuál es el propósito principal de un `robots.txt` en relación con el SEO?**

   - a) Mejorar la velocidad de carga del sitio.
   - b) Guiar a los rastreadores de los motores de búsqueda sobre qué partes del sitio pueden o no rastrear.
   - c) Definir la estructura de los enlaces internos.
   - d) Especificar los metadatos para compartir en redes sociales.

**5. ¿Qué atributo de la etiqueta `<a>` es crucial para identificar un enlace interno o externo?**

   - a) `class`
   - b) `id`
   - c) `href`
   - d) `target`

**6. En BeautifulSoup, si `meta_desc = soup.find("meta", attrs={"name": "description"})`, ¿cómo accedes al contenido real de la descripción?**

   - a) `meta_desc.text`
   - b) `meta_desc.value`
   - c) `meta_desc.get("content")`
   - d) `meta_desc.string`

**7. ¿Cuál de las siguientes afirmaciones sobre las etiquetas `<h1>` a `<h6>` es más precisa desde una perspectiva SEO semántica?**

   - a) Solo se debe usar una etiqueta `<h1>` por página; el resto son opcionales.
   - b) Deben seguir una jerarquía lógica (ej. `<h2>` dentro de secciones de `<h1>`, `<h3>` dentro de `<h2>`).
   - c) El número de etiquetas `<h2>` no debe exceder el de `<h3>`.
   - d) Es preferible usar CSS para dar estilo al texto en lugar de estas etiquetas para SEO.

**8. Al analizar enlaces rotos, un código de estado HTTP `404` significa:**

   - a) El servidor ha encontrado el recurso solicitado.
   - b) El recurso solicitado se ha movido permanentemente.
   - c) El servidor no pudo encontrar el recurso solicitado.
   - d) El acceso al recurso está prohibido.

**9. Si necesitas encontrar todas las imágenes (`<img>`) que SÍ tienen un atributo `alt` definido y no vacío, ¿cómo lo harías con BeautifulSoup (asume `imagenes = soup.find_all('img')`)?**

   - a) `[img for img in imagenes if img.get('alt')]`
   - b) `[img for img in imagenes if img['alt'] is not None]`
   - c) `[img for img in imagenes if img.has_attr('alt') and img['alt'] != '']`
   - d) Todas las opciones a, b y c son funcionalmente equivalentes para este propósito si `alt` existe.

**10. ¿Qué indica la presencia de una etiqueta `<link rel="canonical" href="URL_alternativa">` en una página?**

    - a) Que la página actual es un duplicado y la URL_alternativa es la original o preferida.
    - b) Que la página se debe redirigir a URL_alternativa.
    - c) Que URL_alternativa es una versión en otro idioma de la página actual.
    - d) Que URL_alternativa es el sitemap de la página.

**11. Para extraer URLs de un `sitemap.xml` parseado con BeautifulSoup (`soup_sitemap`), donde las URLs están dentro de etiquetas `<loc>`, ¿cómo lo harías?**

    - a) `[url.text for url in soup_sitemap.find_all('loc')]`
    - b) `[url.get('href') for url in soup_sitemap.find_all('url')]`
    - c) `soup_sitemap.select('loc > text')`
    - d) `soup_sitemap.find('url').loc.string`

**12. El "Time to First Byte" (TTFB) mide:**

    - a) El tiempo total que tarda la página en ser interactiva.
    - b) El tiempo desde la solicitud del navegador hasta que recibe el primer byte de respuesta del servidor.
    - c) El tiempo que tarda el DNS en resolverse.
    - d) El tiempo que tarda en descargarse el HTML principal sin recursos.

**13. ¿Cuál de estas metaetiquetas es fundamental para Open Graph (usado por Facebook)?**

    - a) `<meta name="og:title" content="...">`
    - b) `<meta property="og:type" content="...">`
    - c) `<meta itemprop="image" content="...">`
    - d) `<meta name="twitter:card" content="...">`

**14. ¿Cómo se puede verificar si se utiliza HTTPS en un enlace interno `href_value` de forma programática en Python?**

    - a) `if "https" in href_value:`
    - b) `if href_value.startswith("https://") or href_value.startswith("/") :` (asumiendo que los relativos heredan el protocolo)
    - c) `if urlparse(href_value).scheme == "https"` (necesitaría `urljoin` para relativos primero)
    - d) Todas las anteriores pueden ser parte de una solución, pero c es la más precisa para URLs absolutas.

**15. ¿Cuál es el principal problema SEO de tener contenido duplicado extenso entre diferentes URLs de tu propio sitio?**

    - a) Aumenta el tamaño de la base de datos del sitio.
    - b) Puede confundir a los motores de búsqueda sobre qué URL clasificar para consultas relevantes.
    - c) Consume más cuota de rastreo.
    - d) b y c.

**16. Una alta densidad de una palabra clave específica (ej. > 5-7%) en una página es a menudo un indicador de:**

    - a) Contenido de alta calidad y relevante.
    - b) Una buena estrategia de long-tail keywords.
    - c) Posible "keyword stuffing" o sobreoptimización.
    - d) Que la página rankeará bien para esa palabra clave.

**17. ¿Qué formato es comúnmente utilizado para implementar Schema.org y se incluye dentro de una etiqueta `<script type="application/ld+json">`?**

    - a) Microdatos
    - b) RDFa Lite
    - c) JSON-LD
    - d) XML Schema

**18. Si `response` es el objeto devuelto por `requests.get()`, ¿qué información NO se encuentra directamente en `response.headers`?**

    - a) `Content-Type`
    - b) `Server`
    - c) El texto HTML de la página.
    - d) `Set-Cookie`

**19. Al analizar la estructura de encabezados, si encuentras una página sin `<h1>` pero con varios `<h2>`, ¿cuál es la principal implicación SEO?**

    - a) La página cargará más rápido.
    - b) Los motores de búsqueda podrían tener dificultades para identificar el tema principal de la página.
    - c) Es una práctica moderna recomendada para la legibilidad.
    - d) Mejora la accesibilidad para lectores de pantalla.

**20. Para extraer todos los atributos de una etiqueta encontrada con BeautifulSoup (ej. `tag = soup.find('div')`), ¿cómo lo harías?**

    - a) `tag.get_attributes()`
    - b) `tag.attrs`
    - c) `tag.attributes()`
    - d) `tag.list_attrs()`

**21. En `requests`, ¿para qué se usa el parámetro `timeout` en una llamada como `requests.get(url, timeout=5)`?**

    - a) Para esperar 5 segundos antes de enviar la petición.
    - b) Para establecer la duración máxima de la conexión y la lectura de la respuesta en 5 segundos.
    - c) Para que la petición se reintente cada 5 segundos si falla.
    - d) Para limitar la velocidad de descarga a 5MB/s.

**22. ¿Cuál es una forma de encontrar todas las etiquetas `script` que tienen el atributo `src` usando BeautifulSoup?**

    - a) `soup.find_all('script', src=True)`
    - b) `soup.find_all(lambda tag: tag.name == 'script' and tag.has_attr('src'))`
    - c) `[s for s in soup.find_all('script') if s.get('src')]`
    - d) Todas las anteriores son formas válidas o casi equivalentes.

**23. ¿Cuál es la diferencia principal entre `soup.find()` y `soup.find_all()` en BeautifulSoup?**

    - a) `find()` busca por clase CSS, `find_all()` por ID.
    - b) `find()` devuelve solo el primer elemento coincidente, `find_all()` devuelve una lista de todos los elementos coincidentes.
    - c) `find()` solo busca en el `head`, `find_all()` en todo el documento.
    - d) `find()` es más rápido pero menos preciso que `find_all()`.

**24. ¿Para qué sirve el método `.get_text(strip=True)` en un objeto de etiqueta de BeautifulSoup?**

    - a) Para obtener solo el texto del primer hijo de la etiqueta.
    - b) Para obtener todo el texto contenido dentro de la etiqueta y sus descendientes, eliminando espacios en blanco al inicio y final.
    - c) Para obtener el valor de un atributo llamado "text".
    - d) Para obtener el texto sin etiquetas HTML, pero conservando los espacios extra.

**25. Si quieres verificar si una imagen (`img_tag`) tiene un atributo `alt` vacío (ej. `alt=""`), ¿cuál sería la condición en Python?**

    - a) `img_tag.get('alt') == ""`
    - b) `not img_tag.get('alt')`
    - c) `img_tag.has_attr('alt') and len(img_tag['alt']) == 0`
    - d) a y c son correctas.

**26. ¿Qué biblioteca de Python es fundamental para crear y manipular DataFrames, útil para generar informes SEO?**

    - a) `Requests`
    - b) `BeautifulSoup`
    - c) `Pandas`
    - d) `NumPy`

**27. Al construir una URL absoluta a partir de una URL base (`base = "https://dominio.com"`) y un enlace relativo (`rel = "/pagina.html"`), ¿qué función de `urllib.parse` es la más adecuada?**

    - a) `urlparse(base, rel)`
    - b) `urljoin(base, rel)`
    - c) `urlsplit(base + rel)`
    - d) `urlencode({base: rel})`

**28. Un `sitemap.xml` generalmente NO incluye:**

    - a) URLs de imágenes importantes.
    - b) URLs que están bloqueadas por `robots.txt`.
    - c) La fecha de última modificación de una URL.
    - d) La prioridad de rastreo de una URL.

**29. ¿Cuál es el problema de usar enlaces internos en formato `http://` en un sitio que ya funciona bajo `https://`?**

    - a) Puede causar errores de "contenido mixto" si el navegador redirige mal.
    - b) Obliga a una redirección innecesaria de HTTP a HTTPS, afectando ligeramente el rendimiento.
    - c) Google podría indexar ambas versiones si no hay canonicals correctos.
    - d) Todas las anteriores.

**30. ¿Qué selector CSS usarías con `soup.select()` para encontrar una etiqueta `<div>` con la clase `content`?**

    - a) `soup.select('div.content')`
    - b) `soup.select('div#content')`
    - c) `soup.select('div[class~=content]')`
    - d) a y c son correctas, pero 'a' es más común para una sola clase.

**31. Si tienes una lista de diccionarios `datos_seo = [{'url': '...', 'titulo': '...'}, {'url': '...', 'titulo': '...'}]`, ¿cómo crearías un DataFrame de Pandas?**

    - a) `pd.DataFrame.from_list(datos_seo)`
    - b) `pd.DataFrame(datos_seo)`
    - c) `pd.Series(datos_seo).to_frame()`
    - d) `pd.load_dict(datos_seo)`

**32. La etiqueta `<meta name="viewport" content="width=device-width, initial-scale=1.0">` es crucial para:**

    - a) El SEO de imágenes.
    - b) La correcta visualización en dispositivos móviles (Responsive Design).
    - c) La carga diferida de JavaScript.
    - d) La definición del conjunto de caracteres.

**33. En el contexto de `robots.txt`, la directiva `Disallow: /admin/` significa:**

    - a) Permitir el rastreo de todo el directorio `/admin/`.
    - b) No permitir el rastreo de ningún contenido dentro del directorio `/admin/`.
    - c) Permitir el rastreo solo a Googlebot en `/admin/`.
    - d) Indicar que el directorio `/admin/` contiene el sitemap.

**34. ¿Cuál es el principal beneficio de usar el atributo `alt` en las imágenes para el SEO?**

    - a) Permite que las imágenes se carguen más rápido.
    - b) Proporciona contexto a los motores de búsqueda sobre el contenido de la imagen, ayudando en la búsqueda de imágenes.
    - c) Es obligatorio para que las imágenes se muestren en la página.
    - d) Define el tamaño de la imagen en la página.

**35. ¿Qué código de Python se usaría para obtener solo las URLs de una lista de etiquetas `<a>` almacenadas en `lista_enlaces`? (Asumiendo que cada `enlace` en `lista_enlaces` es un objeto Tag de BeautifulSoup)**

    - a) `[enlace.get('href') for enlace in lista_enlaces if enlace.get('href')]`
    - b) `[enlace.href for enlace in lista_enlaces]`
    - c) `[enlace.text for enlace in lista_enlaces]`
    - d) `[getattr(enlace, 'href') for enlace in lista_enlaces]`

**36. Si `response.elapsed.total_seconds()` devuelve `0.05` para una página, esto se considera un TTFB:**

    - a) Muy lento
    - b) Lento
    - c) Aceptable
    - d) Muy rápido

**37. Para verificar la presencia de Google Analytics, es común buscar subcadenas como `UA-` o `G-` en:**

    - a) `response.headers['Analytics']`
    - b) `soup.find('script', id='ga').string`
    - c) `response.text` (el contenido HTML crudo)
    - d) El archivo `robots.txt`

**38. Si una página tiene un título muy largo (ej. más de 70-80 caracteres), ¿cuál es la implicación SEO más probable?**

    - a) Será penalizada por Google directamente.
    - b) Se truncará en los resultados de búsqueda, pudiendo perder efectividad.
    - c) Mejorará el CTR al ofrecer más información.
    - d) No tiene ninguna implicación significativa.

**39. ¿Qué es un "favicon" y dónde se declara típicamente en HTML?**

    - a) Un script para validar formularios; se declara en el `<body>`.
    - b) Un pequeño icono que representa al sitio web (visible en pestañas del navegador); se declara en el `<head>`.
    - c) Una fuente personalizada para el sitio; se declara en el CSS.
    - d) Un cookie de seguimiento; se gestiona por el servidor.

**40. Al realizar scraping, si un sitio requiere JavaScript para mostrar contenido importante, ¿`requests.get().text` será suficiente para obtener ese contenido?**

    - a) Sí, `requests` ejecuta JavaScript como un navegador.
    - b) No, `requests` solo obtiene el HTML inicial; se necesitarían herramientas como Selenium o Playwright.
    - c) Sí, si se usa el header `User-Agent` correcto.
    - d) Depende de la versión de Python utilizada.

---
