import json, requests, shutil, re
from os import path

def formatPokemonId(id):
  return str(id).zfill(3)

def formatPokemonName(name):
  return name.lower().replace("-female", "-f").replace("-male", "-m").replace("meowstic", "meowstic-m")

f = open("pokemons.json", "r", encoding="utf8")
pkms = json.loads(f.read())
f.close()

# Get Pokemon Ingame Gifs
for pkm in pkms:
  if not path.exists("media/ingame-gif/%s.gif" % formatPokemonId(pkm['number'])):
    name = formatPokemonName(pkm['slug'])
    img = requests.get("https://www.smogon.com/dex/media/sprites/xy/%s.gif" % name, stream=True)
    file = open("media/ingame-gif/%s.gif" % formatPokemonId(pkm['number']), "wb")
    img.raw.decode_content = True
    shutil.copyfileobj(img.raw, file)
    del img
print("Ingame Gif Done!")

# Get Pokemon Ingame Images
for pkm in pkms:
  if not path.exists("media/ingame-png/%s.png" % formatPokemonId(pkm['number'])):
    img = requests.get("https://serebii.net/swordshield/pokemon/%s.png" % formatPokemonId(pkm['number']), stream=True)
    file = open("media/ingame-png/%s.png" % formatPokemonId(pkm['number']), "wb")
    img.raw.decode_content = True
    shutil.copyfileobj(img.raw, file)
    del img
print("Ingame Png Done!")

# Get Pokemon Drawn Images
for pkm in pkms:
  if not path.exists("media/drawn-png/%s.png" % formatPokemonId(pkm['number'])):
    img = requests.get("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/%s.png" % formatPokemonId(pkm['number']), stream=True)
    file = open("media/drawn-png/%s.png" % formatPokemonId(pkm['number']), "wb")
    img.raw.decode_content = True
    shutil.copyfileobj(img.raw, file)
    del img
print("Drawn Png Done!")
