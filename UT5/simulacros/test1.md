# Test 1
```
Sistema de Puntuación:

Respuesta correcta: Suma +0.25 puntos.
Respuesta incorrecta: Resta -0.08333... puntos (o la fracción 1/12).
Respuesta en blanco (no contestada): Suma o resta 0 puntos (no afecta la puntuación).
```

**1. Para extraer el contenido textual del título de una página HTML utilizando BeautifulSoup, una vez que tienes el objeto `soup`, ¿cuál de las siguientes opciones es la más directa y común, asumiendo que la etiqueta `title` existe?**

   - a) `soup.find('title').get_text()`
   - b) `soup.title.string`
   - c) `soup.find('head').find('title').text`
   - d) `soup.getText('title')`

**2. En el contexto de SEO, necesitas verificar si una página tiene una meta descripción. ¿Cuál es el método de BeautifulSoup más adecuado para encontrar la etiqueta `meta` de descripción?**

  - a) `soup.find("meta", name="description")`
  - b) `soup.find_all("meta")[0].get("content")`
  - c) `soup.select("meta[name='description']")`
  - d) `soup.find("description").text`

**3. ¿Cómo verificarías con BeautifulSoup que una página HTML contiene exactamente una etiqueta `<h1>`, lo cual es una práctica recomendada en SEO?**

  - a) `if soup.h1: print("Existe un H1")`
  - b) `len(soup.find_all('h1')) == 1`
  - c) `soup.find('h1').count == 1`
  - d) `bool(soup.find('h1'))`

**4. Al analizar imágenes para SEO, es crucial verificar la presencia del atributo `alt`. Si tienes un objeto `img_tag` que representa una etiqueta `<img>`, ¿cómo comprobarías si el atributo `alt` está ausente o vacío?**

  - a) `img_tag.alt == None`
  - b) `not img_tag.get('alt')`
  - c) `img_tag.find('alt').text == ""`
  - d) `img_tag.has_attribute('alt') == False`

**5. Para encontrar todas las etiquetas de encabezado (de `<h1>` a `<h6>`) en un documento HTML usando BeautifulSoup, ¿cuál sería la forma más eficiente?**

  - a) Realizar `soup.find_all()` para cada tipo de encabezado por separado y luego combinar las listas.
  - b) `soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])`
  - c) `soup.select('h1, h2, h3, h4, h5, h6')`
  - d) Iterar sobre todos los elementos y verificar el nombre de la etiqueta.

**6. Necesitas extraer la URL de destino de una etiqueta de enlace canónico (`<link rel="canonical" href="...">`). Si `canonical_tag` es el objeto BeautifulSoup para esta etiqueta, ¿cómo obtendrías la URL?**

  - a) `canonical_tag.text`
  - b) `canonical_tag.get("href")`
  - c) `canonical_tag.attrs["href"]`
  - d) `canonical_tag.href`

**7. Cuando buscas específicamente etiquetas `<td>` que tienen un atributo `style` con un valor exacto, por ejemplo, `width: 14.8064%; height: 56px;`, ¿cuál es la sintaxis correcta con `find_all`?**

  - a) `soup.find_all('td', style="width: 14.8064%; height: 56px;")`
  - b) `soup.find_all('td', attrs={'style': "width: 14.8064%; height: 56px;"})`
  - c) `soup.select('td[style="width: 14.8064%; height: 56px;"]')`
  - d) `soup.find_all(tag='td', attributes={'style': "width: 14.8064%; height: 56px;"})`

**8. Para verificar si una página utiliza Schema.org a través de JSON-LD, ¿qué tipo de etiqueta y atributo buscarías principalmente con BeautifulSoup?**

  - a) `soup.find_all("script", type="application/javascript")`
  - b) `soup.find_all("meta", name="schema")`
  - c) `soup.find_all("script", type="application/ld+json")`
  - d) `soup.find_all("div", class_="schema-org")`

**9. Si quieres encontrar todos los enlaces `<a>` que tienen un atributo `href` definido (independientemente de su valor), ¿cuál es la forma correcta de hacerlo con BeautifulSoup?**

  - a) `soup.find_all('a', href=True)`
  - b) `soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href'))`
  - c) `[tag for tag in soup.find_all('a') if tag.get('href')]`
  - d) Todas las opciones b y c son correctas y a también podría funcionar dependiendo de la versión y el contexto de uso de BeautifulSoup.

**10. Al crear un informe de auditoría SEO básica con Pandas, y después de haber parseado el HTML con BeautifulSoup (`soup`), ¿cómo determinarías de forma booleana si la etiqueta `<meta name="description">` existe?**

   - a) `soup.find("meta", attrs={"name": "description"}) != None`
   - b) `"description" in soup.find("meta").attrs`
   - c) `len(soup.select("meta[name='description']")) > 0`
   - d) `soup.meta_description.exists()`

---