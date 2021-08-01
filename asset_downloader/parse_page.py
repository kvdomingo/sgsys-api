import json
from bs4 import BeautifulSoup


def main():
    with open('./glyph.html', 'r', encoding='utf-8') as f:
        data = str.join('', f.readlines())
    soup = BeautifulSoup(data, features='html.parser')
    mw_glyphs, p_glyphs, d_glyphs = soup.select('table.wikitable')
    table_row = mw_glyphs.select('tr')[1::]
    glyph_list = []
    for tr in table_row:
        table_data = tr.select('td')
        glyph_positions = table_data[::3]
        glyph_images = table_data[1::3]
        glyph_names = table_data[2::3]
        for pos, im, name in zip(glyph_positions, glyph_images, glyph_names):
            if not im.a.img.get('src').startswith('http'):
                im_glyph = im.a.img.get('data-src')
            else:
                im_glyph = im.a.img.get('src')
            glyph_list.append(dict(
                position=pos.text.strip(),
                glyph=f'{im_glyph.split(".svg")[0]}.svg',
                name=name.a.text,
            ))
    with open('./glyph.json', 'w', encoding='utf-8') as f:
        json.dump(glyph_list, f, indent=2)


if __name__ == '__main__':
    main()
