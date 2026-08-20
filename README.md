# Fushibol · Landing page

Pagina de aterrizaje de **Fushibol**, la app del futbol amateur en Bolivia.

- **Sitio en vivo:** https://fushibol.com
- **App:** https://app.fushibol.com
- **Estilo:** minimalista / ensayo fotografico. Fondo casi negro, fotografia a
  todo el ancho, tipografia condensada (Barlow Condensed) y mucho espacio.

## Como funciona

`index.html` es una pagina estatica hecha a mano que referencia los archivos de
`assets/` directamente (fotos, fuentes, capturas). **No hay paso de build**: se
edita `index.html` y se sube. GitHub Pages sirve todo el repo.

```bash
python -m http.server 8000   # abrir http://localhost:8000
```

## Estructura

```
index.html            La pagina (editable directo)
CNAME                 Dominio propio (fushibol.com)
assets/
  fonts/              Barlow Condensed (500/700/900)
  hero.jpg, cta.jpg   Fotos full-bleed
  feat-1..4.jpg       Fotos de las secciones
  cs-1..6.jpg         Contact sheet
  shot-*.png          Capturas reales de la app
  logo.png            Logo
```

Las fotos salen de `../images` (stock de futbol) procesadas con PIL.

## Publicar en GitHub Pages

Settings > Pages > rama `main`, carpeta raiz. El dominio `fushibol.com` se toma
del archivo `CNAME`.
