"""
Script que lê logs de erro e atualiza o arquivo py_patterns.json
"""

import json

def carregar_erros_existentes(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def registrar_erro(caminho, novo_erro):
    erros = carregar_erros_existentes(caminho)
    if novo_erro not in erros:
        erros.append(novo_erro)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(erros, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    erro_exemplo = {
        "erro": "SyntaxError: unexpected indent",
        "correcao": "verifique espaços e tabulações inconsistentes",
        "padrão": "indentação incorreta",
        "tag": "syntax-error"
    }
    registrar_erro("../knowledge/py_patterns.json", erro_exemplo)