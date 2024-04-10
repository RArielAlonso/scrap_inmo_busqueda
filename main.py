import httpx
from selectolax.parser import HTMLParser
import pandas as pd
from rich import print


def get_html(base_url):
    page_link = base_url + source
    page_link = base_url + source.replace(".html", f"-pagina-{page}.html")
    page = httpx.get(url=base_url)
    html = HTMLParser(page.text)
    return html


def extract_text(html, sel):
    try:
        return html.css(sel)
    except ArithmeticError:
        return None


def main():
    base_url = "https://www.inmobusqueda.com.ar/departamento-venta-la-plata-casco-urbano.html"
    html = get_html(base_url)
    deptos = [i.text() for i in extract_text(html, "div.resultadoTipo ")]
    detalles = [i.text() for i in extract_text(html, "div.resultadoLocalidad ")]
    precios = [i.text() for i in extract_text(html, "div.resultadoPrecio ")]
    descripciones = [i.text() for i in extract_text(html, "div.resultadoDescripcion ")]
    data = {"depto": deptos, "detalle": detalles, "precio": precios, "descripciones": descripciones}
    df = pd.DataFrame(data=data)
    print(df)

    return data


if __name__ == "__main__":
    main()
