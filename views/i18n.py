# views/i18n.py

class I18n:
    def __init__(self, lang="en"):
        self.lang = lang

    def language_intro(self):
        return {
            "pt": "Selecione o idioma. Essa escolha é apenas para instruções do programa.",
            "en": "Select the language. This choice is only for program instructions."
        }[self.lang]

    def language_options(self):
        return {
            "pt": "1) Português\n2) English",
            "en": "1) Portuguese\n2) English"
        }[self.lang]

    def server_questions(self):
        return {
            "pt": "Informe os dados de conexão ao servidor:",
            "en": "Enter the server connection data:"
        }[self.lang]

    def local_selected(self):
        return {
            "pt": "Modo local selecionado. Os arquivos serão gerados aqui.",
            "en": "Local mode selected. Files will be generated here."
        }[self.lang]

    def connection_success(self):
        return {
            "pt": "Conexão estabelecida com sucesso!",
            "en": "Connection established successfully!"
        }[self.lang]

    def connection_failed(self):
        return {
            "pt": "Falha na conexão com o banco de dados.",
            "en": "Failed to connect to the database."
        }[self.lang]

    def ask_entity_name(self):
        return {
            "pt": "Digite o nome da entidade (Enter para terminar):",
            "en": "Enter entity name (press Enter to finish):"
        }[self.lang]

    def ask_attribute_name(self):
        return {
            "pt": "Digite o nome do atributo (Enter para terminar):",
            "en": "Enter attribute name (press Enter to finish):"
        }[self.lang]

    def ask_attribute_type(self):
        return {
            "pt": "Digite o tipo do atributo:",
            "en": "Enter attribute type:"
        }[self.lang]

    def ask_length_value(self):
        return {
            "pt": "Digite o tamanho (1 a 255):",
            "en": "Enter length (1 to 255):"
        }[self.lang]

    def ask_precision_value(self):
        return {
            "pt": "Digite a precisão (ex: 10):",
            "en": "Enter precision (e.g. 10):"
        }[self.lang]

    def ask_scale_value(self):
        return {
            "pt": "Digite a escala (ex: 2):",
            "en": "Enter scale (e.g. 2):"
        }[self.lang]

    def ask_not_null(self):
        return {
            "pt": "Esse atributo pode ser NULL? (s/n):",
            "en": "Can this attribute be NULL? (y/n):"
        }[self.lang]

    def ask_unique(self):
        return {
            "pt": "Esse atributo deve ser UNIQUE? (s/n):",
            "en": "Should this attribute be UNIQUE? (y/n):"
        }[self.lang]

    def ask_primary_key(self):
        return {
            "pt": "Esse atributo deve ser PRIMARY KEY? (s/n):",
            "en": "Should this attribute be PRIMARY KEY? (y/n):"
        }[self.lang]

    def ask_auto_increment(self):
        return {
            "pt": "Esse atributo deve ser AUTO INCREMENT? (s/n):",
            "en": "Should this attribute be AUTO INCREMENT? (y/n):"
        }[self.lang]

    def ask_more_entities(self):
        return {
            "pt": "Deseja criar outra entidade? (s/n):",
            "en": "Do you want to create another entity? (y/n):"
        }[self.lang]

    def invalid_option(self):
        return {
            "pt": "Opção inválida, tente novamente.",
            "en": "Invalid option, please try again."
        }[self.lang]

    def empty_entity_name(self):
        return {
            "pt": "O nome da entidade não pode ser vazio.",
            "en": "Entity name cannot be empty."
        }[self.lang]

    def empty_attribute_name(self):
        return {
            "pt": "O nome do atributo não pode ser vazio.",
            "en": "Attribute name cannot be empty."
        }[self.lang]

    def entity_created(self):
        return {
            "pt": "Entidade criada com sucesso!",
            "en": "Entity created successfully!"
        }[self.lang]

    def sql_generated(self):
        return {
            "pt": "Arquivo(s) SQL gerado(s) com sucesso.",
            "en": "SQL file(s) generated successfully."
        }[self.lang]

    def exit_program(self):
        return {
            "pt": "Encerrando o programa.",
            "en": "Exiting the program."
        }[self.lang]

    def goodbye(self):
        return {
            "pt": "Obrigado por usar o Entity SQL Terminal!",
            "en": "Thank you for using Entity SQL Terminal!"
        }[self.lang]

    def attribute_list_done(self):
        return {
            "pt": "Lista de atributos concluída.",
            "en": "Attribute list completed."
        }[self.lang]

    # 🔹 Nova pergunta essencial
    def ask_relation_exist(self, a, b):
        return {
            "pt": f"O {a} pode existir sem {b}? (s/n):",
            "en": f"Can {a} exist without {b}? (y/n):"
        }[self.lang]

    def ask_relation_many(self, a, b):
        return {
            "pt": f"Um {a} pode ter vários {b}s? (s/n):",
            "en": f"Can {a} have many {b}s? (y/n):"
        }[self.lang]

    def relation_result(self, a, b, relation_type):
        return {
            "pt": f"Resultado: relação {relation_type} entre {a} e {b}.",
            "en": f"Result: {relation_type} relation between {a} and {b}."
        }[self.lang]

    def ask_relation_extra_table(self, a, b, rel_table):
        return {
            "pt": f"Para relação entre {a} e {b} foi necessária a criação da tabela {rel_table}. Deseja criar mais atributos para essa tabela? (s/n):",
            "en": f"For relation between {a} and {b}, table {rel_table} was created. Do you want to add more attributes to this table? (y/n):"
        }[self.lang]

    def main_menu(self):
        return {
            "pt": "Selecione o modo de operação:\n1) Conectar ao servidor\n2) Gerar arquivos locais\n3) Encerrar programa",
            "en": "Select the operation mode:\n1) Connect to server\n2) Generate local files\n3) Exit program"
        }[self.lang]

    def list_databases(self, dbs):
        if self.lang == "pt":
            msg = "=== Bancos já criados ===\n"
        else:
            msg = "=== Databases created ===\n"
        for db in dbs:
            msg += f"- {db}\n"
        return msg
