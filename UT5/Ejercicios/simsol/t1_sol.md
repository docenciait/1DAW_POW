# Test 1

```text
Respuestas Correctas TEST1:

1b) soup.title.string (Es la forma más idiomática y directa que se muestra en los notebooks para obtener el contenido de la etiqueta title).

2a) soup.find("meta", name="description") (Es la forma más común y específica para encontrar la etiqueta meta descripción por su atributo name). Aunque soup.select también funciona, find con attrs o argumentos de palabra clave es muy común en los ejemplos.

3b) len(soup.find_all('h1')) == 1 (Esta opción cuenta el número de etiquetas <h1> y lo compara con 1, que es la forma explícita mostrada en los ejercicios).

4b) not img_tag.get('alt') (El método .get('alt') devolverá None si el atributo no existe, o la cadena vacía si existe pero está vacío. Ambas situaciones evalúan a False en un contexto booleiano cuando se niegan, cubriendo ambos casos de "ausente o vacío" de forma concisa, como se practica en los notebooks).

5b) soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) (Pasar una lista de nombres de etiquetas a find_all es la manera eficiente de buscar múltiples tipos de etiquetas simultáneamente).

6b) canonical_tag.get("href") (El método .get() es la forma segura de acceder a los atributos de una etiqueta, ya que devuelve None si el atributo no existe, evitando errores).

7b) soup.find_all('td', attrs={'style': "width: 14.8064%; height: 56px;"}) (La forma correcta de pasar atributos específicos con sus valores a find_all es usando el argumento attrs con un diccionario).

8c) soup.find_all("script", type="application/ld+json") (JSON-LD se incrusta comúnmente en etiquetas <script> con el tipo application/ld+json).

9d) Todas las opciones b y c son correctas y a también podría funcionar dependiendo de la versión y el contexto de uso de BeautifulSoup. (href=True en find_all busca la presencia del atributo. La opción b usa una lambda para la misma lógica, y la opción c es una comprensión de lista que filtra explícitamente. Todas son válidas, aunque a es la más concisa).

10a) soup.find("meta", attrs={"name": "description"}) != None (Esto verifica si el método find devuelve un objeto etiqueta o None, lo cual indica la presencia o ausencia de la etiqueta, una práctica común en los ejemplos de auditoría).
```

# TEST 2



1.  **c) `soup = BeautifulSoup(codigo_html, 'html.parser')`**
2.  **b) `soup.title.string`**
3.  **a) `soup.find("meta", name="description").get("content")`** (asumiendo que la etiqueta existe)
4.  **b) `len(soup.find_all('h1')) == 1`**
5.  **b) `not img_tag.get('alt', '').strip()`** (Cubre ausencia, `None`, y cadenas vacías o con solo espacios)
6.  **b) `soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])`**
7.  **b) `canonical_tag.get("href")`**
8.  **d) b y c son correctas.** (La opción 'b' usa una lambda para una comprobación flexible del contenido del atributo `style`. La opción 'c' usa un selector CSS que busca la subcadena dentro del atributo `style`. Ambas son válidas para este caso).
9.  **c) `soup.find_all("script", type="application/ld+json")`**
10. **b) `desc = soup.find("meta", attrs={"name": "description"}); desc is not None and desc.get("content")`** (Primero verifica existencia, luego que `get("content")` no sea `None` ni vacío, lo cual evalúa a `True` si tiene contenido).


# TEST 3


1.  **d) `soup.select("a[href*='external.com']")`** (La opción 'a' también es correcta y muy pythonica. La 'd' usa selectores CSS que son poderosos para este tipo de coincidencias de subcadena en atributos. Ambas son buenas, pero 'd' es más específica de la sintaxis de selectores que BeautifulSoup soporta bien).
2.  **a) `img_tag.get('src') and img_tag.get('src').startswith('http://')`** (Comprueba primero que `src` exista y luego que comience con `http://`)
3.  **b) `tags = soup.find_all('link', attrs={'rel':'alternate', 'hreflang': True}); hreflang_tag = tags[0]; value = hreflang_tag.get('hreflang')`** (Busca la combinación de `rel="alternate"` y la presencia del atributo `hreflang`, luego obtiene su valor).
4.  **d) B y C son correctas.** (`soup.select_one("meta[name=viewport]")` y `soup.find("meta", attrs={"name": "viewport"})` son formas efectivas de encontrar la etiqueta).
5.  **d) A y C son correctas.** (`.text.strip()` y `.get_text(strip=True)` logran el mismo resultado de extraer texto limpio).
6.  **d) A y C son correctas.** (La opción 'a' usa un `or` lógico entre dos búsquedas `find`. La opción 'c' usa un selector CSS con una coma para indicar 'o' entre selectores).
7.  **a) `for row in soup.find_all('tr'): for cell in row.find_all('td'): print(cell.text)`** (Esta es la estructura estándar para iterar filas y luego celdas dentro de cada fila).
8.  **b) Para evitar un error `AttributeError` si la etiqueta `title` no existe en el HTML.** (Si `soup.title` es `None`, acceder a `.string` directamente causaría un error).
9.  **d) `requests.get(urljoin("https://example.com", "/pagina"))`** (asumiendo `from urllib.parse import urljoin`) (`urljoin` es la forma más robusta de combinar URLs base y relativas).
10. **b) `analytics_found = any(tracker_id in response.text for tracker_id in ["UA-", "G-", "gtag(", "ga("])`** (Esta es una forma concisa y eficiente de verificar si alguna de las subcadenas está presente).