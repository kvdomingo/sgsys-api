import json
import requests
from tqdm import tqdm


def main():
    with open('./glyph.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for dat in tqdm(data):
        res = requests.get(dat['glyph'], stream=True)
        if res.status_code == 200:
            with open(f'./glyphs-mw/{dat["name"].lower().replace(" ", "_")}.svg', 'wb') as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)


if __name__ == '__main__':
    main()
