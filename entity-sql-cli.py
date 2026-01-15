def escolher_idioma():
    # Primeiro print: explicação em PT e EN
    print("Selecione o idioma. Essa escolha serve apenas para traduzir as instruções do programa.")
    print("Não altera o banco de dados nem os arquivos gerados.\n")
    print("Select the language. This choice is only to translate the program instructions.")
    print("It does not change the database or the generated files.\n")

    # Segundo print: opções
    print("1) Português")
    print("2) English")

    escolha = input("> ").strip()
    if escolha == "2":
        return "en"
    return "pt"

if __name__ == "__main__":
    lang = escolher_idioma()
    print(f"Idioma selecionado: {lang}")
