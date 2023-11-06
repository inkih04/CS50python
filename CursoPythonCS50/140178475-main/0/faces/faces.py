def replace(texto):
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }

    for emoticono in emojis:
        texto = texto.replace(emoticono, emojis.get(emoticono))
    return texto


texto = input()
print(replace(texto), end ="")