from pathlib import Path
from bs4 import BeautifulSoup

def remover_item(item_a_remover: str, local_html: Path, destino: Path) -> None:
    html = local_html.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")

    for li in soup.find_all("li"):
        texto = li.get_text(strip=True)
        if texto == item_a_remover:
            li.decompose()

    destino.write_text(str(soup), encoding="utf-8")

    return

if __name__ == "__main__":

    pasta_atual = Path(__file__).parent

    remover_item('Almoçar',
                 pasta_atual / 'view_lista.html',
                 pasta_atual / 'novo_html.html'
                 )