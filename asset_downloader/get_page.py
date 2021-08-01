import requests


def main():
    res = requests.get('https://stargate-sgc.fandom.com/wiki/Glyph')
    data = res.text
    with open('./glyph.html', 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    main()
