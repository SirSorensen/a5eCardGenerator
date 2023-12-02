import requests
import re

spell = str.lower("ACCELERANDO")
url = f'https://a5e.tools/spell/{spell}'
data = requests.get(url)

# dump resulting text to file
with open(f"original_{spell}.txt", "w") as out_f:
    out_f.write(data.text)