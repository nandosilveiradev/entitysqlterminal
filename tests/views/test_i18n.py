from entitysqlterminal.views.i18n import I18n, messages


def test_all_messages():
    for key, translations in messages.items():
        for lang, text in translations.items():
            i18n = I18n(lang=lang)
            result = i18n.text(key)
            assert result == text, f"Erro na chave {key} para idioma {lang}"
