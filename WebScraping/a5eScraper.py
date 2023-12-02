

def a5e_scrape_source_text(name : str, sub_url : str, output_folder : str = r'Outputs\\') -> str:
    import requests

    spell = str.lower(name)
    url = f'https://a5e.tools/{sub_url}{name}'
    data = requests.get(url)

    # dump resulting text to file
    with open(output_folder + f"rich_content_{spell}.txt", "w+", encoding='utf-8') as out_f:
        out_f.write(data.text)
    
    return data.text