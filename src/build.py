#!/usr/bin/env python3
"""Genera index.html a partir de src/template.html embebiendo fuentes e
imagenes como data URIs, para que la pagina sea un unico archivo autocontenido
(ideal para GitHub Pages). Uso: python src/build.py"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
APP_URL = "https://eduardo123-test-golazo.expo.app"


def data_uri(path: pathlib.Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


repl = {
    "__FONT500__": data_uri(ASSETS / "fonts/BarlowCondensed_500Medium.ttf", "font/ttf"),
    "__FONT700__": data_uri(ASSETS / "fonts/BarlowCondensed_700Bold.ttf", "font/ttf"),
    "__FONT900__": data_uri(ASSETS / "fonts/BarlowCondensed_900Black.ttf", "font/ttf"),
    "__LOGO__": data_uri(ASSETS / "logo.png", "image/png"),
    "__SHOT_HOME__": data_uri(ASSETS / "shot-inicio.png", "image/png"),
    "__SHOT_PERFIL__": data_uri(ASSETS / "shot-perfil.png", "image/png"),
    "__SHOT_RANKING__": data_uri(ASSETS / "shot-ranking.png", "image/png"),
    "__SHOT_EVENTOS__": data_uri(ASSETS / "shot-eventos.png", "image/png"),
    "__APP__": APP_URL,
}

html = (ROOT / "src/template.html").read_text(encoding="utf-8")
# GitHub Pages sirve el archivo dentro de <html><body>; anadimos el envoltorio.
html = "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\" />\n" + html
# El template ya trae <title>, <meta viewport>, <meta description> y <style>;
# cerramos head/body alrededor del contenido restante.
html = html.replace("</style>\n", "</style>\n</head>\n<body>\n", 1)
html += "\n</body>\n</html>\n"

for token, value in repl.items():
    html = html.replace(token, value)

leftover = [t for t in repl if t in html]
assert not leftover, f"tokens sin reemplazar: {leftover}"

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
size_mb = round(len(html.encode("utf-8")) / 1024 / 1024, 2)
print(f"OK: {out} ({size_mb} MB)")
