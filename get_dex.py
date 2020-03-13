from os import path
import requests, json

if not path.exists("pokemons.json"):
  pkms = requests.get("https://www.pokemon.com/us/api/pokedex/kalos").json()

  pkm_json = []
  last = 0

  for pkm in pkms:
    if (last != pkm['id']):
      pkm_json.append({
        'id':         pkm['id'],
        'number':     pkm['number'],
        'name':       pkm['name'],
        'slug':       pkm['slug'],
        'type':       pkm['type'],
        'weakness':   pkm['weakness'],
        'abilities':  pkm['abilities'],
        'weight':     pkm['weight'],
        'height':     pkm['height'],
        'image':      pkm['ThumbnailImage']
      })
    
    last = pkm['id']

  f = open("pokemons.json", "w")
  f.write(json.dumps(pkm_json, indent=2))
  f.close()
  print("Pokemon Json Done!")
else:
  f = open("pokemons.json", "r")
  pkms = json.loads(f.read());

  print(len(pkms))

  