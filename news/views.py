from django.shortcuts import render
from decouple import config
import requests # faz requisições HTTP

def index(request):
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='+config('API_KEY')
    response = requests.get(url)

    try:
        data = response.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    if response.status_code == 200:
    
        for indice in data['articles']:
            print(f'''
                        Autor: {indice['author']}
                        Título: {indice['title']}
                    Descrição: {indice['description']}\n''')
    
        
    else:
        print('Não foi possível encontrar o artigo!')

    contexto = {
        "artigos": data['articles']
    }
    
    #artigo = data['articles']

    return render(request, 'index.html', contexto )
