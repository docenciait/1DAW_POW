| **Módulo SEO**           |  Test 30 (4 alt, 1 corr.)                    | **Puntos:** Corr.:+0.33, 3 Incorrectas Resta 1C                   |
| :----------------------------- | :--------------------------------------- | :--------------------------------- |
| **Fecha:** 15 Mayo 2025 - 8:15H| **Curso:** 1º DAW        | **Calificación:** 0-10             |
| **Duración:** 45min                 | **Lugar:** Salón Actos      | **RA:** RA5                        |
| **ALUMNO/A:**                 |   |  **CALIF:.**                      |


---

1. **¿Cuál es el propósito de la línea soup = BeautifulSoup(response.text, "html.parser")?**

```
a) Descargar los encabezados HTML desde el sitio web
b) Renderizar una página dinámica con JavaScript
c) Convertir el HTML recibido en un objeto manipulable por Python ✅
d) Buscar enlaces en la página
```

2. **Al iniciar un script de web scraping para análisis SEO, después de obtener el contenido HTML de una URL con `requests.get(url).text` y almacenarlo en `codigo_html`, ¿cuál es la forma correcta de parsear este contenido con BeautifulSoup?**

```
a) soup = BeautifulSoup(codigo_html, 'lxml')
b) soup = BeautifulSoup.parse(codigo_html)
c) soup = BeautifulSoup(codigo_html, 'html.parser') ✅
d) soup = html.parser(codigo_html)
```

3. **Cuando buscas específicamente etiquetas `<td>` que tienen un atributo `style` con un valor exacto, por ejemplo, `width: 14.8064%; height: 56px;`, ¿cuál es la sintaxis correcta con `find_all`?**

```
a) soup.find_all('td', style="width: 14.8064%; height: 56px;")
b) soup.find_all('td', attrs={'style': "width: 14.8064%; height: 56px;"}) ✅
c) soup.select('td[style="width: 14.8064%; height: 56px;"]')
d) soup.find_all(tag='td', attributes={'style': "width: 14.8064%; height: 56px;"})
```

4. **Para verificar si una página utiliza Schema.org a través de JSON-LD, ¿qué tipo de etiqueta y atributo buscarías principalmente con BeautifulSoup?**

```
a) soup.find_all("script", type="application/javascript")
b) soup.find_all("meta", name="schema")
c) soup.find_all("script", type="application/ld+json") ✅
d) soup.find_all("div", class_="schema-org")
```

5. **¿Qué hace la función `get_text()` en BeautifulSoup?**
```
a) Elimina los enlaces
b) Extrae todo el texto visible del HTML  ✅
c) Extrae solo el contenido de imágenes
d) Corta el contenido
```

