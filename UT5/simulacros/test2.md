# Tanda 1: Test de SEO Técnico con BeautifulSoup

```
Sistema de Puntuación:

Respuesta correcta: Suma +0.25 puntos.
Respuesta incorrecta: Resta -0.08333... puntos (o la fracción 1/12).
Respuesta en blanco (no contestada): Suma o resta 0 puntos (no afecta la puntuación).
```

**1. Al iniciar un script de web scraping para análisis SEO, después de obtener el contenido HTML de una URL con `requests.get(url).text` y almacenarlo en `codigo_html`, ¿cuál es la forma correcta de parsear este contenido con BeautifulSoup?**

   - a) `soup = BeautifulSoup(codigo_html, 'lxml')`
   - b) `soup = BeautifulSoup.parse(codigo_html)`
   - c) `soup = BeautifulSoup(codigo_html, 'html.parser')`
   - d) `soup = html.parser(codigo_html)`

**2. Para extraer el contenido textual del título de una página HTML utilizando BeautifulSoup, una vez que tienes el objeto `soup`, ¿cuál de las siguientes opciones es la más directa y común, asumiendo que la etiqueta `title` existe?**

   - a) `soup.find('title').get_text()`
   - b) `soup.title.string`
   - c) `soup.find('head').find('title').text`
   - d) `soup.getText('title')`

**3. En el contexto de SEO, necesitas verificar si una página tiene una meta descripción. ¿Cuál es el método de BeautifulSoup más adecuado para encontrar la etiqueta `meta` de descripción y luego obtener su contenido?**

   - a) `soup.find("meta", name="description").get("content")` (asumiendo que la etiqueta existe)
   - b) `soup.find_all("meta")[0].text`
   - c) `soup.select("meta[name='description']").string`
   - d) `soup.find("description").text`

**4. ¿Cómo verificarías con BeautifulSoup que una página HTML contiene exactamente una etiqueta `<h1>`, lo cual es una práctica recomendada en SEO?**

   - a) `if soup.h1: print("Existe un H1")`
   - b) `len(soup.find_all('h1')) == 1`
   - c) `soup.find('h1').count == 1`
   - d) `bool(soup.find('h1'))`

**5. Al analizar imágenes (`<img>`) para SEO, es crucial verificar la presencia del atributo `alt`. Si tienes un objeto `img_tag` que representa una etiqueta `<img>`, ¿cómo comprobarías de forma segura si el atributo `alt` está ausente o es una cadena vacía?**

  -  a) `img_tag.alt == None or img_tag.alt == ""`
 -   b) `not img_tag.get('alt', '').strip()`
  -  c) `img_tag.find('alt').text == ""`
  -  d) `img_tag.has_attr('alt') == False`

**6. Para encontrar todas las etiquetas de encabezado (de `<h1>` a `<h6>`) en un documento HTML usando BeautifulSoup, ¿cuál sería la forma más eficiente?**

   - a) Realizar `soup.find_all()` para cada tipo de encabezado por separado y luego combinar las listas.
   - b) `soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])`
   - c) `soup.select('h1, h2, h3, h4, h5, h6')`
   - d) Iterar sobre todos los elementos y verificar el nombre de la etiqueta.

**7. Necesitas extraer la URL de destino de una etiqueta de enlace canónico (`<link rel="canonical" href="...">`). Si `canonical_tag` es el objeto BeautifulSoup para esta etiqueta, ¿cómo obtendrías la URL de forma segura (evitando un error si `href` no existe)?**

   - a) `canonical_tag.text`
   - b) `canonical_tag.get("href")`
   - c) `canonical_tag.attrs["href"]`
   - d) `canonical_tag.href`

**8. Cuando buscas específicamente etiquetas `<td>` que tienen un atributo `style` con un valor exacto, por ejemplo, `width: 14.8064%;`, ¿cuál es la sintaxis correcta con `find_all` para encontrar aquellas que *contienen* ese estilo específico (sabiendo que pueden tener más estilos)?**

   - a) `soup.find_all('td', style="width: 14.8064%;")`
   - b) `soup.find_all('td', attrs={'style': lambda x: x and 'width: 14.8064%;' in x})`
   - c) `soup.select('td[style*="width: 14.8064%;"]')`
   - d) b y c son correctas.

**9. Para verificar si una página utiliza Schema.org a través de JSON-LD, ¿qué tipo de etiqueta y atributo buscarías principalmente con BeautifulSoup?**

   - a) `soup.find_all("script", type="application/javascript")`
   - b) `soup.find_all("meta", name="schema")`
   - c) `soup.find_all("script", type="application/ld+json")`
   - d) `soup.find_all("div", class_="schema-org")`

**10. Al crear un informe de auditoría SEO básica y después de haber parseado el HTML con BeautifulSoup (`soup`), ¿cómo determinarías de forma booleana si la etiqueta `<meta name="description">` existe y tiene contenido?**

 - a) `soup.find("meta", attrs={"name": "description"}) is not None`
 - b) `desc = soup.find("meta", attrs={"name": "description"}); desc is not None and desc.get("content")`
 - c) `len(soup.select("meta[name='description'][content]")) > 0`
 - d) `soup.meta_description.exists() and soup.meta_description.has_content()`

---