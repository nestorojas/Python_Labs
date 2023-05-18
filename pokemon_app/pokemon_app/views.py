"""
Module: pokemon_app.views

This module contains the views for the Pokemon application.
It provides functionality for retrieving and displaying Pokemon information.

Author: Your Name
Date: May 17, 2023
"""

import requests
from django.shortcuts import render

def home(request):
    """
    Add any necessary logic or data retrieval here.
    ...
    """
    context = {
        'message': 'Welcome to the Pokemon API!',
    }
    return render(request, 'home.html', context)

def get_pokemon_list(request):
    """
    Retrieve a list of Pokémon from the Pokémon API.
    ...
    """
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0', timeout=5)
    data = response.json()
    pokemon_list = data['results']
    context = {'pokemon_list': pokemon_list}
    return render(request, 'pokemon_list.html', context)



def pokemon_detail(request, pokemon_name):
    """
    Retrieve details of Pokémon from the Pokémon API.
    ...
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url, timeout=5)
    data = response.json()
    abilities = data['abilities']
    pokemon_name = data['name']

    context = {
        'abilities': abilities,
        'pokemon': {
            'name': pokemon_name,
        }
    }
    return render(request, 'pokemon_detail.html', context)