6. `soup.title.string.strip()` **¿Qué hace este código cuando se ha extraído la información con BS4?**
```
a) Elimina las etiquetas <title>
b) Devuelve el contenido de la etiqueta`<title> sin espacios  ✅
c) Reemplaza el título por vacío
d) Convierte el título en mayúsculas
```

7. `texto = soup.get_text().lower()` **¿Qué hace en el contexto de BS4?**
```
a) Extrae solo los títulos
b) Limpia HTML y pasa a minúsculas ✅
c) Convierte imágenes a texto
d) Cuenta párrafos
```

8. **¿Qué tipo de palabras se eliminan para que el análisis sea útil en SEO?**
```
a) Palabras largas y en inglés
b) Palabras muy técnicas
c) Palabras comunes sin valor semántico (stopwords) ✅
d) Palabras duplicadas dentro del HTML
```

9. **¿Qué hace la línea `ul = soup.find('ul', class_="listado carreras grado")` en el contexto del scraping con BeautifulSoup?**
```
a) Busca todos los elementos <ul> que contengan carreras de grado con cualquier clase.
b) Encuentra el primer elemento <ul> con la clase exacta "listado carreras grado" y lo asigna a ul. ✅
c) Extrae todos los elementos <li> con la clase "carreras grado" de una lista.
d) Encuentra todos los elementos <ul> que tengan una clase que contenga la palabra "listado".
```

10. **Busca el primer elemento <div> en el documento HTML y lo asigna a div_tag.**
```
a) div_tag = soup.find_all('div')[0]
b) div_tag = soup.select_one('div')
c) div_tag = soup.find('div') ✅
d) div_tag = soup.get('div')
```

11. **Retorna el primer elemento enlace de la URL.**
```
a) link = soup.find_all('link')[0]
b) link = soup.select_one('a[href]')
c) link = soup.find('a') ✅
d) link = soup.get('a')
```

12. **¿Qué análisis SEO podrías realizar con el siguiente código? `soup.find_all('img', alt=False)`**
```
a) Verificar cuántas imágenes no tienen la etiqueta <img>
b) Detectar imágenes sin atributo alt, lo que afecta a la accesibilidad y SEO ✅
c) Encontrar imágenes grandes que ralentizan el sitio
d) Obtener imágenes con enlaces rotos
```

13. **¿Qué permite detectar el siguiente código desde una perspectiva SEO? `len(soup.find_all('h1'))`**
```
a) La cantidad de enlaces internos en el sitio
b) El número total de palabras clave en el texto
c) Si hay más de un <h1>, lo cual es un error estructural SEO ✅
d) La cantidad de títulos duplicados
```

14. **Después de haber parseado el HTML con BeautifulSoup (`soup`), ¿cómo determinarías de forma booleana si la etiqueta `<meta name="description">` existe?**
```
a) soup.find("meta", attrs={"name": "description"}) != None ✅
b) "description" in soup.find("meta").attrs
c) len(soup.select("meta[name='description']")) > 0
d) soup.meta_description.exists()
```
15. **Cómo verificarías con BeautifulSoup que una página HTML contiene exactamente una etiquecta `<h1>`**

```
a) soup.find('h1') == 1
b) soup.select('h1') == 1
c) len(soup.find_all('h1')) == 1 ✅
d) soup.h1.count() == 1
```
16. **¿Cuál es el propósito principal de usar `if soup.title else "No encontrado" `al intentar extraer el texto de un título?**
```
a) Para asegurar que el título no exceda una longitud máxima.
✅ b) Para evitar un error AttributeError si la etiqueta title no existe en el HTML.
c) Para convertir el título a minúsculas.
d) Para añadir "No encontrado" si el título está vacío.
```
17. **Si estás comprobando enlaces internos rotos, y tienes una URL base https://example.com, un enlace como href="/pagina" se considera interno. ¿Cómo construirías la URL completa para hacer una petición requests.get() a este enlace relativo?**
```
a) requests.get("/pagina")
b) requests.get("https://example.com" + "pagina")
c) requests.get_relative("https://example.com", "pagina")
✅ d) requests.get(urljoin("https://example.com", "/pagina"))
```

18. **¿Qué detecta este código? `no_alt = [img for img in soup.find_all('img') if not img.get('alt')]`**
```
a) Imágenes duplicadas
b) Imágenes grandes sin compresión
c) Imágenes sin texto alternativo, lo cual afecta a la accesibilidad y SEO ✅
d) Imágenes rotas
```

19. **¿Qué hace requests.head(link, timeout=5) cuando se utiliza en un scraping SEO?**
```
a) Obtiene solo los encabezados de la respuesta HTTP, sin el cuerpo del contenido.
b) Descarga completamente el contenido de la página web, lo que lo hace más eficiente que requests.get().
✅ c) Envía una solicitud HTTP de tipo HEAD para verificar si un enlace está roto y comprobar el tiempo de respuesta de la página.
d) Realiza una petición GET completa de la página web, incluyendo el contenido del cuerpo.
```

20. **¿Qué se está verificando con la expresión `urlparse(href).netloc == "" or urlparse(href).netloc == urlparse(url).netloc` en un script de scraping SEO?**
```
a) Que el enlace href apunta a una dirección HTTPS válida.
b) Que el enlace href está roto o devuelve error 404.
✅ c) Que el enlace href es interno 
d) Que el enlace href redirige automáticamente a la página de inicio del sitio.
```
21. **url ya está dada, qué estás haciendo con el siguiente fragmento de código?** `robots_url = url + "/robots.txt"; r = requests.get(robots_url)`
```
a) Estás comprobando si el sitio web utiliza sitemap.xml correctamente.
b) Estás extrayendo el contenido HTML del archivo robots.html.
✅ c) Estás solicitando el archivo robots para analizar las directivas que indican qué partes del sitio pueden ser rastreadas por bots.
d) Estás accediendo al panel de administración del sitio para hacer login.
```
22. **¿Cuál es el propósito de usar `requests.get()` junto con `response.elapsed.total_seconds()` en un análisis que impacte en el rendimiento SEO?**
```
a) Para obtener el número de enlaces internos de la página.
b) Para verificar si la página redirige correctamente a HTTPS.
✅ c) Para medir el tiempo de carga del servidor (Time To First Byte), lo cual impacta en el rendimiento SEO.
d) Para analizar si las imágenes tienen el atributo alt.
```

23. **¿Qué se está comprobando con `parsed.netloc == parsed_base.netloc and not full_url.startswith("https://")` en un análisis SEO técnico?**
```
a) Que el enlace pertenece a otro dominio y no está bien enlazado con rel="nofollow".
b) Que el enlace tiene un protocolo FTP y no HTTP/HTTPS.
✅ c) Que el enlace es interno pero no usa HTTPS, lo cual puede afectar negativamente al SEO por falta de seguridad.
d) Que el enlace apunta a un recurso multimedia como una imagen o vídeo externo.
```
24. **¿Qué puedes deducir si `requests.head(link).status_code == 404` al auditar enlaces de una web?**
```
a) Que el enlace se carga correctamente.
✅ b) Que el enlace está roto y no lleva a una página válida.
c) Que es un redireccionamiento interno.
d) Que el contenido está protegido por robots
```

25. **¿Qué instrucción usarías para encontrar el <meta> que define la descripción de la página?**
```
a) soup.find("meta", name="description")
b) soup.get("meta").description
✅ c) soup.find("meta", attrs={"name": "description"})
d) soup.find("meta[name='description']")
```

26. **¿Cómo obtienes todas las etiquetas <strong> para evaluar uso excesivo de énfasis en SEO?**
```
✅ a) soup.find_all("strong")
b) soup.select("b")
c) soup.strongs()
d) soup.get("strong")
```
27. **¿Cómo detectar si una página tiene múltiples etiquetas `<h1>`, lo cual es negativo para SEO?**
```
a) soup.count("h1") > 1
b) len(soup.select("h1")) > 1.0
✅ c) len(soup.find_all("h1")) > 1
d) soup.h1 > 1
```

28. **Tienes un documento HTML con múltiples elementos que comparten la misma clase, por ejemplo, `<div class="product-title">...</div>`. Quieres obtener el texto de todos estos elementos. ¿Qué combinación de métodos utilizarías?**
```
a) soup.find('div', class_='product-title').get_text()
b) soup.select('.product-title')[0].text
✅  c) soup.find_all('div', class_='product-title') y luego iterar sobre los resultados para obtener .text o .get_text().
d) soup.find_class('product-title').all_text()
```

29. **En el contexto de SEO, necesitas verificar si una página tiene una meta descripción. ¿Cuál es el método de BeautifulSoup más adecuado para encontrar la etiqueta `meta` de descripción y luego obtener su contenido?**
```
✅  a) soup.find("meta", name="description").get("content") (asumiendo que la etiqueta existe)
b) soup.find_all("meta")[0].text
c) soup.select("meta[name='description']").string
d) soup.find("description").text
```
30. **Quieres asegurarte de que una página responsive tenga la meta etiqueta viewport correctamente configurada. ¿Cuál es la forma más precisa de buscar la etiqueta `<meta name="viewport">`?**
```
a) soup.find("meta", viewport=True)
b) soup.select_one("meta[name=viewport]")
c) soup.find("meta", attrs={"name": "viewport"})
✅ d) B y C son correctas.
```
---
| Pregunta | Respuesta | Pregunta | Respuesta  |
|---|---|---|---|
| 1.  |  | 16. |  |
| 2.  |  | 17. |  |
| 3.  |  | 18. |  |
| 4.  |  | 19. |  |
| 5.  |  | 20. |  |
| 6.  |  | 21. |  |
| 7.  |  | 22. |  |
| 8.  |  | 23. |  |
| 9.  |  | 24. |  |
| 10. |  | 25. |  |
| 11. |  | 26. |  |
| 12. |  | 27. |  |
| 13. |  | 28. |  |
| 14. |  | 29. |  |
| 15. |  | 30. |  |

---

1.  c) Convierte el HTML en un objeto navegable.
2.  c) Sintaxis correcta para parsear con el parser estándar de Python.
3.  b) Uso correcto del argumento `attrs` para buscar por valor exacto de atributo.
4.  c) JSON-LD se incrusta en `<script type="application/ld+json">`.
5.  b) Extrae todo el texto visible de un elemento y sus descendientes.
6.  b) Accede al texto del título (`.string`) y elimina espacios (`.strip()`).
7.  b) Extrae texto visible (`.get_text()`) y lo convierte a minúsculas (`.lower()`).
8.  c) Las stopwords no aportan significado semántico clave para el análisis.
9.  b) `find` busca el primer elemento, `class_` busca por clase exacta.
10. c) `find('div')` busca la primera etiqueta `div`.
11. c) `find('a')` busca la primera etiqueta de enlace.
12. b) `alt=False` busca elementos `<img>` sin atributo `alt`.
13. c) `len(find_all('h1'))` cuenta los h1; más de uno es error SEO común.
14. a) Comprueba si `find` encontró la etiqueta (no es `None`).
15. c) Cuenta todos los `<h1>` y verifica si la cantidad es exactamente 1.
16. b) Maneja el caso donde `soup.title` es `None` para evitar errores.
17. d) `urljoin` combina una URL base con una ruta relativa correctamente.
18. c) Lista de comprensión que filtra `<img>` donde `get('alt')` devuelve `None` o `""`.
19. c) Envía solicitud HEAD para verificar estado (como 404) y tiempo sin descargar contenido.
20. c) Verifica si el dominio del enlace es vacío (relativo) o igual al dominio base.
21. c) Descarga el contenido del archivo estándar `robots.txt`.
22. c) `response.elapsed.total_seconds()` mide el tiempo de respuesta (TTFB).
23. c) Verifica enlaces al mismo dominio (`netloc`) que no usan HTTPS.
24. b) El código de estado 404 significa "No Encontrado", enlace roto.
25. c) Uso preciso de `find` con `attrs` para la meta descripción.
26. a) `find_all()` busca todas las ocurrencias de la etiqueta especificada.
27. c) Cuenta todos los `<h1>` y verifica si el número es mayor que 1.
28. c) `find_all` obtiene todos los elementos; se itera para extraer texto de cada uno.
29. a) Combina encontrar la meta descripción y extraer su atributo `content`.
30. d) Ambas b) (selector CSS) y c) (find con attrs) son formas precisas de encontrar la meta viewport.