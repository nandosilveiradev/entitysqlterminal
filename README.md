# 📘 Entity SQL Terminal# 

[English README](README.md) | [Português README](pt-README.md)

Command-line tool to generate SQL files or connect to a PostgreSQL server and manage entities in a practical and persistent way.




## 🎯 Purpose
Entity SQL Terminal was created to:
- Simplify entity management in PostgreSQL databases.
- Automate SQL file generation.
- Provide an interactive workflow with multi-language support (PT/EN).
- Allow quick connection tests and query execution in local or remote environments.

---

## 🚀 Prerequisites
- Python 3.10+
- Docker (optional, only if you want to run a local PostgreSQL database)
- Git (to clone the repository)

---

## 🔧 Environment Setup
This project uses **venv** to isolate dependencies:

    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\Activate.ps1  # Windows PowerShell
    pip install -r requirements.txt

---

## 🐘 PostgreSQL Database with Docker (Optional)
The project already includes a `docker-compose.yml` to spin up the database, but **it is not mandatory**.  
The program works even without running the container — this option is useful only if you have a real project that needs to create and connect to a database.

To start the database with Docker:

    docker-compose up -d

Default configuration:
- Host: `localhost`
- Port: `5000`
- User: `nando`
- Password: `secret`
- Database: `entitydb`

---

## ▶️ Running the Program
    python3 entity-sql-cli.py

Execution flow:
1. Choose language (Portuguese or English).
2. Choose mode (Server or Local).
3. If **Server**, provide connection data (optional).
4. The program tests the connection and returns success or error.
5. If **Local**, it generates SQL files from entities.

---

## 📂 Project Structure
    entitysqlterminal/
    ├── controllers/
    │   ├── mode_controller.py        # Controls execution mode (server/local)
    │   ├── server_controller.py      # Manages PostgreSQL connections
    │   └── connection_tester.py      # Tests database connections
    ├── views/
    │   ├── cli_view.py               # Command-line interface
    │   └── i18n.py                   # Internationalization (PT/EN)
    ├── entity-sql-cli.py             # Main entry point
    ├── docker-compose.yml            # Optional PostgreSQL configuration
    └── requirements.txt              # Project dependencies

---

## ✅ Checklist
- [x] Language selection (PT/EN)
- [x] Mode selection (server/local)
- [x] Connection data collection
- [x] PostgreSQL connection test
- [x] Virtual environment with requirements.txt
- [x] PostgreSQL database via Docker (optional)

---

## 📌 Roadmap
- [ ] Implement automatic SQL entity generation from models.
- [ ] Add support for other databases (MySQL, SQLite).
- [ ] Create export of results to CSV/JSON.
- [ ] Improve CLI interface with additional commands.
- [ ] Add unit tests and continuous integration.
- [ ] Document usage examples in the Wiki.

---

## 🤝 Contributing
1. Fork the repository.
2. Create a branch for your feature (`git checkout -b my-feature`).
3. Commit your changes (`git commit -m 'Added my feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a Pull Request.

---

## 📝 License
This project is licensed under the MIT License.