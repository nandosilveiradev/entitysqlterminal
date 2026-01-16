# 📘 Entity SQL Terminal
Ferramenta em linha de comando para gerar arquivos SQL ou conectar a um servidor PostgreSQL e manipular entidades de forma prática e persistente.

## 🎯 Objetivo
O Entity SQL Terminal foi criado para:
- Simplificar a manipulação de entidades em bancos PostgreSQL.
- Automatizar a geração de arquivos SQL.
- Oferecer um fluxo interativo com suporte a múltiplos idiomas (PT/EN).
- Permitir testes rápidos de conexão e execução de queries em ambiente local ou remoto.

---

## 🚀 Pré-requisitos
- Python 3.10+
- Docker (opcional, apenas se quiser rodar um banco PostgreSQL localmente)
- Git (para clonar o repositório)

---

## 🔧 Configuração do ambiente
Este projeto usa **venv** para isolar dependências:

    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\Activate.ps1  # Windows PowerShell
    pip install -r requirements.txt

---

## 🐘 Banco de dados PostgreSQL com Docker (Opcional)
O projeto já inclui um `docker-compose.yml` para subir o banco, mas **não é obrigatório**.  
O programa funciona mesmo sem executar o container — essa opção é útil apenas se você tiver um projeto real que precise criar e conectar a um banco de dados.

Para subir o banco via Docker:

    docker-compose up -d

Configuração padrão:
- Host: `localhost`
- Porta: `5000`
- Usuário: `nando`
- Senha: `secret`
- Banco: `entitydb`

---

## ▶️ Executando o programa
    python3 entity-sql-cli.py

Fluxo de execução:
1. Escolher idioma (Português ou English).
2. Escolher modo (Server ou Local).
3. Se for **Server**, informar dados de conexão (opcional).
4. O programa testa a conexão e retorna sucesso ou erro.
5. Se for **Local**, gera arquivos SQL a partir das entidades.

---

## 📂 Estrutura do projeto
    entitysqlterminal/
    ├── controllers/
    │   ├── mode_controller.py        # Controla o modo de execução (server/local)
    │   ├── server_controller.py      # Gerencia conexões com PostgreSQL
    │   └── connection_tester.py      # Testa conexões com o banco
    ├── views/
    │   ├── cli_view.py               # Interface de linha de comando
    │   └── i18n.py                   # Internacionalização (PT/EN)
    ├── entity-sql-cli.py             # Ponto de entrada principal
    ├── docker-compose.yml            # Configuração opcional do banco PostgreSQL
    └── requirements.txt              # Dependências do projeto

---

## ✅ Checklist
- [x] Escolha de idioma (PT/EN)
- [x] Escolha de modo (server/local)
- [x] Coleta de dados de conexão
- [x] Teste de conexão com PostgreSQL
- [x] Ambiente virtual com requirements.txt
- [x] Banco PostgreSQL via Docker (opcional)

---

## 📌 Roadmap
- [ ] Implementar geração automática de entidades SQL a partir de modelos.
- [ ] Adicionar suporte a outros bancos (MySQL, SQLite).
- [ ] Criar exportação de resultados para CSV/JSON.
- [ ] Melhorar interface CLI com comandos adicionais.
- [ ] Adicionar testes unitários e integração contínua.
- [ ] Documentar exemplos de uso no Wiki.

---

## 🤝 Contribuindo
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Adicionei minha feature'`).
4. Faça push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

---

## 📝 License
Este projeto está licenciado sob a MIT License.
