

def a5e_scrape_source_text(name : str, sub_url : str, output_folder : str = r'Outputs\\') -> str:
    import requests

    name = str.lower(name)
    output_filepath = f"{output_folder}source_text_{name}.txt"

    url = f'https://a5e.tools/{sub_url}{name}'
    data = requests.get(url)

    # dump resulting text to file
    with open(output_filepath, "w+", encoding='utf-8') as output_file:
        output_file.write(data.text)
    
    return data.text
