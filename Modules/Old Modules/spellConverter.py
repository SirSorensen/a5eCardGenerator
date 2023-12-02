import pip._vendor.requests as requests
import re

def extractType(inputStr : str, filetext : str) -> str:
    spell_level_regex = r'(?<=<div class="field field--name-field-)' + inputStr + r'[^>]*>(?:\s*<\s*a[^>]*>)?([\w ]*)<'
    result = re.search(spell_level_regex, filetext)
    if result:
        print(result.group(1))

spell = str.lower("ACCELERANDO")
url = f'https://a5e.tools/spell/{spell}'
data = requests.get(url)

# dump resulting text to file
with open(f"original_{spell}.txt", "r") as data:
    dataText = data.read()
    data.close()
    extractType("spell-level", dataText)
    extractType("classical-spell-school", dataText)
    extractType("spellcomponent-description", dataText)



