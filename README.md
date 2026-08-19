# Fushibol · Landing page

Pagina de aterrizaje de **Fushibol**, la app del futbol amateur en Bolivia: arma
tu equipo, entra a torneos, reta a otros equipos y lleva tus estadisticas como un
profesional.

- **App web:** https://eduardo123-test-golazo.expo.app
- **Estilo:** fanzine / programa de partido (neobrutalista). Tipografia Barlow
  Condensed, monoespaciada para los datos, papel tiza + verde botella + naranja.

> El dominio de marca sera **fushibol.com** (en gestion).

## Ver la pagina

`index.html` es un unico archivo autocontenido (fuentes e imagenes van embebidas
como data URIs), asi que se abre directo en el navegador o se sirve tal cual.

```bash
python -m http.server 8000
# luego abrir http://localhost:8000
```

### Publicar en GitHub Pages

En **Settings > Pages**, elegir la rama `main` y la carpeta raiz (`/`). La pagina
queda disponible en `https://eduardoshande.github.io/Golazo-landing-page/`, y luego
se puede apuntar el dominio `fushibol.com` a GitHub Pages.

## Regenerar `index.html`

El HTML final se genera desde `src/template.html` y los binarios de `assets/`.
Si editas el template o cambias una captura, reconstruye con:

```bash
python src/build.py
```

## Estructura

```
index.html            Pagina final autocontenida (generada, lista para desplegar)
src/template.html     Plantilla editable (tokens __FONT__ / __SHOT_*__ / __APP__)
src/build.py          Embebe fuentes e imagenes y escribe index.html
assets/               Logo, capturas reales de la app y fuentes Barlow Condensed
```

## Creditos

- Tipografia: [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) (SIL Open Font License).
- Capturas: pantallas reales de la app Fushibol.
