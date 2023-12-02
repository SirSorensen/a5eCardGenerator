import requests
import re
from bs4 import BeautifulSoup

spell = str.lower("ACCELERANDO")
url = f'https://a5e.tools/spell/{spell}'
data = requests.get(url)

if False:
    data = BeautifulSoup(data.text, "html.parser")
    data = re.sub(r'(?:\n[^\S\n]*){3,}', r'\n\n', data.text)

    # dump resulting text to file
    with open(f"soup_{spell}.txt", "w") as out_f:
        out_f.write(data)
else:
    # dump resulting text to file
    with open(f"original_{spell}.txt", "w") as out_f:
        out_f.write(data.text)