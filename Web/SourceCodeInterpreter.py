
import re


def extractType(inputStr : str, file_text : str) -> str:
    spell_level_regex = r'(?<=<div class="field field--name-field-)' + inputStr + r'[^>]*>(?:\s*<\s*a[^>]*>)?([\w ]*)<'
    result = re.search(spell_level_regex, file_text)
    if result:
        return result.group(1)
    else:
        return ""