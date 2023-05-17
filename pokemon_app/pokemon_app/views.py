import requests
from django.shortcuts import render

def pokemon_list(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    data = response.json()
    pokemon_list = data['results']
    context = {'pokemon_list': pokemon_list}
    return render(request, 'pokemon_list.html', context)

def pokemon_detail(request, pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    data = response.json()
    abilities = data['abilities']
    context = {'abilities': abilities}
    return render(request, 'pokemon_detail.html', context)
