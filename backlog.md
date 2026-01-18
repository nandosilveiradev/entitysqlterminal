# EntitySQLTerminal Backlog

## 📌 Backlog
- [ ] Add tests for `mode_controller`
  - [ ] Switching between local/server modes
- [ ] Add tests for `server_controller`
- [ ] Add tests for `tmux_controller`
- [ ] Add tests for `models/database`
  - [ ] Table creation
  - [ ] SQL generation
- [ ] Add tests for `views/cli_view`
  - [ ] Output messages
- [ ] Add tests for `views/i18n`
  - [ ] Portuguese translations
  - [ ] English translations
- [ ] Increase coverage to 70–80%
- [ ] Documentation
  - [ ] Create `README.md` with usage instructions
  - [ ] Document the full flow of entity and relation creation
  - [ ] Add examples of generated SQL output

---

## 🚧 In Progress
- [ ] Improve coverage of `LocalController`
  - [ ] Flows with VARCHAR
  - [ ] Flows with DECIMAL
  - [ ] Multiple attributes
- [ ] Improve coverage of `NormalizationController`
  - [ ] N:N case with extra table
- [ ] Create utility `get_attr(entity, name)` to simplify attribute checks in tests

---

## ✅ Done
- [x] Initial project structure (`controllers`, `models`, `views`)
- [x] Implementation of the `Entity` class with support for attributes and SQL generation
- [x] Implementation of `LocalController` for entity creation via CLI
- [x] Implementation of `NormalizationController` for relation normalization
- [x] Implementation of `state_view.update_view_state` to save state into a file
- [x] Pytest configuration and creation of `pytest.ini`
- [x] Creation of the `tests/` folder with unit and integration tests
- [x] Tests for `Entity` (SQL generation)
- [x] Tests for `LocalController` (mocked inputs and attributes)
- [x] Tests for `NormalizationController` (mocked relations)
- [x] Tests for `state_view` (file `view_state.txt`)
- [x] Integration test covering the full flow (LocalController → NormalizationController → state_view)
- [x] Initial test coverage reaching ~43%
- [x] Fixed test failures (`DummyView`, `DummyI18n`, attributes stored as list of dicts)
- [x] Added `.gitignore` to exclude `__pycache__`, `.coverage`, and temporary files
