def stringmod(text):
    maganh = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    original_text = text
    for maganh in maganh:
        original_text = original_text.replace(maganh, '')
    return original_text


print(stringmod("Ez egy példa szöveg magánhangzókkal."))