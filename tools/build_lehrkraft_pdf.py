#!/usr/bin/env python3
"""Erzeugt build/So-arbeiten-wir.pdf: die Seite "So arbeiten wir" (Scrum-
Arbeitsweise) als eigenständiges Dokument für Lehrkräfte - z. B. zum
Ausdrucken oder Weitergeben, ohne die komplette Lerneinheit.

Nutzt dieselbe Aufbereitung wie build.py (Formeln, Bilder, Links in
Bildunterschriften), damit sich an dieser Seite nichts extra pflegen lässt -
sie kommt unverändert aus src/pages/01-agil.md.
"""
import asyncio, datetime, os, sys
from playwright.async_api import async_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as nuk

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'src')
PAGE_FILE = os.path.join(SRC, 'pages', '01-agil.md')
OUT_HTML = os.path.join(HERE, '..', 'build', 'So-arbeiten-wir.html')
OUT_PDF = os.path.join(HERE, '..', 'build', 'So-arbeiten-wir.pdf')


def build_html():
    meta, body = nuk.parse_page(PAGE_FILE)
    h = nuk.render_md(body)
    nuk._render_math()
    h = nuk._insert_math(h)
    h = nuk.figures(h)
    h = nuk._insert_caption_links(h)
    h = nuk.embed_images(h)

    css = open(os.path.join(SRC, 'style.css'), encoding='utf-8').read()
    stamp = datetime.date.today().strftime('%d.%m.%Y')
    title = nuk.html.escape(meta['title'])

    doc = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
main.content{{max-width:800px;margin:0 auto;padding:1.5em}}
/* Nur für dieses PDF: die als .pdf-break markierten Überschriften
   beginnen immer auf einer neuen Seite (samt Überschrift), unabhängig
   davon, wie viel Text vorher noch auf die Seite passen würde. */
@media print {{
  h2.pdf-break {{ break-before: page; page-break-before: always; }}
}}
</style>
</head>
<body>
<main class="content">
<article class="page" id="{meta['id']}">
<header class="pagehead"><h1>{title}</h1></header>
{h}
</article>
</main>
<footer class="sitefoot">Auszug aus der Lerneinheit Nuklearmedizin (Physik 9/10) · Stand {stamp}</footer>
</body>
</html>'''
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    open(OUT_HTML, 'w', encoding='utf-8').write(doc)
    print(f'geschrieben: {OUT_HTML} ({os.path.getsize(OUT_HTML)/1024:.0f} KB)')


async def build_pdf():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto('file://' + OUT_HTML)
        await pg.emulate_media(media='print')
        try:
            await asyncio.wait_for(pg.evaluate('''async () => {
                const imgs = [...document.images];
                imgs.forEach(i => { i.loading = 'eager'; });
                await Promise.all(imgs.map(i => i.complete ? null :
                    new Promise(r => {
                        i.addEventListener('load', r, {once: true});
                        i.addEventListener('error', r, {once: true});
                        setTimeout(r, 10000);
                    })));
            }'''), timeout=30)
        except asyncio.TimeoutError:
            print('! Warnung: Warten auf Bilder hat das Timeout überschritten, fahre trotzdem fort', file=sys.stderr)
        await pg.pdf(path=OUT_PDF, format='A4', print_background=True,
                     margin={'top': '15mm', 'bottom': '15mm', 'left': '15mm', 'right': '15mm'})
        await b.close()
    print(f'geschrieben: {OUT_PDF} ({os.path.getsize(OUT_PDF)/1024:.0f} KB)')


def main():
    build_html()
    asyncio.run(build_pdf())


if __name__ == '__main__':
    main()
