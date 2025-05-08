## Test 3

```
Sistema de Puntuación:

Respuesta correcta: Suma +0.25 puntos.
Respuesta incorrecta: Resta -0.08333... puntos (o la fracción 1/12).
Respuesta en blanco (no contestada): Suma o resta 0 puntos (no afecta la puntuación).
```


**1. Si necesitas extraer todos los enlaces (`<a>`) de una página que apuntan a un dominio externo específico, ¿cómo podrías filtrar los resultados de `soup.find_all('a')`? (Asume que `enlaces` es la lista de todas las etiquetas `<a>`)**

   - a) `[link for link in enlaces if link.get('href') and 'external.com' in link.get('href')]`
   - b) `soup.find_all('a', href_contains='external.com')`
   - c) `[link for link in enlaces if link['href'].startswith('http://external.com')]` (esto no cubriría https o variaciones)
   - d) `soup.select("a[href*='external.com']")`

**2. Para implementar una comprobación de "contenido mixto" (recursos HTTP en una página HTTPS), necesitas inspeccionar atributos como `src` en `<img>` y `<script>`, y `href` en `<link>`. Si tu página principal es HTTPS, ¿cuál sería una condición de BeautifulSoup para identificar un recurso de imagen problemático?**

   - a) `img_tag.get('src') and img_tag.get('src').startswith('http://')` (asumiendo que `img_tag` es un elemento `<img>`)
   - b) `img_tag.src.is_http()`
   - c) `soup.find('img', src_protocol='http')`
   - d) `img_tag['src'].protocol == 'http'`

**3. Al verificar las etiquetas `hreflang` para SEO internacional, buscas etiquetas `<link rel="alternate" hreflang="...">`. ¿Cómo encontrarías todas estas etiquetas y luego accederías al valor del atributo `hreflang` para la primera etiqueta encontrada (`hreflang_tag`)?**

  -  a) `tags = soup.find_all('link', rel='alternate'); hreflang_tag = tags[0]; value = hreflang_tag.hreflang`
  -  b) `tags = soup.find_all('link', attrs={'rel':'alternate', 'hreflang': True}); hreflang_tag = tags[0]; value = hreflang_tag.get('hreflang')` (asumiendo que `tags` no está vacío)
  -  c) `soup.select("link[rel=alternate][hreflang]")[0].get_attribute('hreflang')`
  -  d) `soup.find('link', rel='alternate').get('hreflang')` (esto solo encontraría la primera, no todas)

**4. Quieres asegurarte de que una página responsive tenga la meta etiqueta viewport correctamente configurada. ¿Cuál es la forma más precisa de buscar la etiqueta `<meta name="viewport">`?**

 -   a) `soup.find("meta", viewport=True)`
  -  b) `soup.select_one("meta[name=viewport]")`
  -  c) `soup.find("meta", attrs={"name": "viewport"})`
  -  d) B y C son correctas.

**5. Al iterar sobre una lista de `td_elements` obtenida con `soup.find_all('td')`, ¿cómo extraerías el texto limpio (sin espacios extra al inicio/final) de cada celda?**

  -  a) `[td.text.strip() for td in td_elements]`
 -   b) `[td.string.clean() for td in td_elements]`
  -  c) `[td.get_text(strip=True) for td in td_elements]`
  -  d) A y C son correctas.

**6. Si necesitas verificar la existencia de un favicon declarado como `<link rel="icon" href="/favicon.ico">` o `<link rel="shortcut icon" href="/favicon.ico">`, ¿cuál opción de BeautifulSoup es más flexible para encontrar cualquiera de estas dos formas?**

 -   a) `soup.find("link", rel="icon") or soup.find("link", rel="shortcut icon")`
  -  b) `soup.find("link", attrs={"rel": ["icon", "shortcut icon"]})` (Esto no funciona como se espera con listas en `attrs` para valores alternativos)
 -   c) `soup.select_one("link[rel='icon'], link[rel='shortcut icon']")`
 -   d) A y C son correctas.

**7. En un ejercicio para extraer datos de una tabla (`<table>`), si quieres obtener todas las filas (`<tr>`) y luego, para cada fila, obtener todas sus celdas (`<td>`), ¿cuál sería la estructura de bucle anidado más común con BeautifulSoup?**

 -   a) `for row in soup.find_all('tr'): for cell in row.find_all('td'): print(cell.text)`
 -   b) `for cell in soup.find_all('td'): for row in cell.find_parents('tr'): print(cell.text)`
 -   c) `rows = soup.table.find_all_next('tr'); for row in rows: cells = row.find_all_next('td'); ...`
 -   d) `soup.select("table tr td")` (esto selecciona las celdas, pero la pregunta es sobre la estructura del bucle)

**8. ¿Cuál es el propósito principal de usar `if soup.title else "No encontrado"` al intentar extraer el texto de un título?**

 -   a) Para asegurar que el título no exceda una longitud máxima.
 -   b) Para evitar un error `AttributeError` si la etiqueta `title` no existe en el HTML.
 -   c) Para convertir el título a minúsculas.
 -   d) Para añadir "No encontrado" si el título está vacío.

**9. Si estás comprobando enlaces internos rotos, y tienes una URL base `https://example.com`, un enlace como `href="/pagina"` se considera interno. ¿Cómo construirías la URL completa para hacer una petición `requests.get()` a este enlace relativo?**

 -   a) `requests.get("/pagina")`
 -   b) `requests.get("https://example.com" + "/pagina")`
 -   c) `requests.get_relative("https://example.com", "/pagina")`
 -   d) `requests.get(urljoin("https://example.com", "/pagina"))` (asumiendo `from urllib.parse import urljoin`)

**10. Al realizar una auditoría SEO, se crea un diccionario `info` para luego convertirlo a un DataFrame de Pandas. Si quieres registrar si Google Analytics está presente buscando subcadenas como "UA-" o "G-" en `response.text` (el contenido HTML crudo), ¿cuál es una forma pythonica de hacerlo?**

- a) `analytics_found = False; if "UA-" in response.text or "G-" in response.text: analytics_found = True`
- b) `analytics_found = any(tracker_id in response.text for tracker_id in ["UA-", "G-", "gtag(", "ga("])`
- c) `analytics_found = response.text.contains("UA-") or response.text.contains("G-")`
- d) `analytics_found = soup.find(string=["UA-", "G-"]) is not None`








