#!/bin/bash

while read -r line; do
  # Só pega linhas que começam com "- [ ]"
  if [[ $line == "- [ ] "* ]]; then
    # Remove o prefixo "- [ ] " e guarda o resto como título
    title="${line#- [ ] }"
    # Cria a issue no GitHub
    gh issue create --title "$title" --body "Imported from backlog.md" --label "backlog"
  fi
done < backlog.md


