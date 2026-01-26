from pathlib import Path

def lendo_html(
        path_html: Path,
        ) -> list[str]:
        
    with open(path_html,'r',encoding='utf-8') as html:
        lista_html = html.readlines()
        
    return lista_html

def removendo_item(
            lista_html: list[str],
            item_a_remover: str
            ) -> list[str]:
        
    removido = False
    escrever = True
    novo_html_list = []

    for i,item in enumerate(lista_html):

        if not removido:
            if i + 2 < len(lista_html) and item_a_remover in lista_html[i + 2]:
                escrever = False
                removido = True
                continue

        if escrever:
            novo_html_list.append(item)

        if "</li>" in item:
            escrever = True

    if not removido:
        print('Item não encontrado! Verifique ortografia.')
        
    return novo_html_list

def salvando_novo_html(
            nova_lista_html: list[str],
            local: Path
            ) -> Path:
        
    with open(local,'w+',encoding='utf-8') as f:
        f.writelines(nova_lista_html)

    return
    
def remover_item(
        item_a_remover: str,
        local_html: Path,
        destino: Path
        ) -> list[str]:
    
    lista_html = lendo_html(local_html)

    novo_html = removendo_item(lista_html,item_a_remover)

    salvando_novo_html(novo_html,destino)

    return novo_html

if __name__ == '__main__':

    pasta_atual = Path(__file__).parent
    arquivo_html = pasta_atual / 'view_lista.html'

    remover_item(
        'Passear com cachorro',
        arquivo_html,
        pasta_atual / 'novo_html.html'
    )

    print('Hello World!')