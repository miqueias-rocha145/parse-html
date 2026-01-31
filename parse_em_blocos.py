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
        
    escrever_bloco = True
    novo_html_list = []
    bloco_temp_html = []
    dentro_bloco = False

    for i,item in enumerate(lista_html):
        
        if item.strip().startswith("<li class"):
            dentro_bloco = True

        if dentro_bloco:

            if item_a_remover == item.strip():
                escrever_bloco = False

            bloco_temp_html.append(item)

            if item.strip().startswith("</li>"):
                dentro_bloco = False
                
                if escrever_bloco:
                    novo_html_list.extend(bloco_temp_html)
                
                bloco_temp_html = []
                escrever_bloco = True

            continue

        novo_html_list.append(item)
        
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
        'Almoçar',
        arquivo_html,
        pasta_atual / 'novo_html.html'
    )
