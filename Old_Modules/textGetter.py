import requests
import re

output_folder = r'Outputs\\'

spell = str.lower("ACCELERANDO")
url = f'https://a5e.tools/spell/{spell}'
data = requests.get(url)

# dump resulting text to file
with open(output_folder + f"original_{spell}.txt", "w", encoding='utf-8') as out_f:
    out_f.write(data.text)