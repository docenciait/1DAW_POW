import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from collections import Counter

# Paso 1: Obtener contenido de la página web
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al obtener la página: {response.status_code}")
        return None

# Paso 2: Analizar las palabras más comunes (SEO)
def analyze_keywords(text):
    # Usamos BeautifulSoup para limpiar el HTML
    soup = BeautifulSoup(text, 'html.parser')
    # Extraemos todo el texto visible
    page_text = soup.get_text().lower().split()

    # Contamos las palabras más frecuentes
    word_counts = Counter(page_text)
    return word_counts

# Paso 3: Filtrar palabras clave relacionadas con SEO (como 'seo', 'google', 'ranking', etc.)
def filter_keywords(word_counts):
    keywords = ['seo', 'google', 'ranking', 'content', 'optimization', 'keywords', 'algorithm']
    filtered_counts = {word: count for word, count in word_counts.items() if word in keywords}
    return filtered_counts

# Paso 4: Visualizar los resultados con matplotlib
def plot_keyword_analysis(filtered_counts):
    if not filtered_counts:
        print("No se encontraron palabras clave relevantes.")
        return

    words = list(filtered_counts.keys())
    counts = list(filtered_counts.values())

    # Convertir a un array de numpy para una mayor eficiencia
    np_counts = np.array(counts)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(words, np_counts, color='skyblue')
    plt.xlabel('Palabras clave')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de palabras clave SEO en la página web')
    plt.show()

# URL de la página para analizar
url = 'https://www.jcchouinard.com/python-for-seo/'  # Cambiar por la URL que quieras analizar

# Ejecutamos el análisis
page_content = get_page_content(url)
if page_content:
    word_counts = analyze_keywords(page_content)
    filtered_counts = filter_keywords(word_counts)
    plot_keyword_analysis(filtered_counts)

