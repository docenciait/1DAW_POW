# ✅ Test de Autoevaluación: SEO On-Page con Python (20 preguntas) 

**Instrucciones** : Elige la opción correcta. Solo una respuesta es válida por pregunta.


---



### 🧠 Fundamentos y herramientas 

**1.1.**  ¿Qué librería en Python es más adecuada para analizar el HTML de una página?

A) urllib

B) re

C) BeautifulSoup

D) time

**1.2.**  ¿Cuál de estas librerías se utiliza para hacer peticiones HTTP?

A) matplotlib

B) requests

C) pandas

D) os

**1.3.**  ¿Qué librería se usa para exportar datos a Excel desde Python?

A) numpy

B) selenium

C) pandas

D) hashlib

**1.4.**  ¿Cuál es el objetivo principal de BeautifulSoup?

A) Controlar formularios

B) Parsear (analizar) HTML y XML

C) Dibujar gráficos

D) Descargar archivos binarios

**1.5.**  ¿Qué función tiene `urljoin()` en el análisis de enlaces?

A) Analiza direcciones IP

B) Convierte URL a mayúsculas

C) Une URLs base con relativas

D) Divide una URL en partes


---



### 🔍 Elementos SEO on-page 

**2.1.**  ¿Cuál es la etiqueta principal que debe representar el título del contenido?

A) `<title>`

B) `<h1>`

C) `<meta>`

D) `<header>`

**2.2.**  ¿Cuál es la longitud recomendada para una etiqueta `<title>`?

A) Máximo 20 caracteres

B) Entre 60 y 70 caracteres

C) Más de 100 caracteres

D) No tiene límite

**2.3.**  ¿Qué atributo de la imagen se analiza para evaluar la accesibilidad y el SEO?

A) `src`

B) `href`

C) `alt`

D) `class`

**2.4.**  ¿Cuál de estos códigos HTTP indica un enlace roto?

A) 200

B) 301

C) 403

D) 404

**2.5.**  ¿Qué metaetiqueta se usa para evitar que una página sea indexada?

A) `<meta name="robots" content="noindex">`

B) `<meta charset="UTF-8">`

C) `<meta name="canonical">`

D) `<meta name="nofollow">`


---



### ✍️ Análisis de contenido y palabras clave 

**3.1.**  ¿Qué hace la función `get_text()` en BeautifulSoup?

A) Elimina los enlaces

B) Extrae todo el texto visible del HTML

C) Extrae solo el contenido de imágenes

D) Corta el contenido

**3.2.**  ¿Qué son las “stopwords”?

A) Enlaces rotos

B) Palabras que deben destacarse

C) Palabras comunes que se excluyen del análisis

D) Palabras duplicadas

**3.3.**  ¿Para qué se usa `collections.Counter()`?

A) Ordenar listas alfabéticamente

B) Contar elementos repetidos

C) Dividir cadenas de texto

D) Verificar enlaces rotos

**3.4.**  ¿Qué estructura de datos devuelve `Counter(palabras)`?

A) Lista

B) Diccionario

C) Tupla

D) Conjunto (set)

**3.5.**  ¿Cuál es un buen indicador de que una página tiene contenido suficiente para SEO?

A) Más de 50 palabras

B) Más de 100 enlaces

C) Más de 300 palabras de contenido real

D) Tener un sitemap


---



### 🧪 Práctica con enlaces, imágenes y exportación 

**4.1.**  ¿Cómo detectamos imágenes sin atributo `alt` con BeautifulSoup?

A) `img.get("src") == None`

B) `img.get("alt") == None`

C) `img.has_class("alt")`

D) `img.text == ""`

**4.2.**  ¿Qué atributo usamos para identificar un enlace canónico?

A) `rel="canonical"`

B) `name="robots"`

C) `meta="description"`

D) `href="canonical"`

**4.3.**  ¿Qué diferencia hay entre un enlace interno y uno externo?

A) El interno usa `mailto:`

B) El externo tiene un dominio distinto

C) El externo no tiene protocolo

D) El interno es siempre un script

**4.4.**  ¿Qué código HTTP representa acceso prohibido?

A) 302

B) 200

C) 403

D) 100

**4.5.**  ¿Qué función usamos en pandas para guardar un DataFrame en Excel?

A) `save_as_excel()`

B) `export_excel()`

C) `to_excel()`

D) `write_xls()`


---



### 🧩 Verificación de estructura SEO (código) 

**5.1.**  `soup.title.string.strip()` ¿Qué hace este código?

A) Elimina las etiquetas `<title>`

B) Devuelve el contenido de la etiqueta `<title>` sin espacios

C) Reemplaza el título por vacío

D) Convierte el título en mayúsculas

**5.2.**  `img.get("alt")` ¿Qué analiza en SEO técnico?

A) Extrae la dirección de una imagen

B) Comprueba el tipo de archivo

C) Verifica si tiene texto alternativo

D) Devuelve la altura de la imagen

**5.3.**  ¿Qué devuelve si se encuentra un enlace canónico?

A) Contenido del `<meta name="robots">`

B) Valor del `href` del canonical

C) El título de la página

D) Todos los enlaces rotos

**5.4.**  `texto = soup.get_text().lower()` ¿Qué hace?

A) Extrae solo los títulos

B) Limpia HTML y pasa a minúsculas

C) Convierte imágenes a texto

D) Cuenta párrafos

**5.5.**  `Counter(palabras)` ¿Qué hace?

A) Agrupa imágenes por nombre

B) Cuenta cuántas veces aparece cada palabra

C) Ordena palabras alfabéticamente

D) Convierte una lista en string


---



## ✅ Plantilla de soluciones 

| Pregunta | Respuesta correcta | 
| --- | --- | 
| 1.1 | C | 
| 1.2 | B | 
| 1.3 | C | 
| 1.4 | B | 
| 1.5 | C | 
| 2.1 | B | 
| 2.2 | B | 
| 2.3 | C | 
| 2.4 | D | 
| 2.5 | A | 
| 3.1 | B | 
| 3.2 | C | 
| 3.3 | B | 
| 3.4 | B | 
| 3.5 | C | 
| 4.1 | B | 
| 4.2 | A | 
| 4.3 | B | 
| 4.4 | C | 
| 4.5 | C | 
| 5.1 | B | 
| 5.2 | C | 
| 5.3 | B | 
| 5.4 | B | 
| 5.5 | B | 
